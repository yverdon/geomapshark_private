from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models
from django import forms as djforms


admin.site.register(models.WorksType)
admin.site.register(models.WorksObject)
admin.site.register(models.PermitRequest)
admin.site.register(models.PermitActorType)
admin.site.register(models.PermitRequestActor)
admin.site.register(models.PermitActor)
admin.site.register(models.PermitRequestGeoTime)
admin.site.register(models.PermitAuthor)
admin.site.register(models.PermitDepartment)
admin.site.register(models.PermitRequestValidation)
admin.site.register(models.GeomLayer)
admin.site.register(models.WorksObjectPropertyValue)


def works_object_type_administrative_entities(obj):
    return ", ".join(administrative_entity.name for administrative_entity in obj.administrative_entities.all())


works_object_type_administrative_entities.short_description = _("Communes")


class WorksObjectTypeAdmin(admin.ModelAdmin):
    list_display = ['__str__', works_object_type_administrative_entities]
    list_filter = ['administrative_entities']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('works_object', 'works_type').prefetch_related('administrative_entities')


class WorksObjectPropertyAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_mandatory']


class PermitAdministrativeEntityAdminForm(djforms.ModelForm):

    class Meta:
        model = models.PermitAdministrativeEntity
        fields = '__all__'
        widgets = {
            'general_informations': djforms.Textarea(attrs={'rows': 5, }),
        }


class PermitAdministrativeEntityAdmin(admin.ModelAdmin):
    form = PermitAdministrativeEntityAdminForm


admin.site.register(models.WorksObjectType, WorksObjectTypeAdmin)
admin.site.register(models.WorksObjectProperty, WorksObjectPropertyAdmin)
admin.site.register(models.PermitAdministrativeEntity, PermitAdministrativeEntityAdmin)
