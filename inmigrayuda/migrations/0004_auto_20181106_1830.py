# Generated by Django 2.1.2 on 2018-11-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmigrayuda', '0003_auto_20181106_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='fuente',
            field=models.CharField(max_length=100),
        ),
    ]
