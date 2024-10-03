from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    github = models.URLField(max_length=500, blank=False, null=False)
    linkedin = models.URLField(max_length=500, blank=False, null=False)
    bio = models.TextField(blank=False, null=False)

    def clean(self):
        if len(self.bio) > 500:
            return ValidationError("Bio não pode ter mais que 500 caracteres")

    def __str__(self) -> str:
        return self.name
