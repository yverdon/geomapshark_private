from django.db import models
from django.db.models.fields.files import FieldFile
from django.urls import reverse

from geocity.fields import PrivateFileSystemStorage, PublicFileSystemStorage


class AdministrativeEntityFieldFile(FieldFile):
    @property
    def url(self):
        return reverse(
            "accounts:administrative_entity_file_download",
            kwargs={"path": self.name},
        )


class AdministrativeEntityFileField(models.FileField):
    """
    FileField storing information in a private media root.
    """

    attr_class = AdministrativeEntityFieldFile

    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs["storage"] = PrivateFileSystemStorage()
        super().__init__(verbose_name, name, **kwargs)


class CustomLoginImageFieldFile(FieldFile):
    """
    FieldFile for storing public image for site customization
    """

    @property
    def url(self):

        return reverse(
            "accounts:site_profile_custom_image",
            kwargs={"path": self.name},
        )


class CustomLoginImageFileField(models.FileField):
    """
    FileField storing public image for site customization
    """

    attr_class = CustomLoginImageFieldFile

    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs["storage"] = PublicFileSystemStorage()
        super().__init__(verbose_name, name, **kwargs)
