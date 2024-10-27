from django.db import models

from common.models import BaseModel


class AuthorModel(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
