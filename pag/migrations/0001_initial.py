# Generated by Django 4.0.6 on 2022-08-22 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veri', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=150)),
                ('agora', models.DateField()),
                ('texto', models.TextField()),
                ('img', models.ImageField(upload_to='imagens/')),
            ],
        ),
    ]
