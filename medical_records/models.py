from django.db import models
from django.core.exceptions import ValidationError
from django.db import models

# HealthcareRecord Model
class HealthcareRecord(models.Model):
    trauma_register_record_id = models.OneToOneField("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", null=False, blank=True, related_name="healthcare_record")
    numero_de_historia_clinica = models.CharField(max_length=30, null=True, blank=True, default=None)
    hospital = models.CharField(max_length=300, null=True, blank=True, default=None)
    fecha_y_hora_de_llegada_del_paciente = models.DateTimeField(null=True, blank=True, default=None)
    referido = models.BooleanField(null=True, blank=True, default=None)
    policia_notificada = models.BooleanField(null=True, blank=True, default=None)
    fecha_y_hora_de_llegada_del_medico = models.DateTimeField(null=True, blank=True, default=None)
    fecha_y_hora_de_notificacion_al_medico = models.DateTimeField(null=True, blank=True, default=None)
    alerta_equipo_de_trauma = models.BooleanField(null=True, blank=True, default=None)
    nivel_de_alerta = models.CharField(max_length=30, null=True, blank=True, default=None)
    paciente_asegurado = models.BooleanField(null=True, blank=True, default=None)
    tipo_de_seguro = models.CharField(max_length=60, null=True, blank=True, default=None)
    motivo_de_consulta = models.TextField(null=True, blank=True, default=None)
    inmunizacion_contra_el_tetanos = models.CharField(max_length=60, null=True, blank=True, default=None)
    descripcion_del_examen_fisico = models.TextField(null=True, blank=True, default=None)
    mecanismo_primario = models.CharField(max_length=30, null=True, blank=True, default=None)
    numero_de_lesiones_serias = models.CharField(max_length=30, null=True, blank=True, default=None)
    descripcion_del_diagnostico = models.TextField(null=True, blank=True, default=None)
    disposicion_o_destino_del_paciente = models.CharField(max_length=50, null=True, blank=True, default=None)
    donacion_de_organos = models.CharField(max_length=30, null=True, blank=True, default=None)
    autopsia = models.CharField(max_length=30, null=True, blank=True, default=None)
    muerte_prevenible = models.CharField(max_length=30, null=True, blank=True, default=None)
    tipo_de_admision = models.CharField(max_length=30, null=True, blank=True, default=None)
    fecha_y_hora_de_la_disposicion = models.DateTimeField(null=True, blank=True, default=None)
    tiempo_en_sala_de_emergencias_horas = models.SmallIntegerField(null=True, blank=True, default=None)
    tiempo_en_sala_de_emergencias_minutos = models.SmallIntegerField(null=True, blank=True, default=None)
    numero_de_referencia_del_ed = models.CharField(max_length=30, null=True, blank=True, default=None)
    fecha_de_admision = models.DateField(null=True, blank=True, default=None)
    fecha_y_hora_de_alta = models.DateTimeField(null=True, blank=True, default=None)
    dias_de_hospitalizacion = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, default=None)
    uci_dias = models.IntegerField(null=True, blank=True, default=None)
    detalles_de_hospitalizacion = models.TextField(null=True, blank=True, default=None)
    disposicion_o_destino_del_paciente_del_hospitalizacion = models.CharField(max_length=300, null=True, blank=True, default=None)
    donacion_de_organos_del_hospitalizacion = models.CharField(max_length=30, null=True, blank=True, default=None)
    autopsia_del_hospitalizacion = models.CharField(max_length=30, null=True, blank=True, default=None)
    muerte_prevenible_del_hospitalizacion = models.CharField(max_length=30, null=True, blank=True, default=None)
    numero_de_referencia_del_hospitalizacion = models.CharField(max_length=30, null=True, blank=True, default=None)
    agencia_de_transporte = models.CharField(max_length=90, null=True, blank=True, default=None)
    origen_del_transporte = models.CharField(max_length=90, null=True, blank=True, default=None)
    numero_de_registro_del_transporte = models.CharField(max_length=30, null=True, blank=True, default=None)
    fecha_y_hora_de_notificacion_pre_hospitalaria = models.DateTimeField(null=True, blank=True, default=None)
    fecha_y_hora_de_llegada_a_la_escena = models.DateTimeField(null=True, blank=True, default=None)
    fecha_y_hora_de_salida_de_la_escena = models.DateTimeField(null=True, blank=True, default=None)
    razon_de_la_demora = models.CharField(max_length=300, null=True, blank=True, default=None)
    reporte_o_formulario_pre_hospitalario_entregado = models.BooleanField(null=True, blank=True, default=None)
    ciudad_hospital_mas_cercano_al_sitio_del_incidente = models.CharField(max_length=300, null=True, blank=True, default=None)
    tiempo_de_extricacion_horas = models.SmallIntegerField(null=True, blank=True, default=None)
    tiempo_de_extricacion_minutos = models.SmallIntegerField(null=True, blank=True, default=None)
    duracion_del_transporte_horas = models.SmallIntegerField(null=True, blank=True, default=None)
    duracion_del_transporte_minutos = models.SmallIntegerField(null=True, blank=True, default=None)
    procedimiento_realizado = models.TextField(null=True, blank=True, default=None)
    frecuencia_cardiaca_en_la_escena = models.SmallIntegerField(null=True, blank=True, default=None)
    presion_arterial_sistolica_en_la_escena = models.SmallIntegerField(null=True, blank=True, default=None)
    presion_arterial_diastolica_en_la_escena = models.SmallIntegerField(null=True, blank=True, default=None)
    frecuencia_respiratoria_en_la_escena = models.SmallIntegerField(null=True, blank=True, default=None)
    calificador_de_frecuencia_respiratoria_en_la_escena = models.CharField(max_length=60, null=True, blank=True, default=None)
    temperatura_en_la_escena_celsius = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, default=None)
    saturacion_de_o2_en_la_escena = models.SmallIntegerField(null=True, blank=True, default=None)
    frecuencia_cardiaca_durante_el_transporte = models.SmallIntegerField(null=True, blank=True, default=None)
    presion_arterial_sistolica_de_transporte = models.SmallIntegerField(null=True, blank=True, default=None)
    presion_diastolica_durante_el_transporte = models.SmallIntegerField(null=True, blank=True, default=None)
    frecuencia_respiratoria_durante_el_transporte = models.SmallIntegerField(null=True, blank=True, default=None)
    calificador_de_frecuencia_respiratoria_durante_el_transporte = models.CharField(max_length=60, null=True, blank=True, default=None)
    temperatura_durante_el_transporte_celsius = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, default=None)
    saturacion_de_o2_durante_el_transporte = models.SmallIntegerField(null=True, blank=True, default=None)
    perdida_de_conciencia = models.SmallIntegerField(null=True, blank=True, default=None)
    duracion_de_perdida_de_conciencia = models.TimeField(null=True, blank=True, default=None)
    gcs_ocular = models.SmallIntegerField(null=True, blank=True, default=None)
    gcs_verbal = models.SmallIntegerField(null=True, blank=True, default=None)
    gcs_motora = models.SmallIntegerField(null=True, blank=True, default=None)
    gcs_total = models.SmallIntegerField(null=True, blank=True, default=None)
    sangre_l = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True, default=None)
    coloides_l = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True, default=None)
    cristaloides_l = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True, default=None)
    hallazgos_clinicos_texto = models.TextField(null=True, blank=True, default=None)
    fecha_y_hora_de_envio_de_contra_referencia = models.DateTimeField(null=True, blank=True, default=None)
    fecha_de_alta_de_contrar_referencia = models.DateTimeField(null=True, blank=True, default=None)
    hallazgos_clinicos_existencia = models.BooleanField(null=True, blank=True, default=None)
    servicio_que_atendio = models.CharField(max_length=90, null=True, blank=True, default=None)
    paciente_admitido = models.BooleanField(null=True, blank=True, default=None)
    hospital_que_recibe = models.CharField(max_length=90, null=True, blank=True, default=None)
    otro_servicio = models.CharField(max_length=90, null=True, blank=True, default=None)
    servicio_que_recibe = models.CharField(max_length=90, null=True, blank=True, default=None)
    recomendaciones = models.TextField(null=True, blank=True, default=None)
    numero_de_referencia_de_referencias_salientes = models.CharField(max_length=30, null=True, blank=True, default=None)
    fecha_de_envio_de_referencia = models.DateTimeField(null=True, blank=True, default=None)
    fecha_de_referencia = models.DateField(null=True, blank=True, default=None)
    razon_de_la_referencia = models.TextField(null=True, blank=True, default=None)
    medico_que_refiere = models.CharField(max_length=90, null=True, blank=True, default=None)
    estado_de_referencia = models.CharField(max_length=30, null=True, blank=True, default=None)
    fecha_de_aceptacion_de_referencia = models.DateField(null=True, blank=True, default=None)
    iss = models.SmallIntegerField(null=True, blank=True, default=None)
    kts = models.SmallIntegerField(null=True, blank=True, default=None)
    rts = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True, default=None)
    abdomen = models.SmallIntegerField(null=True, blank=True, default=None)
    torax = models.SmallIntegerField(null=True, blank=True, default=None)
    externo = models.SmallIntegerField(null=True, blank=True, default=None)
    extremidades = models.SmallIntegerField(null=True, blank=True, default=None)
    cara = models.SmallIntegerField(null=True, blank=True, default=None)
    cabeza = models.SmallIntegerField(null=True, blank=True, default=None)
    triss_contuso = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True, default=None)
    triss_penetrante = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True, default=None)

    class Meta:
        db_table = 'healthcare_record'

    def __str__(self):
        return f"HealthcareRecord {self.trauma_register_record_id}"

