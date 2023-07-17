# Generated by Django 4.2.2 on 2023-07-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spymain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='models_info',
            name='hobbies',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='models_info',
            name='industry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='models_info',
            name='job',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='models_info',
            name='preffered_type_according_to_us',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='models_info',
            name='secret',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='models_info',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='animelover',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='asshole',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='aunty',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='bigass',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='bigboobs',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='classy',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='creep',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='fat',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='gamer',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='goddess',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='hot',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='milf',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='movielover',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='naughty',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='nerdy',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='petite',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='playgirl',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='pretty',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='reader',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='redhead',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='sexy',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='summer_body',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='teen',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='model_assets',
            name='topper',
            field=models.BooleanField(blank=True, choices=[(1, 'No'), (2, 'Yes')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='age',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='approx_followers',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='bust',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='height_feet',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='height_inches',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='hip',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='school',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='waist',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='models_info',
            name='weight',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
