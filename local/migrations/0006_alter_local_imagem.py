# Generated by Django 4.2.5 on 2023-12-05 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0005_alter_local_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='imagem',
            field=models.ImageField(null=True, upload_to='media/imagens_de_locais/'),
        ),
    ]
