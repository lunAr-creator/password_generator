import string
import secrets

from typing import List, Union


class simplepass:
    def __init__(self, length: int, characters: str) -> None:
        self.length: int = length
        self.characters: str = characters

    def generate(self, iterations: int = 1) -> Union[str, List[str]]:
        """returns one or multiple passwords,
        depending on length, given characters and iterations.

        Args:
            iterations (int): how many passwords to return

        Returns:
            Union[str, List[str]]: one or multiple passwords
        """
        if iterations == 1:
            return self._gen_pw()
        else:
            return [self._gen_pw() for _ in range(iterations)]

    def _gen_pw(self) -> str:
        """returns a password depending on lenght and given caracters

        Returns:
            str: a randomly generated password
        """
        output_password: str = ""
        for _ in range(self.length):
            output_password += secrets.choice(self.characters)
        return output_password


class complexpass(simplepass):
    def __init__(
        self,
        length: int,
        string_method: str = "both",
        numbers: bool = True,
        special_chars: bool = False,
    ):
        methods = {
            "upper": string.ascii_uppercase,
            "lower": string.ascii_lowercase,
            "both": string.ascii_letters,
        }
        characters: str = methods[string_method]
        if numbers:
            characters += string.digits
        if special_chars:
            characters += string.punctuation
        super().__init__(length=length, characters=characters)


# Tests
if __name__ == "__main__":
    # Generate a complex password

    cp = complexpass(20, "both", True, True)
    print(cp.generate())
    print(cp.generate(2))
    print(cp.generate(3))

    # Generate a simple password

    sp = simplepass(20, "abcdefghijklmnopqrstuvwxyz0123467589")
    print(sp.generate())
    print(sp.generate(2))
    print(sp.generate(3))

    # Can also be used to generate random binary strings

    sp2 = simplepass(10, "01")
    print(sp2.generate())
    print(sp2.generate(2))
    print(sp2.generate(3))

    # or random hex numbers

    sp3 = simplepass(64, "0123456789abcdef")
    print(sp3.generate())
    print(sp3.generate(2))
    print(sp3.generate(3))
