# Generated by Django 3.0.3 on 2020-08-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0012_auto_20200803_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilenames',
            name='nochoice',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='nochoice_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='nochoice_pl',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
