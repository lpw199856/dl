# Generated by Django 2.2.8 on 2020-05-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_demo', '0005_auto_20200408_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='kind',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
