# Generated by Django 4.2.7 on 2023-12-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='Local',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
