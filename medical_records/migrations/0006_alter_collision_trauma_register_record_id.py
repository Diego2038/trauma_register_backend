# Generated by Django 5.1.2 on 2025-03-10 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_records', '0005_alter_apparentintentinjury_trauma_register_record_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collision',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='collision', to='medical_records.patientdata'),
        ),
    ]
