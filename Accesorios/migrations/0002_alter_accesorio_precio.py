# Generated by Django 5.0.4 on 2024-04-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accesorios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesorio',
            name='precio',
            field=models.IntegerField(),
        ),
    ]