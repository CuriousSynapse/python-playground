import secrets
import string

def generate_password(length = 16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 2):
            return password

new_password = generate_password()
print(f"Your new password is: {new_password}")