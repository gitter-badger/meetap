# Generated by Django 3.0.3 on 2020-08-03 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0006_auto_20200803_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_adult',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Małoletni'), (1, 'Niepełnoletni'), (2, 'Pełnoletni')], null=True),
        ),
    ]
