# Generated by Django 5.0.6 on 2024-06-04 13:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "principal",
            "0005_customer_remove_room_check_in_remove_room_check_out_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="room",
            old_name="avaliable",
            new_name="available",
        ),
    ]
