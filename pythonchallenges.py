import random
import string

def generate_random_password(length):
    if length < 4:  
        raise ValueError("Password length should be at least 4")

   
    lowercase = random.choices(string.ascii_lowercase, k=length // 3)
    uppercase = random.choices(string.ascii_uppercase, k=length // 3)
    digits = random.choices(string.digits, k=length - len(lowercase) - len(uppercase))


    password = lowercase + uppercase + digits


    random.shuffle(password)

    
    return ''.join(password)


password_length = 12
password = generate_random_password(password_length)
print("Generated Password:", password)
