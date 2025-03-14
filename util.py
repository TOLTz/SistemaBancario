from datetime import datetime
import random
import string

def dataFormatada():
    data = datetime.today()
    return data.strftime('%d/%m/%Y %H:%M:%S')

def generate_code():
    numbers = ''.join(random.choices(string.digits, k=6))
    letter = random.choice(string.ascii_uppercase)
    return numbers + letter

def bank_code(num):
    numbers = ''.join(random.choices(string.digits, k=num))
    return numbers
