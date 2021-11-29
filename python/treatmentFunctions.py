# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:48:24 2021

@author: Rodrigo
"""

import pandas as pd


def nan():
    return("x")


def filters_only_covid_cases(dw):
    dw = dw[dw["CLASSI_FIN"] == 5]  # Filtra somente os casos Covid-19
    dw.drop("CLASSI_FIN", axis=1, inplace=True)
    return(dw)


def treating_age(dw):
    print("Tratando Coluna DT_NASC")
    dw = dw[dw["DT_NASC"].notna()]
    now = pd.Timestamp.now().year
    dw["DT_NASC"] = pd.to_datetime(dw["DT_NASC"])
    dw["DT_NASC"] = now - dw["DT_NASC"].dt.year
    dw["DT_NASC"].astype(int)
    dw["FAIXA_IDADE"] = nan()
    dw.loc[dw["DT_NASC"] >= 60, "FAIXA_IDADE"] = "IDOSO"
    dw.drop("DT_NASC", axis=1, inplace=True)
    return(dw)


def treating_pregnant(dw):
    print("Tratando Coluna GESTANTE")
    dw = dw[dw["CS_GESTANT"].notna()]
    dw = dw[dw["CS_GESTANT"] != 9]
    dw["CS_GESTANT"].astype(int)
    dw["GESTANTE"] = nan()
    dw.loc[dw["CS_GESTANT"].between(1, 4), "GESTANTE"] = "GESTANTE"
    dw.drop("CS_GESTANT", axis=1, inplace=True)
    return(dw)


def treating_fever(dw):
    print("Tratando Coluna FEBRE")
    dw = dw[dw["FEBRE"].notna()]
    dw = dw[dw["FEBRE"] != 9]
    dw["FEBRE"].astype(int)
    dw["SINTOMA_FEBRE"] = nan()
    dw.loc[dw["FEBRE"] == 1, "SINTOMA_FEBRE"] = "FEBRE"
    dw.drop("FEBRE", axis=1, inplace=True)
    return(dw)


def treating_cough(dw):
    print("Tratando Coluna TOSSE")
    dw = dw[dw["TOSSE"].notna()]
    dw["TOSSE"].astype(int)
    dw["SINTOMA_TOSSE"] = nan()
    dw.loc[dw["TOSSE"] == 1, "SINTOMA_TOSSE"] = "TOSSE"
    dw.drop("TOSSE", axis=1, inplace=True)
    return(dw)


def treating_sore_throat(dw):
    print("Tratando Coluna GARGANTA")
    dw = dw[dw["GARGANTA"].notna()]
    dw = dw[dw["GARGANTA"] != 9]
    dw["GARGANTA"].astype(int)
    dw["SINTOMA_GARGANTA"] = nan()
    dw.loc[dw["GARGANTA"] == 1, "SINTOMA_GARGANTA"] = "DOR_GARGANTA"
    dw.drop("GARGANTA", axis=1, inplace=True)
    return(dw)


def treating_short_of_breath(dw):
    print("Tratando Coluna DISPNEIA")
    dw = dw[dw["DISPNEIA"].notna()]
    dw = dw[dw["DISPNEIA"] != 9]
    dw["DISPNEIA"].astype(int)
    dw["SINTOMA_DISPNEIA"] = nan()
    dw.loc[dw["DISPNEIA"] == 1, "SINTOMA_DISPNEIA"] = "FALTA_AR"
    dw.drop("DISPNEIA", axis=1, inplace=True)
    return(dw)


def treating_diarrhea(dw):
    print("Tratando Coluna DIARREIA")
    dw = dw[dw["DIARREIA"].notna()]
    dw = dw[dw["DIARREIA"] != 9]
    dw["DIARREIA"].astype(int)
    dw["SINTOMA_DIARREIA"] = nan()
    dw.loc[dw["DIARREIA"] == 1, "SINTOMA_DIARREIA"] = "DIARREIA"
    dw.drop("DIARREIA", axis=1, inplace=True)
    return(dw)


def treating_vomiting(dw):
    print("Tratando Coluna VOMITO")
    dw = dw[dw["VOMITO"].notna()]
    dw = dw[dw["VOMITO"] != 9]
    dw["VOMITO"].astype(int)
    dw["SINTOMA_VOMITO"] = nan()
    dw.loc[dw["VOMITO"] == 1, "SINTOMA_VOMITO"] = "VOMITO"
    dw.drop("VOMITO", axis=1, inplace=True)
    return(dw)


def treating_fatigued(dw):
    print("Tratando Coluna FADIGA")
    dw = dw[dw["FADIGA"].notna()]
    dw = dw[dw["FADIGA"] != 9]
    dw["FADIGA"].astype(int)
    dw["SINTOMA_FADIGA"] = nan()
    dw.loc[dw["FADIGA"] == 1, "SINTOMA_FADIGA"] = "FADIGA"
    dw.drop("FADIGA", axis=1, inplace=True)
    return(dw)


def treating_loss_of_smell(dw):
    print("Tratando Coluna PERD_OLFT")
    dw = dw[dw["PERD_OLFT"].notna()]
    dw = dw[dw["PERD_OLFT"] != 9]
    dw["PERD_OLFT"].astype(int)
    dw["SINTOMA_PERDA_OLFATO"] = nan()
    dw.loc[dw["PERD_OLFT"] == 1, "SINTOMA_PERDA_OLFATO"] = "PERDA_OLFATO"
    dw.drop("PERD_OLFT", axis=1, inplace=True)
    return(dw)


def treating_loss_of_taste(dw):
    print("Tratando Coluna PERD_PALA")
    dw = dw[dw["PERD_PALA"].notna()]
    dw = dw[dw["PERD_PALA"] != 9]
    dw["PERD_PALA"].astype(int)
    dw["SINTOMA_PERDA_PALADAR"] = nan()
    dw.loc[dw["PERD_PALA"] == 1, "SINTOMA_PERDA_PALADAR"] = "PERDA_PALADAR"
    dw.drop("PERD_PALA", axis=1, inplace=True)
    return(dw)


def treating_chronic_cardiovascular_disease(dw):
    print("Tratando Coluna CARDIOPATI")
    dw = dw[dw["CARDIOPATI"].notna()]
    dw = dw[dw["CARDIOPATI"] != 9]
    dw["CARDIOPATI"].astype(int)
    dw["DOENCA_CARDIOPATI"] = nan()
    dw.loc[dw["CARDIOPATI"] == 1, "DOENCA_CARDIOPATI"] = "CARDIOPATI"
    dw.drop("CARDIOPATI", axis=1, inplace=True)
    return(dw)


def treating_chronic_hematologic_disease(dw):
    print("Tratando Coluna HEMATOLOGI")
    dw = dw[dw["HEMATOLOGI"].notna()]
    dw = dw[dw["HEMATOLOGI"] != 9]
    dw["HEMATOLOGI"].astype(int)
    dw["DOENCA_HEMATOLOGI"] = nan()
    dw.loc[dw["HEMATOLOGI"] == 1, "DOENCA_HEMATOLOGI"] = "HEMATOLOGI"
    dw.drop("HEMATOLOGI", axis=1, inplace=True)
    return(dw)


def treating_Downs_syndrome(dw):
    print("Tratando Coluna SIND_DOWN")
    dw = dw[dw["SIND_DOWN"].notna()]
    dw = dw[dw["SIND_DOWN"] != 9]
    dw["SIND_DOWN"].astype(int)
    dw["SINDROME_DOWN"] = nan()
    dw.loc[dw["SIND_DOWN"] == 1, "SINDROME_DOWN"] = "SINDROME_DOWN"
    dw.drop("SIND_DOWN", axis=1, inplace=True)
    return(dw)


def treating_chronic_liver_disease(dw):
    print("Tratando Coluna HEPATICA")
    dw = dw[dw["HEPATICA"].notna()]
    dw = dw[dw["HEPATICA"] != 9]
    dw["HEPATICA"].astype(int)
    dw["DOENCA_HEPATICA"] = nan()
    dw.loc[dw["HEPATICA"] == 1, "DOENCA_HEPATICA"] = "HEPATICA"
    dw.drop("HEPATICA", axis=1, inplace=True)
    return(dw)


def treating_asthma(dw):
    print("Tratando Coluna ASMA")
    dw = dw[dw["ASMA"].notna()]
    dw = dw[dw["ASMA"] != 9]
    dw["ASMA"].astype(int)
    dw["DOENCA_ASMA"] = nan()
    dw.loc[dw["ASMA"] == 1, "DOENCA_ASMA"] = "ASMA"
    dw.drop("ASMA", axis=1, inplace=True)
    return(dw)


def treating_diabetes(dw):
    print("Tratando Coluna DIABETES")
    dw = dw[dw["DIABETES"].notna()]
    dw = dw[dw["DIABETES"] != 9]
    dw["DIABETES"].astype(int)
    dw["DOENCA_DIABETES"] = nan()
    dw.loc[dw["DIABETES"] == 1, "DOENCA_DIABETES"] = "DIABETES"
    dw.drop("DIABETES", axis=1, inplace=True)
    return(dw)


def treating_neurological_disease(dw):
    print("Tratando Coluna NEUROLOGIC")
    dw = dw[dw["NEUROLOGIC"].notna()]
    dw = dw[dw["NEUROLOGIC"] != 9]
    dw["NEUROLOGIC"].astype(int)
    dw["DOENCA_NEUROLOGIC"] = nan()
    dw.loc[dw["NEUROLOGIC"] == 1, "DOENCA_NEUROLOGIC"] = "NEUROLOGICA"
    dw.drop("NEUROLOGIC", axis=1, inplace=True)
    return(dw)


def treating_lung_disease(dw):
    print("Tratando Coluna PNEUMOPATI")
    dw = dw[dw["PNEUMOPATI"].notna()]
    dw = dw[dw["PNEUMOPATI"] != 9]
    dw["PNEUMOPATI"].astype(int)
    dw["DOENCA_PNEUMOPATI"] = nan()
    dw.loc[dw["PNEUMOPATI"] == 1, "DOENCA_PNEUMOPATI"] = "PNEUMOPATICA"
    dw.drop("PNEUMOPATI", axis=1, inplace=True)
    return(dw)


def treating_immunodepression_disease(dw):
    print("Tratando Coluna IMUNODEPRE")
    dw = dw[dw["IMUNODEPRE"].notna()]
    dw = dw[dw["IMUNODEPRE"] != 9]
    dw["IMUNODEPRE"].astype(int)
    dw["DOENCA_IMUNODEPRE"] = nan()
    dw.loc[dw["IMUNODEPRE"] == 1, "DOENCA_IMUNODEPRE"] = "IMUNODEPRESSAO"
    dw.drop("IMUNODEPRE", axis=1, inplace=True)
    return(dw)


def treating_kidney_disease(dw):
    print("Tratando Coluna RENAL")
    dw = dw[dw["RENAL"].notna()]
    dw = dw[dw["RENAL"] != 9]
    dw["RENAL"].astype(int)
    dw["DOENCA_RENAL"] = nan()
    dw.loc[dw["RENAL"] == 1, "DOENCA_RENAL"] = "RENAL"
    dw.drop("RENAL", axis=1, inplace=True)
    return(dw)


def treating_obesity(dw):
    print("Tratando Coluna OBESIDADE")
    dw = dw[dw["OBESIDADE"].notna()]
    dw = dw[dw["OBESIDADE"] != 9]
    dw["OBESIDADE"].astype(int)
    dw["DOENCA_OBESIDADE"] = nan()
    dw.loc[dw["OBESIDADE"] == 1, "DOENCA_OBESIDADE"] = "OBESIDADE"
    dw.drop("OBESIDADE", axis=1, inplace=True)
    return(dw)


def treating_obesity(dw):
    print("Tratando Coluna OBESIDADE")
    dw = dw[dw["OBESIDADE"].notna()]
    dw = dw[dw["OBESIDADE"] != 9]
    dw["OBESIDADE"].astype(int)
    dw["DOENCA_OBESIDADE"] = nan()
    dw.loc[dw["OBESIDADE"] == 1, "DOENCA_OBESIDADE"] = "OBESIDADE"
    dw.drop("OBESIDADE", axis=1, inplace=True)
    return(dw)


def treating_admitted_to_ICU(dw):
    print("Tratando Coluna UTI")
    dw = dw[dw["UTI"].notna()]
    dw = dw[dw["UTI"] != 9]
    dw["UTI"].astype(int)
    dw["INTERNACAO_UTI"] = nan()
    dw.loc[dw["UTI"] == 1, "INTERNACAO_UTI"] = "UTI"
    dw.drop("UTI", axis=1, inplace=True)
    return(dw)


def treating_evolvement(dw):
    print("Tratando Coluna EVOLUCAO")
    dw = dw[dw["EVOLUCAO"].notna()]
    dw = dw[dw["EVOLUCAO"] != 9]
    dw = dw[dw["EVOLUCAO"] != 3]
    dw["EVOLUCAO"].astype(int)
    dw["CASO_EVOLUCAO"] = nan()
    dw.loc[dw["EVOLUCAO"] == 2, "CASO_EVOLUCAO"] = "OBITO"
    dw.drop("EVOLUCAO", axis=1, inplace=True)
    return(dw)
