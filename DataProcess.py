# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 20:26:46 2021

@author: Rodrigo
"""
import pandas as pd
import treatmentFunctions as tf


dw = pd.read_csv('INFLUD-04-10-2021.csv', sep=";")

dropColumns = ["DT_NOTIFIC",
               "SEM_NOT",
               "SEM_PRI",
               "DT_SIN_PRI",
               "SG_UF_NOT",
               "ID_MUNICIP",
               "ID_REGIONA",
               "ID_UNIDADE",
               "CO_UNI_NOT",
               "NU_IDADE_N",
               "TP_IDADE",
               "COD_IDADE",
               "CS_ETINIA",
               "CS_ESCOL_N",
               "ID_PAIS",
               "CO_PAIS",
               "SG_UF",
               "ID_RG_RESI",
               "CO_RG_RESI",
               "ID_MN_RESI",
               "CO_MUN_RES",
               "CS_ZONA",
               "CO_REGIONA",
               "CO_MUN_NOT",
               "NOSOCOMIAL",
               "OUTRO_SIN",
               "OUTRO_DES",
               "OUT_MORBI",
               "MORB_DESC",
               "VACINA",
               "DT_UT_DOSE",
               "MAE_VAC",
               "DT_VAC_MAE",
               "M_AMAMENTA",
               "DT_DOSEUNI",
               "DT_1_DOSE",
               "DT_2_DOSE",
               "ANTIVIRAL",
               "TP_ANTIVIR",
               "OUT_ANTIV",
               "DT_ANTIVIR",
               "HOSPITAL",  # Data em que o paciente foi hospitalizado
               "DT_INTERNA",  # Data internação
               "SG_UF_INTE",
               "ID_RG_INTE",
               "ID_MN_INTE",
               "DT_ENTUTI",  # Data entrada UTI
               "DT_SAIDUTI",  # Data saida UTI
               "SUPORT_VEN",
               "RAIOX_RES",
               "RAIOX_OUT",
               "DT_RAIOX",
               "TOMO_RES",
               "TOMO_OUT",
               "DT_TOMO",
               "AMOSTRA",
               "DT_COLETA",
               "TP_AMOSTRA",
               "OUT_AMOST",
               "TP_TES_AN",
               "DT_RES_AN",
               "RES_AN",
               "POS_AN_FLU",
               "TP_FLU_AN",
               "POS_AN_OUT",
               "AN_SARS2",
               "AN_VSR",
               "AN_PARA1",
               "AN_PARA2",
               "AN_PARA3",
               "AN_ADENO",
               "AN_ADENO",
               "DS_AN_OUT",
               "PCR_RESUL",
               "DT_PCR",
               "POS_PCRFLU",
               "TP_FLU_PCR",
               "TP_FLU_PCR",
               "FLUASU_OUT",
               "PCR_FLUBLI",
               "PCR_FLUBLI",
               "POS_PCROUT",
               "PCR_VSR",
               "PCR_PARA1",
               "PCR_PARA2",
               "PCR_PARA3",
               "PCR_PARA4",
               "PCR_ADENO",
               "PCR_METAP",
               "PCR_BOCA",
               "PCR_RINO",
               "PCR_OUTRO",
               "DS_PCR_OUT",
               "TP_AM_SOR",
               "SOR_OUT",
               "DT_CO_SOR",
               "TP_SOR",
               "OUT_SOR",
               "SOR_OUT",
               "RES_IGG",
               "RES_IGM",
               "RES_IGA",
               "DT_RES",
               "CLASSI_OUT",
               "CRITERIO",  # Critério de confirmação
               "DT_ENCERRA",
               "DT_DIGITA",
               "PAIS_VGM",
               "HISTO_VGM",
               "CO_PS_VGM",
               "LO_PS_VGM",
               "DT_RT_VGM",
               "PAC_COCBO",
               "PAC_DSCBO",
               "OUT_ANIM",
               "CO_MU_INTE",
               "CO_RG_INTE",
               "OBES_IMC",
               "AN_OUTRO",
               "DT_VGM",
               "CS_SEXO",
               "CS_RACA",
               "SURTO_SG",
               "AVE_SUINO",
               "DESC_RESP",
               "DOR_ABD",
               "PUERPERA",
               "FATOR_RISC",
               "PCR_RESUL",
               "FLUBLI_OUT",
               "DT_EVOLUCA",
               "PCR_FLUASU",
               "PCR_SARS2",
               "SATURACAO",
               "PERD_PALA",
               "PERD_OLFT",
               "UTI",
               "VOMITO",
               "FADIGA",
               "DIARREIA",
               "DISPNEIA",
               "GARGANTA",
               "FEBRE",
               "TOSSE"
               ]


dw = dw.drop(columns=dropColumns)

dw = tf.filters_only_covid_cases(dw)

dw = tf.treating_age(dw)  # Idade

dw = tf.treating_pregnant(dw)  # Gestante

# dw = tf.treating_fever(dw)  # Febre

# dw = tf.treating_cough(dw)  # Tosse

# dw = tf.treating_sore_throat(dw)  # Dor de Garganta

# dw = tf.treating_short_of_breath(dw)  # Falta de ar

# dw = tf.treating_diarrhea(dw)  # Diarreia

# dw = tf.treating_vomiting(dw)  # Vômito

# dw = tf.treating_fatigued(dw)  # Fadiga

# dw = tf.treating_loss_of_smell(dw)  # Perda de olfato

# dw = tf.treating_loss_of_taste(dw)  # Perda de Paladar

dw = tf.treating_chronic_cardiovascular_disease(dw)  # Doença Cardiovascular

dw = tf.treating_chronic_hematologic_disease(dw)  # Doença Hematológica Crônica

dw = tf.treating_Downs_syndrome(dw)  # Síndrome de Down

dw = tf.treating_chronic_liver_disease(dw)  # Doença Hepática Crônica

dw = tf.treating_asthma(dw)  # Asma

dw = tf.treating_diabetes(dw)  # Diabetes

dw = tf.treating_neurological_disease(dw)  # Doença Neurológica

dw = tf.treating_lung_disease(dw)  # Doença Pneumopática

dw = tf.treating_immunodepression_disease(dw)  # Imunodepressão

dw = tf.treating_kidney_disease(dw)  # Doença Renal

dw = tf.treating_obesity(dw)  # Obesidade

# dw = tf.treating_admitted_to_ICU(dw)  # Internado em UTI

dw = tf.treating_evolvement(dw)  # Evolução do caso

dw = dw.reset_index(drop=True)

dataWarehouse = []

for dw_row in dw.values:
    dataWarehouse.append(list(filter(lambda x: x != tf.nan(), dw_row)))
