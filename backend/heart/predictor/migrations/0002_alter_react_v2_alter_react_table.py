# Generated by Django 5.1.5 on 2025-01-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='react',
            name='v2',
            field=models.TextField(),
        ),
        migrations.AlterModelTable(
            name='react',
            table='predictor_react',
        ),
    ]
