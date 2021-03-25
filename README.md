# pw-gen
[![Downloads](https://pepy.tech/badge/pw-gen)](https://pepy.tech/project/pw-gen) ![Version](https://img.shields.io/badge/version-0.0.2-blue)


```pw-gen``` is a library for dealing with generating secure randomised passwords that are customisable and strong simultaneously.

## Installation

Use the package manager [pip](https://pypi.org/project/pip/) to install pw-gen.

```bash
pip install pw-gen
```
<br></br>
## Usage
### Simple passwords (Less Arguments)
```python
from pw_gen import Simple

var = Simple(20)

print(var.generate(3))
print(var.return_result(1))
```

#### Output (Please note that output varies depending on arguments provided)

```
['mr3s7swtr1k0l6as2m9a', 'b6uev6v4dhcbrptj0i89', 'q7gy2xm6szpyj1snbmz6']
b6uev6v4dhcbrptj0i89
```

### Complex passwords (More Arguments)

```python
from pw_gen import Complex

var = Complex(20, 'both', True, False)

print(var.generate(3))
print(var.return_result(1))
```

#### Output (Please note that output varies depending on arguments provided)

```
['kQ6rbCxq1l7roGlJ5AUs', '0CXTxSWyXdPg3aZkjt7B', 'l4RY1CeRpARqX2uaQGtC']
0CXTxSWyXdPg3aZkjt7B
```


### Memorable passwords (Easy to remember)

```python
from pw_gen import Memorable

var = Memorable(True)

print(var.generate(3))
print(var.return_result(1))
```

#### Output (Please note that output varies depending on arguments provided)

```
['DappleStrenuous7169', 'FriedmanAnimal1504', 'PowellBilabial799']
FriedmanAnimal1504
```
<br></br>
## Creating passwords - In depth

<details>
<summary>Creating a password</summary>
<br>
To customise and generate our password we must first create an instance of our password.

This can be done with either a "simple", "complex" or memorable password. Simple passwords can be created by making a "simple" object and assigning 2 parameters: 1 of which is password length, the other is the characters that will be randomised to create it (characters is an optional parameter - you can leave it out and the password will be customised to use ```ascii_letters``` and ```ascii_digits```.
<br>  
Example 1:

```python
from pw_gen import Simple

var = Simple(20, 'abcdfghijklmnopqrstuvwxyz0123456789')

#or

var = Simple(20)
```

Now for the second way option. To create a "complex" password we must give the object 4 parameters: password length, string method (lowercase, uppercase or both), numbers (True or False) and special characters (True or False)
<br></br>
Example 2:

```python
from pw_gen import Complex

var = Complex(20, 'both', True, False)
```

Finally we have the last type of password: memorable. It takes one arguement (numbers) and it is whether to include numbers in the password (this defaults to True but can be changed to false)
<br></br>
Example 3:

```python
from pw_gen import Memorable

var = Memorable() #defaulted to numbers

#or

var = Memorable(False) #no numbers
```

</details>

<details>
<summary>Generating a password(s)</summary>
<br>
To generate a password we have to use the 'generate' method with our object. The generate method requires one parameter: ```num_of_passwords```. ```num_of_passwords``` refers to the number of outputs (these will all be different). Furthermore, you can either create invisible passwords (will not print the passwords out) or visible passwords (are visible when running the program). The 'generate' method can be used for both 'Simple', 'Complex' and 'Memorable' passwords.
<br></br>

Example 1:

```python
from pw_gen import Simple

var = Simple(20, 'abcdfghijklmnopqrstuvwxyz0123456789')

#or

var = Simple(20)

# Generating password

var.generate(3) # Will generate 3 invisble passwords
print(var.generate(3)) # Will generate 3 visible passwords
```

Example 2:
```python
from pw_gen import Complex

var = Complex(20, 'both', True, False)

# Generating password

var.generate(3) # Will generate 3 invisble passwords
print(var.generate(3)) # Will generate 3 visible passwords
```

Example 3:

```python
from pw_gen import Memorable

var = Memorable()

# Generating password

var.generate(3) # Will generate 3 invisble passwords
print(var.generate(3)) # Will generate 3 visible passwords
```

</details>

<details>
<summary>Getting a specific password from the ones generated</summary>
<br>
If you have seen the code for this library already, you will probably know that the output passwords are appended to a list as they are created. This means that
there will be a list containing a 'iteration' number of passwords. Therefore, we can get a specific password from this list using the 'return_result' method. It takes one parameter: the index of the password. For instance, if I generated 3 passwords, then the index of the second password would be '1'. Therefore, we can get the second output like so:
<br></br>

```python
var.return_result(1) # Invisible: will not print out anything
print(var.return_result(1)) # Visible: will print out
```

Output:

```
['ce08vizthnu6qjkvn092', 'aorhkux4h1nzv4dt9r12', '2vy3w83a14uvja0uye7k']
aorhkux4h1nzv4dt9r12
```

Full example:

```python
from pw_gen import Simple

var = Simple(20, 'abcdfghijklmnopqrstuvwxyz0123456789')

# Generating password

var.generate(3) # Will generate 3 invisble passwords
print(var.generate(3)) # Will generate 3 visible passwords

print(var.return_result(1)) # Visible: will print out
```

</details>
<details>
<summary>Deleting the list of output passwords</summary>
<br>

<br></br>
This method is used if you want to clear your output. This is because everytime you generate a type of password, it will append it to a specific list for that type of password. If you would like to generate some new passwords and you want a fresh output, we have to use the ```clear_results``` method. This is entirely optional, if you want to keep appending new passwords to the same list you **can**.

Example of using ```clear_results```:

<br></br>

```python
from pw_gen import Simple

var = Simple(20, 'abcdfghijklmnopqrstuvwxyz0123456789')

# Generating password

print(var.generate(3)) # Will generate 3 visible passwords

print(var.return_result(1)) # Visible: will print out

var.clear_results() # Clear the list of output passwords.
print(var.generate(3)) # Will generate 3 visible passwords

print(var.return_result(1)) # Visible: will print out
```

Output:

```
['v1lt3hqpiz4az2mllq5t', 'xtbfqwsumx3qq0zwub79', 'wbg132by7iruxcit9a0z']
qc3ad5mc9dzpavqkhigy

['1hh294btvap6av5b86pv', 'h7o4qbi3c42hygcujh39', '5s5zq30odlxnufgbxb6m']
h7o4qbi3c42hygcujh39
```

</details>

<br></br>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
https://opensource.org/licenses/MIT

## PYPI page:
https://pypi.org/project/pw-gen/