# InjuryRecord Model
class InjuryRecord(models.Model):
    trauma_register_record_id = models.OneToOneField("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", null=False, blank=True, related_name="injury_record")
    consumo_de_alcohol = models.CharField(max_length=30, null=True, blank=True, default=None)
    valor_de_alcoholemia = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=None)
    unidad_de_alcohol = models.CharField(max_length=60, null=True, blank=True, default=None)
    otra_sustancia_de_abuso = models.CharField(max_length=600, null=True, blank=True, default=None)
    direccion_nombre_del_lugar = models.CharField(max_length=300, null=True, blank=True, default=None)
    ciudad_de_evento_de_la_lesion = models.CharField(max_length=60, null=True, blank=True, default=None)
    condado_de_lesiones = models.CharField(max_length=60, null=True, blank=True, default=None)
    estado_provincia_de_lesiones = models.CharField(max_length=60, null=True, blank=True, default=None)
    pais_de_lesiones = models.CharField(max_length=60, null=True, blank=True, default=None)
    codigo_postal_de_lesiones = models.CharField(max_length=60, null=True, blank=True, default=None)
    fecha_y_hora_del_evento = models.DateTimeField(null=True, blank=True, default=None)
    accidente_de_trafico = models.BooleanField(null=True, blank=True, default=None)
    tipo_de_vehiculo = models.CharField(max_length=90, null=True, blank=True, default=None)
    ocupante = models.CharField(max_length=60, null=True, blank=True, default=None)
    velocidad_de_colision = models.CharField(max_length=60, null=True, blank=True, default=None)
    scq = models.SmallIntegerField(null=True, blank=True, default=None)
    caida = models.BooleanField(null=True, blank=True, default=None)
    altura_metros = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    tipo_de_superficie = models.CharField(max_length=30, null=True, blank=True, default=None)

    class Meta:
        db_table = 'injury_record'

    def __str__(self):
        return f"InjuryRecord {self.trauma_register_record_id}"

