
def analisar_percentuais(organismo):
    percentual_A = organismo.sequencia.calcular_percentual("A")
    percentual_T = organismo.sequencia.calcular_percentual("T")
    percentual_C = organismo.sequencia.calcular_percentual("C")
    percentual_G = organismo.sequencia.calcular_percentual("G")
    conteudo_GC = organismo.sequencia.calcular_percentual("GC")

    return percentual_A, percentual_T, percentual_C, percentual_G, conteudo_GC