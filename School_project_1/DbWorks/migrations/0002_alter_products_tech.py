# Generated by Django 5.0.5 on 2024-06-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DbWorks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='tech',
            field=models.CharField(max_length=500),
        ),
    ]