# Collision Model
class Collision(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="collision", blank=True, null=False)
    tipo_de_colision = models.CharField(max_length=300, null=True, blank=True, default=None)

    class Meta:
        db_table = 'collision'

    def __str__(self):
        return f"Collision {self.trauma_register_record_id}"

# DrugAbuse Model
class DrugAbuse(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="drug_abuse", blank=True, null=False)
    tipo_de_droga = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'drug_abuse'

    def __str__(self):
        return f"DrugAbuse {self.trauma_register_record_id}"

# VitalSignGcsQualifier Model
class VitalSignGcsQualifier(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="vital_sign_gcs_qualifier", blank=True, null=False)
    calificador_gcs = models.CharField(max_length=300, null=True, blank=True, default=None)

    class Meta:
        db_table = 'vital_sign_gcs_qualifier'

    def __str__(self):
        return f"VitalSignGcsQualifier {self.trauma_register_record_id}"

# HospitalizationVariable Model
class HospitalizationVariable(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="hospitalization_variable", blank=True, null=False)
    tipo_de_variable = models.CharField(max_length=90, null=True, blank=True, default=None)
    valor_de_la_variable = models.CharField(max_length=30, null=True, blank=True, default=None)
    fecha_y_hora_de_la_variable = models.DateTimeField(null=True, blank=True, default=None)
    localizacion_de_variable = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'hospitalization_variable'

    def __str__(self):
        return f"HospitalizationVariable {self.trauma_register_record_id}"

# HospitalizationComplication Model
class HospitalizationComplication(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="hospitalization_complication", blank=True, null=False)
    tipo_de_complicacion = models.CharField(max_length=300, null=True, blank=True, default=None)
    fecha_y_hora_de_complicacion = models.DateTimeField(null=True, blank=True, default=None)
    lugar_de_complicacion = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'hospitalization_complication'

    def __str__(self):
        return f"HospitalizationComplication {self.trauma_register_record_id}"

