# Generated by Django 3.0.3 on 2020-08-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0002_profilenames'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilenames',
            name='active',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='active_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='active_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='dominant',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='dominant_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='dominant_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='neutral',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='neutral_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='neutral_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='passive',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='passive_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='passive_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='submissive',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='submissive_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilenames',
            name='submissive_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_friend_events',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_friend_events_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_friend_events_pl',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_inv_status_me',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_inv_status_me_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_inv_status_me_pl',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_inv_status_others',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_inv_status_others_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_inv_status_others_pl',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_invitations',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_invitations_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_invitations_pl',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_join_request',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_join_request_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profilenames',
            name='sendme_join_request_pl',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
