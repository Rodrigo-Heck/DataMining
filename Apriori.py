# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:42:51 2021

@author: Rodrigo
"""

from apyori import apriori
import INDEX as ids

dados = ids.dataWarehouse


#############################


regras = apriori(dados, min_support=0.02, min_confidence=0.3, min_lift=1.0, min_lenght=1)

resultados = list(regras)

with open("Regras_associacao.txt", "w") as arquivo:
    for i in range(len(resultados)):
        for ii in resultados[i][2]:
            if("OBITO" == list(ii.items_add)[0]):
                #arquivo.write("Se " + str(list(ii.items_base)) + " Então " + str(list(ii.items_add)) + " Confiança: " + str(ii.confidence) + " Suporte: " + str(resultados[i].support) + "\n\n" )
                arquivo.write("Confiança: " + str(f'{ii.confidence:.2f}')
                              +str("  ")
                              + str(list(ii.items_base)) + "  Suporte: "
                              + str(f'{resultados[i].support:.2f}')
                              #+ str("  Lift: ")
                              #+ str(f'{ii.lift:.2f}')
                              + "\n\n")
print("\n\nFIM")
