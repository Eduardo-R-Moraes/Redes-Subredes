def faixaRede(numero:int):
    vetor = [2 ** i for i in range(2, 18)]
    numeroZeros = 0
    
    for i in range(len(vetor)):
        if numero + 1 < vetor[i]:
            numeroZeros = i + 2
            return numeroZeros, vetor[i]
        
def mascaraBinaria(numeroZeros:int):
    numeroUns = 16 - numeroZeros
    mascaraBinaria = '11111111.11111111.'
    for i in range(17):
        if i == 8: mascaraBinaria += '.'

        elif numeroUns: 
            mascaraBinaria += '1'
            numeroUns -= 1

        else: mascaraBinaria += '0'
    
    return mascaraBinaria

def mascaraDecimal(faixa):
    if faixa < 256:
        return f'255.255.255.{255 - faixa}'

    maior = faixa // 256
    return f'255.255.{256 - maior}.0'

def redes(setores:list[int], hosts:list[int], faixa:int):
    redes = []
    subrede = 0
    inicio = 0

    for i in range(len(setores)):
        if inicio == 256:
            subrede += 1
            inicio = 0
        
        if faixa < 256:
            fim = inicio + faixa - 1
            subredeFinal = subrede
            subredeHostTotais = subrede
            hostTotaisFinal = inicio + faixa - 2
            subredeHostAtivoFinal = subrede
            hostAtivosFinal = inicio + hosts[i] + 1

        if faixa >= 256:
            fim = 255
            subredeFinal = (subrede + faixa // 256) - 1
            subredeHostTotais = subredeFinal
            hostTotaisFinal = 254
            subredeHostAtivoFinal = subrede

            if hosts[i] >= 256:
                subredeHostAtivoFinal += hosts[i] // 256 - 1
                resto = hosts[i] % 256
                hostAtivosFinal = resto

            else:
                hostAtivosFinal = inicio + hosts[i] + 1

        rede = { 
            'setor': i+1,

            'inicio': f'192.168.{subrede}.{inicio}',
            'fim': f'192.168.{subredeFinal}.{fim}',

            'hostAtivosInicio': f'192.168.{subrede}.{inicio + 1}',
            'hostAtivosFinal': f'192.168.{subredeHostAtivoFinal}.{hostAtivosFinal}',

            'hostTotaisInicio': f'192.168.{subrede}.{inicio + 1}',
            'hostTotaisFinal': f'192.168.{subredeHostTotais}.{hostTotaisFinal}'
        }

        if faixa < 256: inicio += faixa

        if faixa > 256: subrede = subredeFinal + 1

        redes.append(rede)

    return redes
