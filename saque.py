from util import dataFormatada
from datetime import date
from os import system


limitador = []
hoje = date.today()

def saque(extrato=None):
    quantia = input('Quanto deseja sacar? ')
    quantia = int(quantia)
    money = extrato['Total']
    if len(limitador) >= 10:
        if quantia <= 500:
            if extrato['Total'] == 0:
                print('Seu saldo está em 0, faça um deposito para prosseguir.')
            elif extrato['Total'] <= quantia:
                print('Seu saldo está com valor menor do que o desejado, faça um deposito para prosseguir.')
            else:
                extrato['Total'] = money - quantia
                extrato['Extrato'].append(f'- R${quantia}.00 | {dataFormatada()}')
                limitador.append(hoje)
        else:
            print('Limite de saque de R$500.00, tente novamente com um valor menor.')
    else:
        system('cls')
        print('Limite de saques diario excedidos, tente novamente amanhã.')