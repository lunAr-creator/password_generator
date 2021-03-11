import secrets
import string

result = []

class password:
    def __init__(self, length: int, characters: str) -> None:
        self.length = length
        self.characters = characters

    def generate(self, iterations):
        for p in range(iterations):
            password: str = ''
            for c in range(self.length):
                password += secrets.choice(self.characters)
            result.append(password)
        return result

var = password(20, 'abcdefghijklmnopqrstuvwxyz0123467589')
print(var.generate(2))

print(result[0])
