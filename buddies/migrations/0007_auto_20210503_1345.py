# Generated by Django 3.1.6 on 2021-05-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddies', '0006_auto_20210503_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='in_person',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='time_management',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='time_zone',
            field=models.IntegerField(null=True),
        ),
    ]