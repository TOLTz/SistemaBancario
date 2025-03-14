pessoas = [
    {
        'Nome': 'João_Silva',
        'DataAniversario': '15/03/1990',
        'genero': 'Masculino',
        'Endereco': 'Rua das Flores, 123, São Paulo, SP',
        'Telefone': '(11) 98765-4321',
        'Email': 'joao.silva@email.com',
        'CPF': '123.456.789-00',
        'agencia': 10, 
        'Numero': 10, 
        'Verificacao': 10
    },
    {
        'Nome': 'Maria_Ferreira',
        'DataAniversario': '22/07/1985',
        'genero': 'Feminino',
        'Endereco': 'Avenida Brasil, 456, Rio de Janeiro, RJ',
        'Telefone': '(21) 91234-5678',
        'Email': 'maria.ferreira@email.com',
        'CPF': '987.654.321-00',
        'agencia': 20, 
        'Numero': 20,
        'Verificacao': 20
    }
]

def login(pessoas):
    while True:
        try:
            agencia = int(input('Agência: '))
            n_conta = int(input('Número da conta: '))
            n_verificacao = int(input('Número de verificação: '))

        
            encontrado = False
            for pessoa in pessoas:
                if (pessoa['agencia'] == agencia and 
                    pessoa['Numero'] == n_conta and 
                    pessoa['Verificacao'] == n_verificacao):
                    encontrado = True
                    print(f'Bem vindo! Senhor(a) {pessoa['Nome'].replace("_", ' ')}')
                    return True
            
            if not encontrado:
                print('Você digitou algo errado.')

        except ValueError:
            print("Por favor, digite apenas números.")
login(pessoas)