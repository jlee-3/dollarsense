from django.db import models
from django.utils import timezone
import uuid

# Create your models here.


class Expense(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=60)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    spotRate = models.DecimalField(
        max_digits=10, decimal_places=2, default=None, blank=True, null=True)
    currency = models.CharField(max_length=3)
    category = models.CharField(max_length=30, null=True)
    subCategory = models.CharField(max_length=60, null=True)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'expense'
        verbose_name_plural = 'expenses'

    def __str__(self):
        return self.title
