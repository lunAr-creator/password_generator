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

class complex(password):
    def __init__(self, length, string_method, numbers=True, special_chars=False):
        characters = ''

        methods: dict = {
            "upper": string.ascii_uppercase,
            "lower": string.ascii_lowercase,
            "both": string.ascii_letters,
        }

        characters += methods[string_method]

        if numbers:
            characters += string.digits
        if special_chars:
            characters += string.punctuation

        super().__init__(length=length, characters=characters)

if __name__ == "__main__":
    var = password(20, 'abcdefghijklmnopqrstuvwxyz0123467589')
    print(var.generate(3))

    print(var.result(1))

    # NOTE TO SELF: COMPLEX IS PRODUCING DOUBLE THE IERATION OF PASSWORDS. FIX THIS!!!!

    var1 = complex(20, "both", True, True)
    print(var1.generate(3))

    print(var1.result(1))
