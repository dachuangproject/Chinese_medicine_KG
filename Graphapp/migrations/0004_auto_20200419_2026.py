# Generated by Django 3.0 on 2020-04-19 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Graphapp', '0003_auto_20200419_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='fangyi',
            field=models.CharField(blank=True, max_length=511, null=True),
        ),
    ]
