import secrets
import string

class simplepass:
    def __init__(self, length: int, characters: str) -> None:
        self.length = length
        self.characters = characters

    def generate(self, iterations: int):
        '''
        Generates a password depending on length, given characters and iterations.
        Uses 2 for loops to achieve this
        '''
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

        '''
        Generates a string for the var characters that is used to make
        a password depending on length, upper of lowercase, digits, special
        characters and iterations. Uses 2 for loops to achieve this.
        '''

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

        super().__init__(length=length, characters=characters)

# Tests

if __name__ == '__main__':
    # Generate a complex password

    var1 = complexpass(20, 'both', True, True)
    var1.generate(3)

    # Generate a simple password

    var2 = simplepass(20, 'abcdefghijklmnopqrstuvwxyz0123467589')
    var2.generate(3)
