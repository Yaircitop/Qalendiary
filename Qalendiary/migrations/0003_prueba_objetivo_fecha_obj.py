# Generated by Django 4.1.2 on 2022-11-11 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qalendiary', '0002_objetivo_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('objetivo', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='objetivo',
            name='fecha_obj',
            field=models.DateField(auto_now=True),
        ),
    ]