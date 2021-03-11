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

    def clear_results(self) -> None:
        password_result.clear()


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

# Test scenarios

if __name__ == "__main__":

    # Generate 3 simple passwords
    var = password(20, 'abcdefghijklmnopqrstuvwxyz0123467589')
    print(var.generate(3))

    # Print the 2nd result out of the 3 passwords generated above
    print(var.result(1))

    #Clear the result so that the list of passwords is clear
    var.clear_results()
