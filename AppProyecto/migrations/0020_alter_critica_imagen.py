# Generated by Django 4.2.5 on 2023-10-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0019_critica_fecha_critica_imagen_critica_subtitulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critica',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]