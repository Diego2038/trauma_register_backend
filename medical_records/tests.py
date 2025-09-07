from django.test import TestCase
from medical_records.models import *
from medical_records.serializers import PatientDataSerializer


class PatientDataSerializerCreateTest(TestCase):

  def setUp(self):
    # Datos base para un paciente
    self.patient_data = {
      "trauma_register_record_id": 777,
      "healthcare_record": {
          "numero_de_historia_clinica": "7754",
          "hospital": "Hospital almendras",
          "fecha_y_hora_de_llegada_del_paciente": "2014-04-09T19:26:00Z",
          "referido": False,
          "policia_notificada": False,
          "fecha_y_hora_de_llegada_del_medico": "2014-04-09T19:26:00Z",
          "fecha_y_hora_de_notificacion_al_medico": "2014-04-09T19:26:00Z",
          "alerta_equipo_de_trauma": True,
          "nivel_de_alerta": "Media/Subcrítica",
          "paciente_asegurado": False,
          "tipo_de_seguro": None,
          "motivo_de_consulta": "\"DOLOR EN LA PIERNA IZQUIERDA\"",
          "inmunizacion_contra_el_tetanos": "No",
          "descripcion_del_examen_fisico": "dolor a la palpacion y limitacion en cadera izquierda.",
          "mecanismo_primario": "Contuso",
          "numero_de_lesiones_serias": "1 Lesión Seria",
          "descripcion_del_diagnostico": "fractura de femur.",
          "disposicion_o_destino_del_paciente": "Internado",
          "donacion_de_organos": "No",
          "autopsia": "No",
          "muerte_prevenible": "No aplica",
          "tipo_de_admision": "Urgencia",
          "fecha_y_hora_de_la_disposicion": "2014-04-14T21:56:00Z",
          "tiempo_en_sala_de_emergencias_horas": 122,
          "tiempo_en_sala_de_emergencias_minutos": 50,
          "numero_de_referencia_del_ed": None,
          "fecha_de_admision": "2014-04-09",
          "fecha_y_hora_de_alta": "2014-04-14T04:56:00Z",
          "dias_de_hospitalizacion": "5.00",
          "uci_dias": 0,
          "detalles_de_hospitalizacion": "procedimiento quirurgico: hemiartoplastia de cadera izquierda: 11 abr 2014: procedimiento sin complicaciones.\nse da salida a paciente con recomendaciones.",
          "disposicion_o_destino_del_paciente_del_hospitalizacion": "Domicilio",
          "donacion_de_organos_del_hospitalizacion": "No",
          "autopsia_del_hospitalizacion": "No",
          "muerte_prevenible_del_hospitalizacion": "No aplica",
          "numero_de_referencia_del_hospitalizacion": None,
          "agencia_de_transporte": "no especificado",
          "origen_del_transporte": "no especificado",
          "numero_de_registro_del_transporte": "ninguno",
          "fecha_y_hora_de_notificacion_pre_hospitalaria": None,
          "fecha_y_hora_de_llegada_a_la_escena": None,
          "fecha_y_hora_de_salida_de_la_escena": None,
          "razon_de_la_demora": None,
          "reporte_o_formulario_pre_hospitalario_entregado": None,
          "ciudad_hospital_mas_cercano_al_sitio_del_incidente": None,
          "tiempo_de_extricacion_horas": 2,
          "tiempo_de_extricacion_minutos": 0,
          "duracion_del_transporte_horas": None,
          "duracion_del_transporte_minutos": None,
          "procedimiento_realizado": None,
          "frecuencia_cardiaca_en_la_escena": None,
          "presion_arterial_sistolica_en_la_escena": None,
          "presion_arterial_diastolica_en_la_escena": None,
          "frecuencia_respiratoria_en_la_escena": None,
          "calificador_de_frecuencia_respiratoria_en_la_escena": None,
          "temperatura_en_la_escena_celsius": "0.00",
          "saturacion_de_o2_en_la_escena": None,
          "frecuencia_cardiaca_durante_el_transporte": None,
          "presion_arterial_sistolica_de_transporte": None,
          "presion_diastolica_durante_el_transporte": None,
          "frecuencia_respiratoria_durante_el_transporte": None,
          "calificador_de_frecuencia_respiratoria_durante_el_transporte": "Frecuencia Respiratoria Sin Asistencia",
          "temperatura_durante_el_transporte_celsius": "0.00",
          "saturacion_de_o2_durante_el_transporte": None,
          "perdida_de_conciencia": None,
          "duracion_de_perdida_de_conciencia": None,
          "gcs_ocular": None,
          "gcs_verbal": None,
          "gcs_motora": None,
          "gcs_total": None,
          "sangre_l": "0.000",
          "coloides_l": "0.000",
          "cristaloides_l": "0.000",
          "hallazgos_clinicos_texto": None,
          "fecha_y_hora_de_envio_de_contra_referencia": None,
          "fecha_de_alta_de_contrar_referencia": None,
          "hallazgos_clinicos_existencia": None,
          "servicio_que_atendio": None,
          "paciente_admitido": None,
          "hospital_que_recibe": None,
          "otro_servicio": None,
          "servicio_que_recibe": None,
          "recomendaciones": None,
          "numero_de_referencia_de_referencias_salientes": None,
          "fecha_de_envio_de_referencia": None,
          "fecha_de_referencia": None,
          "razon_de_la_referencia": None,
          "medico_que_refiere": None,
          "estado_de_referencia": None,
          "fecha_de_aceptacion_de_referencia": None,
          "iss": 9,
          "kts": None,
          "rts": "7.8408",
          "abdomen": None,
          "torax": None,
          "externo": None,
          "extremidades": 3,
          "cara": None,
          "cabeza": None,
          "triss_contuso": None,
          "triss_penetrante": None
      },
      "injury_record": {
          "consumo_de_alcohol": "No",
          "valor_de_alcoholemia": None,
          "unidad_de_alcohol": "mg/dl",
          "otra_sustancia_de_abuso": "NINGUNA",
          "direccion_nombre_del_lugar": None,
          "ciudad_de_evento_de_la_lesion": "CALI",
          "condado_de_lesiones": None,
          "estado_provincia_de_lesiones": "VALLE DEL CAUCA",
          "pais_de_lesiones": "Colombia",
          "codigo_postal_de_lesiones": None,
          "fecha_y_hora_del_evento": "2014-12-18T04:56:00Z",
          "accidente_de_trafico": False,
          "tipo_de_vehiculo": None,
          "ocupante": None,
          "velocidad_de_colision": None,
          "scq": None,
          "caida": False,
          "altura_metros": None,
          "tipo_de_superficie": None
      },
      "collision": [
          {
              "tipo_de_colision": "Peatón vs. vehículo de dos o tres ruedas"
          },
          {
              "tipo_de_colision": "Peatón vs. vehículo de dos o tres ruedas otro"
          }
      ],
      "drug_abuse": [
          {
              "tipo_de_droga": "J. NO ESPECIFICADO"
          },
          {
              "tipo_de_droga": "e. Marihuana"
          }
      ],
      "vital_sign_gcs_qualifier": [
          {
              "calificador_gcs": "Paciente Sedado Químicamente O Paralizado"
          },
          {
              "calificador_gcs": "Paciente Sedado"
          }
      ],
      "hospitalization_variable": [
          {
              "tipo_de_variable": "FR.-Frecuencia Respiratoria",
              "valor_de_la_variable": "28",
              "fecha_y_hora_de_la_variable": "2012-01-06T08:29:00Z",
              "localizacion_de_variable": "Hospitalizacion-Piso"
          },
          {
              "tipo_de_variable": "FR.-Frecuencia Cardiaca",
              "valor_de_la_variable": "45",
              "fecha_y_hora_de_la_variable": "2012-01-06T08:29:00Z",
              "localizacion_de_variable": "Hospitalizacion"
          }
      ],
      "hospitalization_complication": [
          {
              "tipo_de_complicacion": "Neumonía bacteriana, no clasificada en otra parte",
              "fecha_y_hora_de_complicacion": "2012-02-07T04:56:00Z",
              "lugar_de_complicacion": "Hospitalizacion-Piso"
          },
          {
              "tipo_de_complicacion": "Neumonía bacteriana",
              "fecha_y_hora_de_complicacion": "2012-02-07T04:56:00Z",
              "lugar_de_complicacion": "Hospitalizacion"
          }
      ],
      "trauma_register_icd10": [
          {
              "descripcion": "Otras convulsiones y las no especificadas",
              "mecanismo_icd": "Co-morbidities"
          },
          {
              "descripcion": "Otras convulsiones",
              "mecanismo_icd": "Co-mor"
          }
      ],
      "intensive_care_unit": [
          {
              "tipo": "Unidad de cuidados intensivos (UCI)",
              "fecha_y_hora_de_inicio": "2012-01-21T04:56:00Z",
              "fecha_y_hora_de_termino": "2012-01-27T04:56:00Z",
              "lugar": "UCI Neuroquirúrgica",
              "icu_days": "6.00"
          },
          {
              "tipo": "Unidad de cuidados ",
              "fecha_y_hora_de_inicio": "2012-01-21T04:56:00Z",
              "fecha_y_hora_de_termino": "2012-01-27T04:56:00Z",
              "lugar": "UCI",
              "icu_days": "7.10"
          }
      ],
      "imaging": [
          {
              "tipo_de_imagen": "Otro",
              "parte_del_cuerpo": "Pélvico",
              "opcion": True,
              "descripcion": "ANGIOTAC: NO SE OBSERVA  LIQUIDO  NI AIRE  EN PERITONEO  SE OBSERVAN CONTINUIDAD  DE  VASOS  Y GRAN FRACTURA  DEL ACETABULO  CUELLO  FÉMUR  Y DIAFISIS  FEMORAL."
          },
          {
              "tipo_de_imagen": "Otro",
              "parte_del_cuerpo": "Abdomen",
              "opcion": False,
              "descripcion": "Descripción de imagen"
          }
      ],
      "apparent_intent_injury": [
          {
              "intencion_aparente": "No especificado"
          },
          {
              "intencion_aparente": "Apuñalamiento"
          }
      ],
      "burn_injury": [
          {
              "tipo_de_quemadura": "Líquidos calientes",
              "grado_de_quemadura": "Segundo grado"
          },
          {
              "tipo_de_quemadura": "Aceite",
              "grado_de_quemadura": "Tercer grado"
          }
      ],
      "firearm_injury": [
          {
              "tipo_de_arma_de_fuego": "Arma de fuego no especificada"
          },
          {
              "tipo_de_arma_de_fuego": "Pistola"
          }
      ],
      "penetrating_injury": [
          {
              "tipo_de_lesion_penetrante": "Apuñalado"
          },
          {
              "tipo_de_lesion_penetrante": "Apuñalado con botella"
          }
      ],
      "poisoning_injury": [
          {
              "tipo_de_envenenamiento": "Pesticidas"
          },
          {
              "tipo_de_envenenamiento": "Veneno"
          }
      ],
      "violence_injury": [
          {
              "tipo_de_violencia": "Sospecha de violencia"
          },
          {
              "tipo_de_violencia": "Daño físico"
          }
      ],
      "device": [
          {
              "tipo_de_dispositivo": "Cinturón"
          },
          {
              "tipo_de_dispositivo": "Casco"
          }
      ],
      "laboratory": [
          {
              "resultado_de_laboratorio": "29.6",
              "fecha_y_hora_de_laboratorio": "2012-01-27T04:56:00Z",
              "nombre_del_laboratorio": "Hct- Hematocrito (%)",
              "nombre_de_la_unidad_de_laboratorio": "%"
          },
          {
              "resultado_de_laboratorio": "31.6",
              "fecha_y_hora_de_laboratorio": "2012-01-27T04:56:00Z",
              "nombre_del_laboratorio": "Hct (%)",
              "nombre_de_la_unidad_de_laboratorio": "%"
          }
      ],
      "physical_exam_body_part_injury": [
          {
              "parte_del_cuerpo": "Antebrazo Y Codo Izquierdo",
              "tipo_de_lesion": "Deformidad"
          },
          {
              "parte_del_cuerpo": "Antebrazo Y Codo Derecho",
              "tipo_de_lesion": "Deformidad"
          }
      ],
      "procedure": [
          {
              "procedimiento_realizado": "Administración de medicación",
              "fecha_y_hora_de_inicio": "2015-01-05T04:56:00Z",
              "fecha_y_hora_de_termino": "2015-01-05T04:56:00Z",
              "lugar": "Hospitalizacion-Piso"
          },
          {
              "procedimiento_realizado": "Administración de curación",
              "fecha_y_hora_de_inicio": "2015-01-05T04:56:00Z",
              "fecha_y_hora_de_termino": "2015-01-05T04:56:00Z",
              "lugar": "Hospitalizacion"
          }
      ],
      "prehospital_procedure": [
          {
              "procedimiento_realizado": "Mascara facial simple"
          },
          {
              "procedimiento_realizado": "Mascara facial compleja"
          }
      ],
      "transportation_mode": [
          {
              "modo_de_transporte": "Ambulancia terrestre"
          },
          {
              "modo_de_transporte": "Helicóptero"
          }
      ],
      "vital_sign": [
          {
              "record_id": 409777,
              "fecha_y_hora_de_signos_vitales": "2012-01-04T19:01:00Z",
              "signos_de_vida": True,
              "frecuencia_cardiaca": 88,
              "presion_arterial_sistolica": 90,
              "presion_arterial_diastolica": 60,
              "frecuencia_respiratoria": 16,
              "calificador_de_frecuencia_respiratoria": "Frecuencia Respiratoria Sin Asistencia",
              "temperatura_celsius": "36.00",
              "peso_kg": "68.00",
              "altura_metros": "1.60",
              "saturacion_de_oxigeno": "98.00",
              "perdida_de_conciencia": "No",
              "duracion_de_perdida_de_conciencia": "00:02:00",
              "gcs_motora": 6,
              "gcs_ocular": 5,
              "gcs_verbal": 4,
              "gcs_total": 15,
              "avup": "Alerta"
          },
          {
              "record_id": 409772,
              "fecha_y_hora_de_signos_vitales": "2012-01-04T19:01:00Z",
              "signos_de_vida": False,
              "frecuencia_cardiaca": 88,
              "presion_arterial_sistolica": 90,
              "presion_arterial_diastolica": 60,
              "frecuencia_respiratoria": 16,
              "calificador_de_frecuencia_respiratoria": "Frecuencia Respiratoria Sin Asistencia",
              "temperatura_celsius": "36.00",
              "peso_kg": "68.00",
              "altura_metros": "1.60",
              "saturacion_de_oxigeno": "98.00",
              "perdida_de_conciencia": "Si",
              "duracion_de_perdida_de_conciencia": "00:02:00",
              "gcs_motora": 6,
              "gcs_ocular": 5,
              "gcs_verbal": 4,
              "gcs_total": 15,
              "avup": "Alerta"
          }
      ],
      "direccion_linea_1": None,
      "direccion_linea_2": "Calle almendras",
      "ciudad": "Cali",
      "canton_municipio": None,
      "provincia_estado": "VALLE DEL CAUCA",
      "codigo_postal": None,
      "pais": "Colombia",
      "edad": 77,
      "unidad_de_edad": "Años",
      "genero": "Femenino",
      "fecha_de_nacimiento": "1973-09-26",
      "ocupacion": "No especificado",
      "estado_civil": "Soltero",
      "nacionalidad": "Colombia",
      "grupo_etnico": None,
      "otro_grupo_etnico": None,
      "num_doc_de_identificacion": "124235234777"
    }

  def test_create_patient_with_related_records(self):
    serializer = PatientDataSerializer(data=self.patient_data)
    self.assertTrue(serializer.is_valid(), serializer.errors)

    patient = serializer.save()

    # Verificar que el paciente se creó
    self.assertEqual(PatientData.objects.count(), 1)
    self.assertEqual(patient.trauma_register_record_id, 777)
    
    self.assertEqual(HealthcareRecord.objects.count(), 1)
    healthcareRecord = HealthcareRecord.objects.first()
    self.assertEqual(healthcareRecord.trauma_register_record_id, patient)
    
    self.assertEqual(InjuryRecord.objects.count(), 1)
    injuryRecord = InjuryRecord.objects.first()
    self.assertEqual(injuryRecord.trauma_register_record_id, patient)
    
    self.assertEqual(Collision.objects.count(), 2)
    collision = Collision.objects.first()
    self.assertEqual(collision.trauma_register_record_id, patient)
    
    self.assertEqual(DrugAbuse.objects.count(), 2)
    drugAbuse = DrugAbuse.objects.first()
    self.assertEqual(drugAbuse.trauma_register_record_id, patient)
    
    self.assertEqual(VitalSignGcsQualifier.objects.count(), 2)
    vitalSignGcsQualifier = VitalSignGcsQualifier.objects.first()
    self.assertEqual(vitalSignGcsQualifier.trauma_register_record_id, patient)
    
    self.assertEqual(HospitalizationVariable.objects.count(), 2)
    hospitalizationVariable = HospitalizationVariable.objects.first()
    self.assertEqual(hospitalizationVariable.trauma_register_record_id, patient)
    
    self.assertEqual(HospitalizationComplication.objects.count(), 2)
    hospitalizationComplication = HospitalizationComplication.objects.first()
    self.assertEqual(hospitalizationComplication.trauma_register_record_id, patient)
    
    self.assertEqual(TraumaRegisterIcd10.objects.count(), 2)
    traumaRegisterIcd10 = TraumaRegisterIcd10.objects.first()
    self.assertEqual(traumaRegisterIcd10.trauma_register_record_id, patient)
    
    self.assertEqual(IntensiveCareUnit.objects.count(), 2)
    intensiveCareUnit = IntensiveCareUnit.objects.first()
    self.assertEqual(intensiveCareUnit.trauma_register_record_id, patient)
    
    self.assertEqual(Imaging.objects.count(), 2)
    _imaging = Imaging.objects.first()
    self.assertEqual(_imaging.trauma_register_record_id, patient)
    
    self.assertEqual(ApparentIntentInjury.objects.count(), 2)
    apparentIntentInjury = ApparentIntentInjury.objects.first()
    self.assertEqual(apparentIntentInjury.trauma_register_record_id, patient)
    
    self.assertEqual(BurnInjury.objects.count(), 2)
    burnInjury = BurnInjury.objects.first()
    self.assertEqual(burnInjury.trauma_register_record_id, patient)
    
    self.assertEqual(FirearmInjury.objects.count(), 2)
    firearmInjury = FirearmInjury.objects.first()
    self.assertEqual(firearmInjury.trauma_register_record_id, patient)
    
    self.assertEqual(PenetratingInjury.objects.count(), 2)
    penetratingInjury = PenetratingInjury.objects.first()
    self.assertEqual(penetratingInjury.trauma_register_record_id, patient)
    
    self.assertEqual(PoisoningInjury.objects.count(), 2)
    poisoningInjury = PoisoningInjury.objects.first()
    self.assertEqual(poisoningInjury.trauma_register_record_id, patient)
    
    self.assertEqual(ViolenceInjury.objects.count(), 2)
    violenceInjury = ViolenceInjury.objects.first()
    self.assertEqual(violenceInjury.trauma_register_record_id, patient)
    
    self.assertEqual(Device.objects.count(), 2)
    device = Device.objects.first()
    self.assertEqual(device.trauma_register_record_id, patient)
    
    self.assertEqual(Laboratory.objects.count(), 2)
    laboratory = Laboratory.objects.first()
    self.assertEqual(laboratory.trauma_register_record_id, patient)
    
    self.assertEqual(PhysicalExamBodyPartInjury.objects.count(), 2)
    physicalExamBodyPartInjury = PhysicalExamBodyPartInjury.objects.first()
    self.assertEqual(physicalExamBodyPartInjury.trauma_register_record_id, patient)
    
    self.assertEqual(Procedure.objects.count(), 2)
    procedure = Procedure.objects.first()
    self.assertEqual(procedure.trauma_register_record_id, patient)
    
    self.assertEqual(PrehospitalProcedure.objects.count(), 2)
    prehospitalProcedure = PrehospitalProcedure.objects.first()
    self.assertEqual(prehospitalProcedure.trauma_register_record_id, patient)
    
    self.assertEqual(TransportationMode.objects.count(), 2)
    transportationMode = TransportationMode.objects.first()
    self.assertEqual(transportationMode.trauma_register_record_id, patient)
    
    self.assertEqual(VitalSign.objects.count(), 2)
    vitalSign = VitalSign.objects.first()
    self.assertEqual(vitalSign.trauma_register_record_id, patient)
    self.assertEqual(vitalSign.record_id, 409777)
