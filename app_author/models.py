from django.db import models

from common.models import BaseModel


class AuthorModel(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Authors"
        verbose_name = "Author"
