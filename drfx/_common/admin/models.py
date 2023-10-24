from django.contrib.auth.models import AbstractUser
from django.db import models

from drfx._common.orm import BaseModel


class Groups(BaseModel):
    name = models.CharField(max_length=64, verbose_name='分级名称')
    level = models.IntegerField(verbose_name='层级等级', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='child_groups', verbose_name='父级', on_delete=models.CASCADE)
    is_leaf = models.BooleanField('叶子节点', default=False)

    class Meta:
        ordering = ['id']


class Roles(BaseModel):
    name = models.CharField(max_length=16, verbose_name='角色名')

    class Meta:
        ordering = ['id']


class Users(AbstractUser):
    """每个层级有多个用户，每个用户可以是不同角色

    Args:
        AbstractUser (_type_): _description_
    """
    name = models.CharField(max_length=64, verbose_name='用户名')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='电话')
    user_role = models.ForeignKey(Roles, blank=True, null=True, related_name='role_users', on_delete=models.CASCADE)
    user_group = models.ForeignKey(Groups, blank=True, null=True, related_name='group_users', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
