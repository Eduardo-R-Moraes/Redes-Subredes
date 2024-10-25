from helpers import *

setores = []
hosts = []

print('\nPara parar de entrar dados digite 0 em um dos campos')
while True:
    print('---------------------------------------------------')
    setor = int(input('Digite o número do setor: '))
    if setor == 0: break

    if not setor in setores:

        setores.append(setor)
        numHosts = int(input('Digite o número de hosts: '))
        if numHosts == 0: break

        setores.append(setores)
        hosts.append(hosts)
    else:
        print('---------------------------------------------------')
        print(f'Setor {setor} já está sendo usado!')

maiorHost = maior(hosts)

numeroZeros, faixa = faixa(maiorHost)
mascaraRede = f'/{32-numeroZeros}'

mascBinaria = mascaraBinaria(numeroZeros)

mascDecimal = mascaraDecimal(faixa)

redes = redes(setores, hosts, faixa)

for valor in redes:
    print('-----------------------------------------------------------------------------')
    print(f'Setor {valor["setor"]}')
    print(f'Rede: {valor["inicio"]}')
    print(f'Hosts ativos: {valor["hostAtivosInicio"]} -> {valor["hostAtivosFinal"]}')
    print(f'Hosts totais: {valor["hostTotaisInicio"]} -> {valor["hostTotaisFinal"]}')
    print(f'BroadCast: {valor["fim"]}')

print('-----------------------------------------------------------------------------')
print('Sobre a rede:')
print(f'- Mascara de rede: {mascaraRede}')
print(f'- Binário: {mascBinaria}')
print(f'- Decimal: {mascDecimal}')