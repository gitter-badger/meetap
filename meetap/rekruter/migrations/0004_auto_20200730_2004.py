# Generated by Django 3.0.3 on 2020-07-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0003_auto_20200730_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
    ]