# Generated by Django 4.0.6 on 2022-08-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='veri',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='agora',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='nome',
            field=models.CharField(max_length=150),
        ),
    ]