# TraumaRegisterIcd10 Model
class TraumaRegisterIcd10(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="trauma_register_icd10", blank=True, null=False)
    descripcion = models.TextField(null=True, blank=True, default=None)
    mecanismo_icd = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'trauma_register_icd10'

    def __str__(self):
        return f"TraumaRegisterIcd10 {self.trauma_register_record_id}"

# IntensiveCareUnit Model
class IntensiveCareUnit(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="intensive_care_unit", blank=True, null=False)
    tipo = models.CharField(max_length=90, null=True, blank=True, default=None)
    fecha_y_hora_de_inicio = models.DateTimeField(null=True, blank=True, default=None)
    fecha_y_hora_de_termino = models.DateTimeField(null=True, blank=True, default=None)
    lugar = models.CharField(max_length=90, null=True, blank=True, default=None)
    icu_days = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, default=None)

    class Meta:
        db_table = 'intensive_care_unit'

    def __str__(self):
        return f"IntensiveCareUnit {self.trauma_register_record_id}"

# Imaging Model
class Imaging(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="imaging", blank=True, null=False)
    tipo_de_imagen = models.CharField(max_length=90, null=True, blank=True, default=None)
    parte_del_cuerpo = models.CharField(max_length=90, null=True, blank=True, default=None)
    opcion = models.BooleanField(null=True, blank=True, default=None)
    descripcion = models.TextField(null=True, blank=True, default=None)

    class Meta:
        db_table = 'imaging'

    def __str__(self):
        return f"Imaging {self.trauma_register_record_id}"

# ApparentIntentInjury Model
class ApparentIntentInjury(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="apparent_intent_injury", blank=True, null=False)
    intencion_aparente = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'apparent_intent_injury'

    def __str__(self):
        return f"ApparentIntentInjury {self.trauma_register_record_id}"

# BurnInjury Model
class BurnInjury(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="burn_injury", blank=True, null=False)
    tipo_de_quemadura = models.CharField(max_length=90, null=True, blank=True, default=None)
    grado_de_quemadura = models.CharField(max_length=30, null=True, blank=True, default=None)

    class Meta:
        db_table = 'burn_injury'

    def __str__(self):
        return f"BurnInjury {self.trauma_register_record_id}"

# FirearmInjury Model
class FirearmInjury(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="firearm_injury", blank=True, null=False)
    tipo_de_arma_de_fuego = models.CharField(max_length=60, null=True, blank=True, default=None)

    class Meta:
        db_table = 'firearm_injury'

    def __str__(self):
        return f"FirearmInjury {self.trauma_register_record_id}"

# PenetratingInjury Model
class PenetratingInjury(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="penetrating_injury", blank=True, null=False)
    tipo_de_lesion_penetrante = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'penetrating_injury'

    def __str__(self):
        return f"PenetratingInjury {self.trauma_register_record_id}"

# PoisoningInjury Model
class PoisoningInjury(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="poisoning_injury", blank=True, null=False)
    tipo_de_envenenamiento = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'poisoning_injury'

    def __str__(self):
        return f"PoisoningInjury {self.trauma_register_record_id}"

# ViolenceInjury Model
class ViolenceInjury(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="violence_injury", blank=True, null=False)
    tipo_de_violencia = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'violence_injury'

    def __str__(self):
        return f"ViolenceInjury {self.trauma_register_record_id}"

# Device Model
class Device(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="device", blank=True, null=False)
    tipo_de_dispositivo = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'device'

    def __str__(self):
        return f"Device {self.trauma_register_record_id}"

# Laboratory Model
class Laboratory(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="laboratory", blank=True, null=False)
    resultado_de_laboratorio = models.CharField(max_length=90, null=True, blank=True, default=None)
    fecha_y_hora_de_laboratorio = models.DateTimeField(null=True, blank=True, default=None)
    nombre_del_laboratorio = models.CharField(max_length=90, null=True, blank=True, default=None)
    nombre_de_la_unidad_de_laboratorio = models.CharField(max_length=30, null=True, blank=True, default=None)

    class Meta:
        db_table = 'laboratory'

    def __str__(self):
        return f"Laboratory {self.trauma_register_record_id}"

# PhysicalExamBodyPartInjury Model
class PhysicalExamBodyPartInjury(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="physical_exam_body_part_injury", blank=True, null=False)
    parte_del_cuerpo = models.CharField(max_length=90, null=True, blank=True, default=None)
    tipo_de_lesion = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'physical_exam_body_part_injury'

