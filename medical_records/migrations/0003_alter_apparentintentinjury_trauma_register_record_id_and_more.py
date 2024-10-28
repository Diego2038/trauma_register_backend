# Generated by Django 5.1.2 on 2024-10-28 01:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medical_records", "0002_alter_patientdata_fecha_de_nacimiento_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apparentintentinjury",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="burninjury",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="collision",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="drugabuse",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="firearminjury",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="healthcarerecord",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="hospitalizationcomplication",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="hospitalizationvariable",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="imaging",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="injuryrecord",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="intensivecareunit",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="laboratory",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="penetratinginjury",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="physicalexambodypartinjury",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="poisoninginjury",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="prehospitalprocedure",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="procedure",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="transportationmode",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="traumaregistericd10",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="violenceinjury",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="vitalsign",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
        migrations.AlterField(
            model_name="vitalsigngcsqualifier",
            name="trauma_register_record_id",
            field=models.ForeignKey(
                db_column="trauma_register_record_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_records.patientdata",
            ),
        ),
    ]
