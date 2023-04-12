from django.db import models
import uuid

# Create your models here.


class Expense(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    spotRate = models.DecimalField(
        max_digits=10, decimal_places=2, default=None, blank=True, null=True)
    currency = models.CharField(max_length=3)
    category = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'expense'
        verbose_name_plural = 'expenses'

    def __str__(self):
        return self.title