# Procedure Model
class Procedure(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="procedure", blank=True, null=False)
    procedimiento_realizado = models.CharField(max_length=90, null=True, blank=True, default=None)
    fecha_y_hora_de_inicio = models.DateTimeField(null=True, blank=True, default=None)
    fecha_y_hora_de_termino = models.DateTimeField(null=True, blank=True, default=None)
    lugar = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'procedure'

    def __str__(self):
        return f"Procedure {self.trauma_register_record_id}"

# PrehospitalProcedure Model
class PrehospitalProcedure(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="prehospital_procedure", blank=True, null=False)
    procedimiento_realizado = models.CharField(max_length=300, null=True, blank=True, default=None)

    class Meta:
        db_table = 'prehospital_procedure'

    def __str__(self):
        return f"PrehospitalProcedure {self.trauma_register_record_id}"

# TransportationMode Model
class TransportationMode(models.Model):
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="transportation_mode", blank=True, null=False)
    modo_de_transporte = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'transportation_mode'

    def __str__(self):
        return f"TransportationMode {self.trauma_register_record_id}"

# VitalSign Model
class VitalSign(models.Model):
    record_id = models.BigIntegerField(primary_key=True)
    trauma_register_record_id = models.ForeignKey("PatientData", on_delete=models.CASCADE, db_column="trauma_register_record_id", related_name="vital_sign", blank=True, null=False)
    fecha_y_hora_de_signos_vitales = models.DateTimeField(null=True, blank=True, default=None)
    signos_de_vida = models.BooleanField(null=True, blank=True, default=None)
    frecuencia_cardiaca = models.SmallIntegerField(null=True, blank=True, default=None)
    presion_arterial_sistolica = models.SmallIntegerField(null=True, blank=True, default=None)
    presion_arterial_diastolica = models.SmallIntegerField(null=True, blank=True, default=None)
    frecuencia_respiratoria = models.SmallIntegerField(null=True, blank=True, default=None)
    calificador_de_frecuencia_respiratoria = models.CharField(max_length=60, null=True, blank=True, default=None)
    temperatura_celsius = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, default=None)
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    altura_metros = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=None)
    saturacion_de_oxigeno = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    perdida_de_conciencia = models.CharField(max_length=30, null=True, blank=True, default=None)
    duracion_de_perdida_de_conciencia = models.TimeField(null=True, blank=True, default=None)
    gcs_motora = models.SmallIntegerField(null=True, blank=True, default=None)
    gcs_ocular = models.SmallIntegerField(null=True, blank=True, default=None)
    gcs_verbal = models.SmallIntegerField(null=True, blank=True, default=None)
    gcs_total = models.SmallIntegerField(null=True, blank=True, default=None)
    avup = models.CharField(max_length=60, null=True, blank=True, default=None)

    class Meta:
        db_table = 'vital_sign'

    def __str__(self):
        return f"VitalSign {self.record_id} - {self.trauma_register_record_id}"

# PatientData Model
class PatientData(models.Model):
    trauma_register_record_id = models.BigIntegerField(primary_key=True)
    direccion_linea_1 = models.CharField(max_length=300, null=True, blank=True, default=None)
    direccion_linea_2 = models.CharField(max_length=300, null=True, blank=True, default=None)
    ciudad = models.CharField(max_length=300, null=True, blank=True, default=None)
    canton_municipio = models.CharField(max_length=90, null=True, blank=True, default=None)
    provincia_estado = models.CharField(max_length=90, null=True, blank=True, default=None)
    codigo_postal = models.CharField(max_length=90, null=True, blank=True, default=None)
    pais = models.CharField(max_length=90, null=True, blank=True, default=None)
    edad = models.IntegerField(null=True, blank=True, default=None)
    unidad_de_edad = models.CharField(max_length=9, null=True, blank=True, default=None)
    genero = models.CharField(max_length=30, null=True, blank=True, default=None)
    fecha_de_nacimiento = models.DateField(null=True, blank=True, default=None)
    ocupacion = models.CharField(max_length=300, null=True, blank=True, default=None)
    estado_civil = models.CharField(max_length=30, null=True, blank=True, default=None)
    nacionalidad = models.CharField(max_length=90, null=True, blank=True, default=None)
    grupo_etnico = models.CharField(max_length=60, null=True, blank=True, default=None)
    otro_grupo_etnico = models.CharField(max_length=60, null=True, blank=True, default=None)
    num_doc_de_identificacion = models.CharField(max_length=90, null=True, blank=True, default=None)

    class Meta:
        db_table = 'patient_data'

    def __str__(self):
        return f"PatientData {self.trauma_register_record_id}"
