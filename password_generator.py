import secrets
import string

password_result = []

class password:
    def __init__(self, length: int, characters: str) -> None:
        self.length = length
        self.characters = characters

    def generate(self, iterations):
        for p in range(iterations):
            password: str = ''
            for c in range(self.length):
                password += secrets.choice(self.characters)
            password_result.append(password)
        return password_result

    def result(self, num) -> None:
        return password_result[num]

var = password(20, 'abcdefghijklmnopqrstuvwxyz0123467589')
print(var.generate(3))

print(var.result(1))
