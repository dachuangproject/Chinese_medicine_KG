# Generated by Django 3.0 on 2020-05-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Graphapp', '0005_auto_20200518_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forcom',
            name='forcom_no',
            field=models.CharField(db_column='forcom_No', max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='formulas',
            name='formulas_no',
            field=models.CharField(db_column='formulas_No', max_length=32, primary_key=True, serialize=False),
        ),
    ]