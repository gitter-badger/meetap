# Generated by Django 3.0.3 on 2020-08-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0008_auto_20200803_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilenames',
            name='contact_explanation',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='contact_explanation_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='contact_explanation_pl',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
