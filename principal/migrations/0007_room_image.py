# Generated by Django 5.0.6 on 2024-06-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("principal", "0006_rename_avaliable_room_available"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="image",
            field=models.ImageField(
                default="principal/room/default.jpeg", upload_to="principal/room"
            ),
        ),
    ]
