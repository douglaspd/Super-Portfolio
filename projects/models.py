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


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    github_url = models.URLField()
    keyword = models.CharField(max_length=50)
    key_skill = models.CharField(max_length=50)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    def clean(self):
        if any(
            len(field) > 500
            for field in [
                self.name,
                self.description,
                self.keyword,
                self.key_skill,
            ]
        ):
            raise ValidationError(
                "Os campos não podem ter mais que 500 caracteres"
            )

    def __str__(self) -> str:
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    url = models.URLField(blank=False, null=False)

    def clean(self) -> None:
        if len(self.name) > 500 or len(self.url) > 500:
            raise ValidationError(
                " Os campos não podem ter mais que 500 caracteres"
            )

    def __str__(self) -> str:
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
        blank=False,
        null=False,
    )
    timestamp = models.DateTimeField(
        auto_now_add=True, blank=False, null=False
    )
    profiles = models.ManyToManyField(
        "Profile", related_name="certificates", blank=False, null=False
    )

    def __str__(self) -> str:
        return self.name

    def clean(self) -> None:
        if (
            any(
                len(
                    self.name,
                    self.certifying_institution,
                    self.timestamp,
                    self.profiles,
                )
            )
            > 500
        ):
            raise ValidationError(
                " Os campos não devem ter mais que 500 caracteres"
            )
