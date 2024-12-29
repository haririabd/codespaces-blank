# Generated by Django 5.1.4 on 2024-12-29 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diyproduct', '0003_user_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='name',
            new_name='store_name',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='name',
            new_name='store_name',
        ),
        migrations.AddField(
            model_name='store',
            name='store_code',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='store',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diyproduct.state'),
        ),
    ]
