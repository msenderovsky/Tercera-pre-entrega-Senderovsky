# Generated by Django 4.2.5 on 2023-09-09 15:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0002_director_alter_película_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='nacimiento',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]