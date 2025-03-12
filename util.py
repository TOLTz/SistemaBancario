from datetime import datetime
import random
import string

def dataFormatada():
    data = datetime.today()
    return data.strftime('%d/%m/%Y %H:%M:%S')

def generate_code():
    numbers = ''.join(random.choices(string.digits, k=6))  # Gera 6 números
    letter = random.choice(string.ascii_uppercase)  # Gera uma letra maiúscula
    return numbers + letter
