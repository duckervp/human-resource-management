# Generated by Django 3.2.3 on 2021-05-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='card_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
