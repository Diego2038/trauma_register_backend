
#! NOTE: If you want to create two or more tables from one sheet, you must finish with the character ":" followed by its numeral 
columns_ubication : dict[str, dict[str,str]] = {  
    "Trauma Register:1": { #* Patient Data
      "trauma_register_record_id": "A", 
      "direccion_linea_1": "G", 
      "direccion_linea_2": "H", 
      "ciudad": "I", 
      "canton_municipio": "J", 
      "provincia_estado": "K", 
      "codigo_postal": "L", 
      "pais": "M", 
      "edad": "N", 
      "unidad_de_edad": "O", 
      "genero": "P", 
      "fecha_de_nacimiento": "Q", 
      "ocupacion": "R", 
      "estado_civil": "S", 
      "nacionalidad": "T", 
      "grupo_etnico": "Y", 
      "otro_grupo_etnico": "Z", 
      "num_doc_de_identificacion": "AC", 
    },
    "Trauma Register:2": { #!* Health Patient Attention
      "trauma_register_record_id": "A",
      "numero_de_historia_clinica": "B",
      "hospital": "C",
      "fecha_y_hora_de_llegada_del_paciente": "D",
      "referido": "E",
      "policia_notificada": "F",
      "fecha_y_hora_de_llegada_del_medico": "U",
      "fecha_y_hora_de_notificacion_al_medico": "V",
      "alerta_equipo_de_trauma": "W",
      "nivel_de_alerta": "X",
      "paciente_asegurado": "AA",
      "tipo_de_seguro": "AB",
      "motivo_de_consulta": "AD",
      "inmunizacion_contra_el_tetanos": "AI",
      "descripcion_del_examen_fisico": "AY",
      "mecanismo_primario": "AZ",
      "numero_de_lesiones_serias": "BA",
      "descripcion_del_diagnostico": "BB",
      "disposicion_o_destino_del_paciente": "BC",
      "donacion_de_organos": "BD",
      "autopsia": "BE",
      "muerte_prevenible": "BF",
      "tipo_de_admision": "BG",
      "fecha_y_hora_de_la_disposicion": "BH",
      "tiempo_en_sala_de_emergencias_hora": "BI",
      "tiempo_en_sala_de_emergencias_minutos": "BJ",
      "numero_de_referencia_del_ed": "BK",
      "fecha_de_admision": "BL",
      "fecha_y_hora_de_alta": "BM",
      "dias_de_hospitalizacion": "BN",
      "uci_dias": "BO",
      "detalles_de_hospitalizacion": "BP",
      "disposicion_o_destino_del_paciente_del_hospitalizacionSTRIN": "BQ",
      "donacion_de_organos_del_hospitalizacion": "BR",
      "autopsia_del_hospitalizacion": "BS",
      "muerte_prevenible_del_hospitalizacion": "BT",
      "numero_de_referencia_del_hospitalizacion": "BU",
      "agencia_de_transporte": "BV",
      "origen_del_transporte": "BW",
      "numero_de_registro_del_transporte": "BX",
      "fecha_y_hora_de_notificacion_pre_hospitalaria": "BY",
      "fecha_y_hora_de_llegada_a_la_escena": "BZ",
      "fecha_y_hora_de_salida_de_la_escena": "CA",
      "razon_de_la_demora": "CB",
      "reporte_o_formulario_pre_hospitalario_entregado": "CC",
      "ciudad_hospital_mas_cercano_al_sitio_del_incidente": "CD",
      "tiempo_de_extricacion_hora": "CE",
      "tiempo_de_extricacion_minutos": "CF",
      "duracion_del_transporte_horas": "CG",
      "duracion_del_transporte_minutos": "CH",
      "procedimiento_realizado": "CI",
      "frecuencia_cardiaca_en_la_escena": "CJ",
      "presion_arterial_sistolica_en_la_escena": "CK",
      "presion_arterial_diastolica_en_la_escena": "CL",
      "frecuencia_respiratoria_en_la_escena": "CM",
      "calificador_de_frecuencia_respiratoria_en_la_escena": "CN",
      "temperatura_en_la_escena_celsius": "CO",
      "saturacion_de_o2_en_la_escena": "CP",
      "frecuencia_cardiaca_durante_el_transporte": "CQ",
      "presion_arterial_sistolica_de_transporte": "CR",
      "presion_diastolica_durante_el_transporte": "CS",
      "frecuencia_respiratoria_durante_el_transporte": "CT",
      "calificador_de_frecuencia_respiratoria_durante_el_transporte": "CU",
      "temperatura_durante_el_transporte_celsius": "CV",
      "saturacion_de_o2_durante_el_transporte": "CW",
      "perdida_de_conciencia": "CX",
      "duracion_de_perdida_de_conciencia": "CY",
      "gcs_ocular": "CZ",
      "gcs_verbal": "DA",
      "gcs_motora": "DB",
      "gcs_total": "DC",
      "sangre_l": "DD",
      "coloides_l": "DE",
      "cristaloides_l": "DF",
      "hallazgos_clinicos_texto": "DG",
      "fecha_y_hora_de_envio_de_contra_referencia": "DH",
      "fecha_de_alta_de_contrar_referencia": "DI",
      "hallazgos_clinicos_existencia": "DJ",
      "servicio_que_atendio": "DK",
      "paciente_admitido": "DL",
      "hospital_que_recibe": "DM",
      "otro_servicio": "DN",
      "servicio_que_recibe": "DO",
      "recomendaciones": "DP",
      "numero_de_referencia_de_referencias_salientes": "DQ",
      "fecha_de_envio_de_referencia": "DR",
      "fecha_de_referencia": "DS",
      "razon_de_la_referencia": "DT",
      "medico_que_refiere": "DU",
      "estado_de_referencia": "DV",
      "fecha_de_aceptacion_de_referencia": "DW",
      "iss": "DX",
      "kts": "DY",
      "rts": "DZ",
      "abdomen": "EA",
      "torax": "EB",
      "externo": "EC",
      "extremidades": "ED",
      "cara": "EE",
      "cabeza": "EF",
      "triss_contuso": "EG",
      "triss_penetrante": "EH",
    },
    "Trauma Register:3": { #* Injury Patient Record
      "trauma_register_record_id": "A",
      "consumo_de_alcohol": "AE",
      "valor_de_alcoholemia": "AF",
      "unidad_de_alcohol": "AG",
      "otra_sustancia_de_abuso": "AH",
      "direccion_nombre_del_lugar": "AJ",
      "ciudad_de_evento_de_la_lesion": "AK",
      "condado_de_lesiones": "AL",
      "estado_provincia_de_lesiones": "AM",
      "pais_de_lesiones": "AN",
      "codigo_postal_de_lesiones": "AO",
      "fecha_y_hora_del_evento": "AP",
      "accidente_de_trafico": "AQ",
      "tipo_de_vehiculo": "AR",
      "ocupante": "AS",
      "velocidad_de_colision": "AT",
      "scq": "AU",
      "caida": "AV",
      "altura_metros": "AW",
      "tipo_de_superficie": "AX",
    },
    "Collision": {
      "trauma_register_record_id": "A",
      "tipo_de_colision": "B",
    },
    "Drug Abuse": {
      "trauma_register_record_id": "A",
      "tipo_de_droga": "B",
      
    },
    "Vital Sign GCS Qualifier": {
      "trauma_register_record_id": "A",
      "calificador_gcs": "B",
    },
    "Hospitalization Variable": {
      "trauma_register_record_id": "A",
      "tipo_de_variable": "B",
      "valor_de_la_variable": "C",
      "fecha_y_hora_de_la_variable": "D",
      "localizacion_de_variable": "E",
    },
    "Hospitalization Complication": {
      "trauma_register_record_id": "A",
      "tipo_de_complicacion": "B",
      "fecha_y_hora_de_complicacion": "C",
      "lugar_de_complicacion": "D",
    },
    "Trauma Register ICD10": {
      "trauma_register_record_id": "A",
      "descripcion": "B",
      "mecanismo_icd": "C",
    },
    "Intensive Care Unit": {
      "trauma_register_record_id": "A",
      "tipo": "B",
      "fecha_y_hora_de_inicio": "C",
      "fecha_y_hora_de_termino": "D",
      "lugar": "E",
      "icu_days": "F", 
    },
    "Imaging": {
      "trauma_register_record_id": "A",
      "tipo_de_imagen": "B",
      "parte_del_cuerpo": "C",
      "opcion": "D",
      "descripcion": "E",
    },
    "Apparent Intent Injury": {
      "trauma_register_record_id": "A",
      "intencion_aparente": "B",
    },
    "Burn Injury": {
      "trauma_register_record_id": "A",
      "tipo_de_quemadura": "B",
      "grado_de_quemadura": "C",
    },
    "Firearm Injury": {
      "trauma_register_record_id": "A",
      "tipo_de_arma_de_fuego": "B",
    },
    "Penetrating Injury": {
      "trauma_register_record_id": "A",
      "tipo_de_lesion_penetrante": "B",
    },
    "Poisoning Injury": {
      "trauma_register_record_id": "A",
      "tipo_de_envenenamiento": "B",
    },
    "Violence Injury": {
      "trauma_register_record_id": "A",
      "tipo_de_violencia": "B",
    },
    "Device": {
      "trauma_register_record_id": "A",
      "tipo_de_dispositivo": "B",
    },
    "Laboratory": {
      "trauma_register_record_id": "A",
      "resultado_de_laboratorio": "B",
      "fecha_y_hora_de_laboratorio": "C",
      "nombre_del_laboratorio": "D",
      "nombre_de_la_unidad_de_laboratorio": "E",
    },
    "Physical Exam Body Part Injury": {
      "trauma_register_record_id": "A",
      "parte_del_cuerpo": "B",
      "tipo_de_lesion": "C",
    },
    "Procedure": {
      "trauma_register_record_id": "A",
      "procedimiento_realizado": "B",
      "fecha_y_hora_de_inicio": "C",
      "fecha_y_hora_de_termino": "D",
      "lugar": "E",
    },
    "Prehospital Procedure": {
      "trauma_register_record_id": "A",
      "procedimiento_realizado": "B",
    },
    "Transportation Mode": {
      "trauma_register_record_id": "A",
      "modo_de_transporte": "B",
    },
    "Vital Sign": {
      "record_id" : "A",
      "trauma_register_record_id" : "B",
      "fecha_y_hora_de_signos_vitales" : "C",
      "signos_de_vida" : "D",
      "frecuencia_cardiaca" : "E",
      "presion_arterial_sistolica" : "F",
      "presion_arterial_diastolica" : "G",
      "frecuencia_respiratoria" : "H",
      "calificador_de_frecuencia_respiratoria" : "I",
      "temperatura_celsius" : "J",
      "peso_kg" : "K",
      "altura_metros" : "L",
      "saturacion_de_oxigeno" : "M",
      "perdida_de_conciencia" : "N",
      "duracion_de_perdida_de_conciencia" : "O",
      "gcs_motora" : "P",
      "gcs_ocular" : "Q",
      "gcs_verbal" : "R",
      "gcs_total" : "S",
      "avup" : "T",
    },
}