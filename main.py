from os import system
from datetime import date, timedelta
import saque
import deposito
"""
    Criar um sistema bancario com deposito, saque e extrato.
    limite de 10 saques diarios, maximo de R$500,00 por saque   
"""
extrato = {'Total': 0, 'Extrato': []}


def ext(extrato, total=extrato['Total']):
    system('cls')
    print('Ações realizadas na conta: ')
    for i in extrato['Extrato']:
        print(i)
    print(f'Seu total é de R${total}.00')
    
_ = True
hoje = date.today()
while _:
    print('-'*35)
    choice = input('Qual operação você deseja realizar? \n[1]Deposito \n[2]Saque \n[3]Extrato \n[4]Sair \n')
    if choice == '1':
        system('cls')
        deposito.deposito(extrato)
    elif choice == '2':
            saque.saque(extrato=extrato)
    elif choice == '3':
        ext(extrato, total=extrato['Total'])
    elif choice == '4':
        system('cls')
        print('Até logo!')
        _ = False
    else:
        system('cls')
        print('Insira algo valido!')
        d = hoje + timedelta(days=1)