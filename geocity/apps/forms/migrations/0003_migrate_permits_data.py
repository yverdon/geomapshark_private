# Generated by Django 3.2.15 on 2022-10-12 09:59

from django.db import migrations

from geocity.migrations import (
    bulk_create,
    common_fields_values,
    copy_model,
    copy_tags,
    migrate_contenttypes,
    sync_sequence,
)


def create_form_categories(apps, schema_editor):
    WorksType = apps.get_model("permits", "WorksType")
    FormCategory = apps.get_model("forms", "FormCategory")

    for works_type in WorksType.objects.all():
        values = common_fields_values(FormCategory, works_type)
        form_category = FormCategory.objects.create(**values)
        copy_tags(
            apps,
            from_obj=works_type,
            to_obj=form_category,
        )


def create_forms(apps, schema_editor):
    WorksObjectType = apps.get_model("permits", "WorksObjectType")
    WorksObjectProperty = apps.get_model("permits", "WorksObjectProperty")

    Form = apps.get_model("forms", "Form")
    Field = apps.get_model("forms", "Field")
    FormField = apps.get_model("forms", "FormField")

    copy_model(WorksObjectProperty, Field)

    def forms():
        for works_object_type in WorksObjectType.objects.select_related(
            "works_type", "works_object"
        ):
            values = common_fields_values(Form, works_object_type)
            values.update(
                {
                    "name": works_object_type.works_object.name,
                    "order": works_object_type.works_object.order,
                    "wms_layers": works_object_type.works_object.wms_layers,
                    "wms_layers_order": works_object_type.works_object.wms_layers_order,
                    "category_id": works_object_type.works_type_id,
                }
            )

            yield Form(**values)

    def form_fields():
        order = 0
        last_wot_id = None
        for (
            works_object_type_through
        ) in WorksObjectProperty.works_object_types.through.objects.order_by(
            "worksobjecttype__id", "worksobjectproperty__order"
        ):
            if works_object_type_through.worksobjecttype_id != last_wot_id:
                last_wot_id = works_object_type_through.worksobjecttype_id
                order = 0
            else:
                order += 1

            yield FormField(
                id=works_object_type_through.id,
                form_id=works_object_type_through.worksobjecttype_id,
                field_id=works_object_type_through.worksobjectproperty_id,
                order=order,
            )

    def administrative_entity_through():
        for (
            administrative_entity_through
        ) in WorksObjectType.administrative_entities.through.objects.all():
            values = common_fields_values(
                Form.administrative_entities.through, administrative_entity_through
            )
            values["form_id"] = administrative_entity_through.worksobjecttype_id
            values[
                "administrativeentity_id"
            ] = administrative_entity_through.permitadministrativeentity_id
            yield Form.administrative_entities.through(**values)

    bulk_create(forms())
    bulk_create(form_fields())
    bulk_create(administrative_entity_through())


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0002_geom_intersection_enabled_shortname"),
        ("permits", "0084_add_shortname_and_change_text"),
        ("contenttypes", "0001_initial"),
        ("accounts", "0003_migrate_permits_data"),
    ]

    operations = [
        migrations.RunPython(migrate_contenttypes),
        migrations.RunPython(create_form_categories),
        sync_sequence("forms_formcategory"),
        migrations.RunPython(create_forms),
        sync_sequence("forms_form"),
        sync_sequence("forms_field"),
        sync_sequence("forms_formfield"),
        sync_sequence("forms_form_administrative_entities"),
    ]
