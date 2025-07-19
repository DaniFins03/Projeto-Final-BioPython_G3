from bio.ler_fasta import ler_fasta 

caminho_do_arquivo ="./arquivos/Flaviviridae-genomes.fasta"
organismos_do_fasta = ler_fasta(caminho_do_arquivo)

print ("Os organismos desse arquivo são:" )

for organismo in organismos_do_fasta:
    print(organismo.nome)
    print("O tamanho é:", organismo.sequencia.calcular_tamanho())
    print("A sequência complementar é (8 primeiras bases):",organismo.sequencia.complementar() [:8])
    print("A sequência complementar reversa é (8 primeiras bases):",organismo.sequencia.complementar_reversa()[:8])
    print("O resultado da transcrição é: ",organismo.sequencia.transcrever()[:8])