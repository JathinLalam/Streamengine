# Generated by Django 4.0.4 on 2022-05-24 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0002_alter_video_video_link_alter_video_video_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_link',
            field=models.URLField(max_length=1000),
        ),
    ]