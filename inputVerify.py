import phonenumbers
import re
from datetime import datetime

def getInput(prompt, validation=None, errorMensage='Entrada invalida, por favor tente novamente'):
    while True:
        userInput = input(prompt)
        if not validation or validation(userInput):
            return userInput
        print(errorMensage)

def isdate(args):
    maxAge = 120
    _pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    if not re.match(_pattern, args):
        return False
    try:
        date = datetime.strptime(args, "%d/%m/%Y")
        if date > datetime.now():
            return False
        
        if date < datetime.now().replace(year=datetime.now().year - maxAge):
            return False
        return True
    except:
        return False

def noneWord(args):
    return bool(args.strip())

def isEmail(email):
    def _reEmail(email):
        _pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(_pattern, email) is not None
    if _reEmail(email):
        return True
    else:
        return False

def celVerify(args, zipCode='+55'):
    try:
        _celphone = phonenumbers.parse(zipCode + args, None)
        if not phonenumbers.is_valid_number(_celphone):
            print('numero invalido')
            return False
        return True
    except phonenumbers.NumberParseException as e:
        print('erro ao tentar validar o numero \n pode haver numeros faltando, ou caracteres invalidos.')
        return False
    
    
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

    