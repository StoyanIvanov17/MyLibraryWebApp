# Generated by Django 5.1.1 on 2024-11-20 13:22

import library.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb_home', '0002_rename_item_image_bestauthors_author_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestauthors',
            name='author_image',
            field=models.ImageField(upload_to='author_images/', validators=[library.core.validators.MaxFileSizeValidator(10485760)], verbose_name='Author Image'),
        ),
    ]
