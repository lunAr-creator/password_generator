import secrets
import string

class simplepass:
    def __init__(self, length, characters):
        self.length = length
        self.characters = characters

    def generate(self, iterations):
        for p in range(iterations):
            output_password = ''
            for c in range(self.length):
                output_password += secrets.choice(self.characters)
            print(output_password)

class complexpass(simplepass):
    def __init__(self, length, string_method, numbers=True, special_chars=False):
        self.length = length
        self.string_method = string_method
        self.numbers = numbers
        self.special_chars = special_chars

    def generate(self, iterations):
        characters = ''

        methods = {
            'upper': string.ascii_uppercase,
            'lower': string.ascii_lowercase,
            'both': string.ascii_letters
        }

        characters += methods[self.string_method]

        if self.numbers:
            characters += string.digits
        if self.special_chars:
            characters += string.punctuation

        for p in range(iterations):
            output_password = ''
            for c in range(self.length):
                output_password += secrets.choice(characters)
            print(output_password)

# Test

if __name__ == '__main__':
    var1 = complexpass(20, 'both', True, False)
    var1.generate(3)

    var2 = simplepass(20, 'abcdefghijklmnopqrstuvwxyz0123467589')
    var2.generate(3)
