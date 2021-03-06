# Generated by Django 3.0.3 on 2020-08-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0003_auto_20200802_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilenames',
            name='adult_settings',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='adult_settings_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='adult_settings_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='contact_settings',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='contact_settings_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='contact_settings_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='general_settings',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='general_settings_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='general_settings_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='mailing_settings',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='mailing_settings_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='mailing_settings_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='profile_settings',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='profile_settings_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='profile_settings_pl',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
