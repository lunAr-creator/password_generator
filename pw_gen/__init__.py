import random
import secrets
import string
import urllib.request

password_result = []

class Simple:
    def __init__(self, length: int, characters = None) -> None:
        self.length = length
        self.characters = characters

    def generate(self, num_of_passwords: int):
        characters = ''

        if self.characters is None:
            characters = string.ascii_letters + string.digits
        if self.characters is not None:
            characters = self.characters

        password_result.clear()
        for p in range(num_of_passwords):
            password: str = ''
            for c in range(self.length):
                password += secrets.choice(characters)
            password_result.append(password)
        return password_result

    def result(self, num: int) -> None:
        return password_result[num]

class Complex(Simple):
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

class Memorable(Complex):
    def __init__(self, numbers=True):
        self.numbers = numbers

    def generate_memorable(self, num_of_passwords):
        word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        req = urllib.request.Request(word_url, headers=headers)
        response = response = urllib.request.urlopen(req)
        long_txt = response.read().decode()
        words = long_txt.splitlines()

        password_result.clear()
        for i in range(num_of_passwords):
            password = ''
            two_words = ''
            for i in range(2):
                two_words += secrets.choice(words).title()
            password = two_words
            if self.numbers == True:
                for i in range(random.randint(3, 4)):
                    password += secrets.choice(string.digits)
            password_result.append(password)
        return password_result
