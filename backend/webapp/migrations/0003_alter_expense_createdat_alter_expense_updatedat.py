# Generated by Django 4.1.7 on 2023-03-26 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_name_expense_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='createdAt',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='expense',
            name='updatedAt',
            field=models.DateTimeField(),
        ),
    ]
