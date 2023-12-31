# Generated by Django 4.2.5 on 2023-11-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(default=None, null=True, verbose_name='latitude do local')),
                ('longitude', models.FloatField(default=None, null=True, verbose_name='longitude do local')),
                ('status', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]
