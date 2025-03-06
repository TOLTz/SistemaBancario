from os import system
"""
    Criar um sistema bancario com deposito, saque e extrato.
    limite de 3 saques diarios, maximo de R$500,00 por saque   
"""

extrato = {'Total': 0, 'Extrato': []}
def deposito(extrato):
    quantia = input('Quanto deseja depositar? ')
    quantia = int(quantia)
    money = extrato['Total']
    extrato['Total'] = money + quantia
    extrato['Extrato'].append(f'+ R${quantia}.00')

def saque(extrato):
    quantia = input('Quanto deseja sacar? ')
    quantia = int(quantia)
    money = extrato['Total']
    if quantia <= 500:
        if extrato['Total'] == 0:
            print('Seu saldo está em 0, faça um deposito para prosseguir.')
        elif extrato['Total'] <= quantia:
            print('Seu saldo está com valor menor do que o desejado, faça um deposito para prosseguir.')
        else:
            extrato['Total'] = money - quantia
            extrato['Extrato'].append(f'- R${quantia}.00')
    else:
        print('Limite de saque de R$500.00, tente novamente com um valor menor.')


_ = True
saques = 0
while _:
    print('-'*35)
    choice = input('Qual operação você deseja realizar? \n[1]Deposito \n[2]Saque \n[3]Extrato \n[4]Sair \n')
    if choice == '1':
        system('cls')
        deposito(extrato)
    elif choice == '2':
        system('cls')
        if saques >= 3:
            print('Limite de saques diario excedidos, tente novamente amanhã.')
        else:
            saque(extrato)
        saques += 1
    elif choice == '3':
        system('cls')
        print('Ações realizadas na conta: ')
        for i in extrato['Extrato']:
            print(i)
        print(f'Seu total é de R${extrato["Total"]}.00')
        
    elif choice == '4':
        system('cls')
        print('Até logo!')
        _ = False
    else:
        system('cls')
        print('Insira algo valido!')