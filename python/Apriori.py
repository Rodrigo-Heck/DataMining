# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:42:51 2021

@author: Rodrigo
"""

from apyori import apriori
import DataProcess as ids

dados = ids.dataWarehouse

support = 0.05
confidence = 0.35

regras = apriori(
                 dados,
                 min_support=support,
                 min_confidence=confidence,
                 )

resultados = list(regras)

with open("../Regras_associacao.txt", "w") as arquivo:
    arquivo.write("======================================\n")
    arquivo.write("Suporte Mínimo: " + str(support) + "\n")
    arquivo.write("Confiança Mínima: " + str(confidence) + "\n")
    arquivo.write("======================================\n\n")
    arquivo.write(" --| Sempre que teve os itemsets abaixo também teve OBITO |--\n\n")

    for i in range(len(resultados)):
        for ii in resultados[i][2]:
            if("OBITO" == list(ii.items_add)[0]):
                arquivo.write("Confiança: " + str(f'{ii.confidence:.2f}')
                              + str("  ")
                              + str(list(ii.items_base)) + "  Suporte: "
                              + str(f'{resultados[i].support:.2f}')
                              # + str("  Lift: ")
                              # + str(f'{ii.lift:.2f}')
                              + "\n\n")
print("\n\nFIM")
