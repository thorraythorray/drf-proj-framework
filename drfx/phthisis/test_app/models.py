from django.db import models

from drfx.base.model import BaseModel


class TestModel(BaseModel):
    test = models.CharField(verbose_name='test', max_length=64)
