# Generated by Django 3.0.3 on 2020-04-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_demo', '0004_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='result',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='img',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]