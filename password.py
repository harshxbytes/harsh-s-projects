import random
import string

class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

if __name__ == "__main__":
    pg = PasswordGenerator(16)  # Default length is 16
    print("Generated Password:", pg.generate_password())

class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def validate(self):
        if len(self.password) < 8:
            return "Password is too short!"
        if not any(char.isdigit() for char in self.password):
            return "Password must contain at least one digit!"
        if not any(char.isupper() for char in self.password):
            return "Password must contain at least one uppercase letter!"
        if not any(char.islower() for char in self.password):
            return "Password must contain at least one lowercase letter!"
        if not any(char in "!@#$%^&*()-_+=" for char in self.password):
            return "Password must contain at least one special character!"
        return "Password is strong!"
import random
import string

class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

if __name__ == "__main__":
    pg = PasswordGenerator(16)  # Default length is 16
    print("Generated Password:", pg.generate_password())
