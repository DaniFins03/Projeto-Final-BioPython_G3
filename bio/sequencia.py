from bio.constantes import DNA_PARA_AMINOACIDO,DNA_STOP_CODONS


class Sequencia:

    def __init__(self, sequencia):
        self.sequencia = sequencia

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __iter__(self):
        return self.sequencia

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia.__getitem__(index)
    
    def complementar(self):
        complementos = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        complementar = ""
        for base in self.sequencia:
            if base in complementos:
                complementar += complementos[base]
            else:
                complementar += base
        return Sequencia(complementar)

    def complementar_reversa(self):
        complementar= self.complementar()
        complementar_rev = complementar[::-1]
        return Sequencia(complementar_rev)
    
    def transcrever(self):
        transcrito = ""
        for base in self.sequencia:
            if base == "T":
                transcrito += "U"
            else:
                transcrito += base
        return Sequencia(transcrito)
    
    def traduzir(self,parar=False):
        proteina=""
        for i in range (0,len(self.sequencia),3):
            codon=self.sequencia[i:i+3]
            if len(codon) < 3:
                break
            if parar and (codon in DNA_STOP_CODONS):
                break
            elif codon in DNA_STOP_CODONS:
                aminoacido = "*"
            elif codon in DNA_PARA_AMINOACIDO:
                aminoacido=DNA_PARA_AMINOACIDO[codon]
            else:
                aminoacido = "x"
            proteina += aminoacido
        return proteina 
    
    def calcular_percentual(self,bases):
        total = len(self.sequencia)
        contador=0
        for base in self.sequencia:
            if base in bases:
                contador += 1
        if total == 0:
            return 0.0
        
        percentual = contador / total
        return f"{percentual:.2f}"