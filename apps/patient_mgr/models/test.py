from django.db import models

from apps.base.models import BaseModel


class TestModel(BaseModel):
    test = models.CharField(verbose_name='test', max_length=64)
