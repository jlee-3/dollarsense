# Generated by Django 4.1.7 on 2023-03-25 09:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=3)),
                ('category', models.CharField(max_length=30)),
                ('createdAt', models.DateField()),
                ('updatedAt', models.DateField()),
            ],
            options={
                'verbose_name': 'expense',
                'verbose_name_plural': 'expenses',
            },
        ),
    ]
