# Generated by Django 2.1.2 on 2018-11-06 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmigrayuda', '0002_noticias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='fuente',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
