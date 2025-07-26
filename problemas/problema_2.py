from bio.sequencia import Sequencia

def executar_problema_2(organismos):

    for organismo in organismos:
        print(f"\nOrganismo: {organismo.nome} (ID: {organismo.id})")
        
        seq = Sequencia(organismo.sequencia.sequencia)
        proteina = seq.traduzir()

        print("Proteína traduzida:")
        proteina.imprimir()