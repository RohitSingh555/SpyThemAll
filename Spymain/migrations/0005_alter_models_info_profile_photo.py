# Generated by Django 4.2.2 on 2023-07-01 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Spymain', '0004_alter_model_assets_animelover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models_info',
            name='profile_photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads/profilephoto'),
            preserve_default=False,
        ),
    ]
