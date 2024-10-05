from django.db import models
from django.utils.timezone import now
from datetime import datetime
import django

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    status = models.SmallIntegerField(default=1)
    deleted = models.BooleanField(default=0)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'items'
        verbose_name_plural = 'items'
