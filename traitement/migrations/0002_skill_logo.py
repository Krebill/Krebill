# Generated by Django 4.0.1 on 2022-02-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traitement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
