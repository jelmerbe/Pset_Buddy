# Generated by Django 3.1.6 on 2021-05-05 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddies', '0015_auto_20210505_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='zoom_preference',
            field=models.IntegerField(null=True),
        ),
    ]