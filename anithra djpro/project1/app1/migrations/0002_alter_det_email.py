# Generated by Django 4.2.7 on 2023-12-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='det',
            name='email',
            field=models.CharField(max_length=25),
        ),
    ]
