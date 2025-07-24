
from bio.sequencia import Sequencia
from bio.ler_fasta import ler_fasta 


def executar_problema_2(caminho_do_arquivo):
    organismos = ler_fasta (caminho_do_arquivo)

    for organismo in organismos:
        print(f"\nOrganismo: {organismo.nome} (ID: {organismo.id})")
        
        seq = Sequencia(organismo.sequencia)
        proteina = seq.traduzir(parar=False)

        print("Proteína traduzida:")
        proteina.imprimir()