# Generated by Django 2.0.9 on 2018-11-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181130_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='height_field',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='width_field',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
