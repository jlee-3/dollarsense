from django.db import models

# Create your models here.


class Expense(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    category = models.CharField(max_length=30)
    createdAt = models.DateField()
    updatedAt = models.DateField()

    class Meta:
        verbose_name = 'expense'
        verbose_name_plural = 'expenses'

    def __str__(self):
        return self.name
