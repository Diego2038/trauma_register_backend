# Generated by Django 5.1.2 on 2025-03-11 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_records', '0006_alter_collision_trauma_register_record_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apparentintentinjury',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='apparent_intent_injury', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='burninjury',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='burn_injury', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='device',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='device', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='drugabuse',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='drug_abuse', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='firearminjury',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='firearm_injury', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='healthcarerecord',
            name='trauma_register_record_id',
            field=models.OneToOneField(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='healthcare_record', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='hospitalizationcomplication',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='hospitalization_complication', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='hospitalizationvariable',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='hospitalization_variable', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='imaging',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='imaging', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='injuryrecord',
            name='trauma_register_record_id',
            field=models.OneToOneField(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='injury_record', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='intensivecareunit',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='intensive_care_unit', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='laboratory', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='penetratinginjury',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='penetrating_injury', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='physicalexambodypartinjury',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='physical_exam_body_part_injury', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='poisoninginjury',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='poisoning_injury', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='prehospitalprocedure',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='prehospital_procedure', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='procedure', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='transportationmode',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='transportation_mode', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='traumaregistericd10',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='trauma_register_icd10', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='violenceinjury',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='violence_injury', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='vitalsign',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='vital_sign', to='medical_records.patientdata'),
        ),
        migrations.AlterField(
            model_name='vitalsigngcsqualifier',
            name='trauma_register_record_id',
            field=models.ForeignKey(blank=True, db_column='trauma_register_record_id', on_delete=django.db.models.deletion.CASCADE, related_name='vital_sign_gcs_qualifier', to='medical_records.patientdata'),
        ),
    ]
