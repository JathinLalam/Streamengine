# Generated by Django 4.0.1 on 2022-04-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_link',
            field=models.FileField(upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_thumbnail',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
