# Generated by Django 5.1.2 on 2025-07-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_records', '0007_alter_apparentintentinjury_trauma_register_record_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalsign',
            name='record_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]
