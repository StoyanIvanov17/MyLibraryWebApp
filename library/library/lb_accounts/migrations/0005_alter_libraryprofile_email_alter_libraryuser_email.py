# Generated by Django 5.1.1 on 2024-11-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb_accounts', '0004_alter_libraryprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryprofile',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='libraryuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=30, unique=True),
        ),
    ]
