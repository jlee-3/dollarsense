# Generated by Django 4.1.7 on 2023-04-26 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_rename_title_expense_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.CharField(max_length=60),
        ),
    ]
