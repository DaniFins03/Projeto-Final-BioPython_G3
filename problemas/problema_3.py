
def identificar_mutacao(sequencias, posicao=999, original='A', mutado='G'):
    relatorio = []

    for sequencia in sequencias:
        if len(sequencia.sequencia) > posicao:
            nucleotideo_encontrado = sequencia.sequencia[posicao].upper()
            tem_mutacao = nucleotideo_encontrado == mutado
            relatorio.append((sequencia.nome, tem_mutacao, nucleotideo_encontrado))
        else:
            relatorio.append((sequencia.nome, False, 'Sequência muito curta'))

    return relatorio
