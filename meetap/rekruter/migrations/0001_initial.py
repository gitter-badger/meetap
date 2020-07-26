# Generated by Django 3.0.3 on 2020-07-26 16:45

from django.db import migrations, models
import rekruter.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_translator', models.BooleanField(default=False, verbose_name='translator')),
                ('is_hotel', models.BooleanField(default=False, verbose_name='hotel')),
                ('role_council', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'User'), (2, 'Council'), (3, 'Council Admin'), (4, 'Superuser')], default=1, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('quarter', models.CharField(blank=True, max_length=2, verbose_name='quarter')),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'other'), (1, 'male'), (2, 'female')], null=True)),
                ('citizenship', models.CharField(blank=True, max_length=40, verbose_name='citizenship')),
                ('dowod', models.CharField(blank=True, max_length=20, verbose_name='dowod')),
                ('passport', models.CharField(blank=True, max_length=20, verbose_name='passport')),
                ('telephone', models.CharField(blank=True, max_length=20, verbose_name='telephone')),
                ('street', models.CharField(blank=True, max_length=30, verbose_name='street')),
                ('building_no', models.CharField(blank=True, max_length=15, verbose_name='building_no')),
                ('local_no', models.CharField(blank=True, max_length=10, verbose_name='local_no')),
                ('postcode', models.CharField(blank=True, max_length=7, verbose_name='postcode')),
                ('city', models.CharField(blank=True, max_length=25, verbose_name='city')),
                ('album', models.CharField(blank=True, max_length=25, verbose_name='album')),
                ('language', models.CharField(blank=True, max_length=2, verbose_name='album')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', rekruter.managers.UserManager()),
            ],
        ),
    ]
