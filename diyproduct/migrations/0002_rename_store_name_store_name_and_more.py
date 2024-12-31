# Generated by Django 5.1.4 on 2024-12-29 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diyproduct", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="store",
            old_name="store_name",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="purchaseorder",
            name="store_name",
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="name",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="diyproduct.store",
            ),
            preserve_default=False,
        ),
    ]