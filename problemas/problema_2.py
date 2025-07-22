
def parse_multifasta(caminho):
    sequencias = {}
    with open(caminho) as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith(">"):
                id = linha[1:]
                sequencias[id] = ""
            else:
                sequencias[id] += linha
    return sequencias