# Generated by Django 4.1 on 2022-10-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donasi", "0002_donasi_terkumpul"),
    ]

    operations = [
        migrations.AddField(
            model_name="donasi", name="urlFoto", field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="donasi",
            name="foto",
            field=models.ImageField(upload_to="upload/"),
        ),
    ]
