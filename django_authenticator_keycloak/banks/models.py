"""Modelos do Django"""
from django.db import models


class Banks(models.Model):
    ispb = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)
    fullName = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = "tb_banks"
