# Generated by Django 5.1.1 on 2024-11-13 12:17

import django.db.models.deletion
import django.utils.timezone
import library.core.validators
import library.lb_accounts.managers
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('lb_events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email address already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('library_card_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', library.lb_accounts.managers.LibraryUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LibraryProfile',
            fields=[
                ('email', models.EmailField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('verification_token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_photos/', validators=[library.core.validators.MaxFileSizeValidator(10485760)], verbose_name='Profile Picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('saved_events', models.ManyToManyField(blank=True, related_name='library_profile_saved_events', to='lb_events.event')),
            ],
        ),
    ]
