import inputVerify
from util import bank_code
def _cadastrar():
    name = inputVerify.getInput('Digite o nome: ', inputVerify.noneWord, 'Voce nao digitou um nome')
    birthday = inputVerify.getInput('Digite a data de nascimento: ', inputVerify.isdate, 'Voce nao digitou uma data de nascimento valida')
    email = inputVerify.getInput('Digite o email: ', inputVerify.isEmail, 'Voce nao digitou um email valido')
    gender = inputVerify.getInput('Digite o genero (M/F): ', inputVerify.noneWord, 'Voce nao digitou um genero')
    address = inputVerify.getInput('Digite o endereco: ', inputVerify.noneWord, 'Voce nao digitou um endereco')
    cel = inputVerify.getInput('Digite o numero de celular: ', inputVerify.celVerify, 'Voce nao digitou um numero valido')
    cpf = inputVerify.getInput('Digite o CPF ', inputVerify.validar_cpf, 'Voce nao digitou um cpf valido')
    return {'Nome': name.replace(' ', '_').title(), 'DataAniversario': birthday, 'genero': gender, 'Endereco': address, 'Telefone': cel, 'Email': email, 'CPF': cpf}

def _criar_conta():
    pessoa = _cadastrar()
    agencia = 9384
    numero = bank_code(12)
    numero_verificacao = bank_code(2)
    pessoa.update({
        'Agencia': agencia,
        'Numero_da_conta': numero,
        'Numero_de_verificacao': numero_verificacao
    })
    return pessoa

def salvar_conta(lista):
    dicionario = _criar_conta()
    return lista.append(dicionario)