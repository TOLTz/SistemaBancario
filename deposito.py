from util import dataFormatada

def deposito(extrato):
    quantia = input('Quanto deseja depositar? ')
    quantia = int(quantia)
    money = extrato['Total']
    extrato['Total'] = money + quantia
    extrato['Extrato'].append(f'+ R${quantia}.00 | {dataFormatada()} ')