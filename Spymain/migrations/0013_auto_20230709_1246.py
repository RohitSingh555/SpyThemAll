# Generated by Django 3.2 on 2023-07-09 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spymain', '0012_alter_models_info_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogView',
            fields=[
                ('models_info_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Spymain.models_info')),
            ],
            bases=('Spymain.models_info',),
        ),
        migrations.AddField(
            model_name='models_info',
            name='Post_view',
            field=models.IntegerField(default=0),
        ),
    ]
