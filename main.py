from bio.ler_fasta import ler_fasta
from problemas.problema_1 import analisar_percentuais
from bio.sequencia import Sequencia
from problemas.problema_3 import identificar_mutacao


caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"
organismos_do_fasta = ler_fasta(caminho_do_arquivo)

print("Os organismos desse arquivo fasta são:")

for organismo in organismos_do_fasta:
    print(organismo.nome)
    print("A sequência complementar é (8 primeiras bases):",organismo.sequencia.complementar() [:8])
    print("A sequência complementar reversa é (8 primeiras bases):",organismo.sequencia.complementar_reversa()[:8])
    print("O resultado da transcrição é: ",organismo.sequencia.transcrever()[:8])
    print("O resultado da tradução é: ",organismo.sequencia.traduzir()[:8])
    print("Percentual de A é :", organismo.sequencia.calcular_percentual(["A"]))
    print("Percentual de C e G é:", organismo.sequencia.calcular_percentual(["C", "G"]))
    


for organismo in organismos_do_fasta:
    percentual_A, percentual_T, percentual_C, percentual_G, conteudo_GC = analisar_percentuais(organismo)

    print(f"Organismo: {organismo.nome}")
    print(f"A: {percentual_A} %")
    print(f"T: {percentual_T} %")
    print(f"C: {percentual_C} %")
    print(f"G: {percentual_G} %")
    print(f"GC: {conteudo_GC} %")

for organismo in organismos_do_fasta:
    seq_nuc = organismo.sequencia.sequencia  
    s = Sequencia(seq_nuc)
    proteina = s.traduzir()

    print(f">{organismo.nome}")
    print(f"A proteína é: {proteina}")

relatorio = identificar_mutacao(organismos_do_fasta,posicao=999, original='A', mutado='G')

for nome, tem_mutacao, nucleotideo_encontrado in relatorio:
    print(f"{nome} | Mutação: {tem_mutacao} | Nucleotídeo encontrado: {nucleotideo_encontrado}")