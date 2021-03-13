# pw-gen

```pw-gen``` is a library for dealing with generating secure randomised passwords that are customisable and strong simultaneously.

## Installation

Use the package manager [pip](https://pypi.org/project/pip/) to install pw-gen.

```bash
pip install pw-gen
```
<br></br>
## Usage
### Simple passwords (Less Arguements)
```python
from pw_gen import simple

var = simple(20, 'abcdefghijklmnopqrstuvwxyz0123467589')

print(var.generate(3))
print(var.result(1))
```

#### Output (Please note that output varies depending on arguements provided)

```
['mr3s7swtr1k0l6as2m9a', 'b6uev6v4dhcbrptj0i89', 'q7gy2xm6szpyj1snbmz6']
b6uev6v4dhcbrptj0i89
```

### Complex passwords (More Arguements)

```python
from pw_gen import complex

var = complex(20, 'both', True, False)

print(var.generate(3))
print(var.result(1))
```

#### Output (Please note that output varies depending on arguements provided)

```
['kQ6rbCxq1l7roGlJ5AUs', '0CXTxSWyXdPg3aZkjt7B', 'l4RY1CeRpARqX2uaQGtC']
0CXTxSWyXdPg3aZkjt7B
```
<br></br>
## Creating passwords - In depth

<details>
<summary>Creating a password</summary>
<br>
To customise and generate our password we must first create an instance of our password.

This can be done with either a "simple" password or a "complex" password. Simple passwords can be created by making a "simple" object and assigning 2 parameters: 1 of which is password length, the other is the characters that will be randomised to create it.
<br>  
Example 1:

```python
from pw_gen import simple

var = simple(20, 'abcdfghijklmnopqrstuvwxyz0123456789')
```

Now for the second way option. To create a "complex" password we must give the object 4 parameters: password length, string method (lowercase, uppercase or both), numbers (True or False) and special characters (True or False)
<br></br>
Example 2:

```python
from pw_gen import complex

var = complex(20, 'both', True, False)
```

</details>

<details>
<summary>Generating a password(s)</summary>
<br>
To generate a password we have to use the 'generate' method with our object. The generate method requires one parameter: iterations. Iterations refers to the number of passwords the program will output (these will all be different). Furthermore, you can either create invisible passwords (will not print the passwords out) or visible passwords (are visible when running the program). The 'generate' method can be used for both 'simple' and 'complex' passwords.
<br></br>

Example 1:

```python
from pw_gen import simple

var = simple(20, 'abcdfghijklmnopqrstuvwxyz0123456789')

# Generating password

var.generate(3) # Will generate 3 invisble passwords
print(var.generate(3)) # Will generate 3 visible passwords
```

Example 2:
```python
from pw_gen import complex

var = complex(20, 'both', True, False)

# Generating password

var.generate(3) # Will generate 3 invisble passwords
print(var.generate(3)) # Will generate 3 visible passwords
```
</details>

<details>
<summary>Getting a specific password from the ones generated</summary>
<br>
If you have seen the code for this library already, you will probably know that the output passwords are appended to a list as they are created. This means that
there will be a list containing a 'iteration' number of passwords. Therefore, we can get a specific password from this list using the 'result' method. It takes one parameter: the index of the password. For instance, if I generated 3 passwords, then the index of the second password would be '1'. Therefore, we can get the second output like so:
<br></br>

```python
var.result(1) # Invisible: will not print out anything
print(var.result(1)) # Visible: will print out
```

Output:

```
['ce08vizthnu6qjkvn092', 'aorhkux4h1nzv4dt9r12', '2vy3w83a14uvja0uye7k']
aorhkux4h1nzv4dt9r12
```

Full example:

```python
from pw_gen import simple

var = simple(20, 'abcdfghijklmnopqrstuvwxyz0123456789')

# Generating password

var.generate(3) # Will generate 3 invisble passwords
print(var.generate(3)) # Will generate 3 visible passwords

print(var.result(1)) # Visible: will print out
```

</details>

<details>
<summary>Hashing a password</summary>
<br>
Hashing a password is very important. If you are storing passwords in files, databases etc it should be the upmost priority to keep password safe from being stolen and then used. A way to prevent this is using hashing. Whilst hackers might still steal it, it would be impossible to reverse engineer a hashed password, meaning that the original password will be safe. We can use the function 'hash' to hash a password. The hash function takes one argument: the password to hash.
<br></br>
For example:
<br></br>

```python
from pw_gen import simple, hash

#Creating a password
var = simple(20, 'abcdefghijklmnopqrstuvwxyz0123467589')

# Generating a password
print(var.generate(3))

# We get the password using the 'result' method I covered earlier.
hashed_password = hash(var.result(1))
print(hash(hashed_password)) # print the result of the hashed password
```

Output:

```
71bfc946b8d90390fe1879e604a3dbe3f38d16b45d6a4a81de9b3e6085d08ca6956098627c09ef471ac5597955ab860e290dde7feee334f4efa5c235ecb99588d5658b6cd62f30bb5d62050c3bdcd93a6e6319e94d6714d55f997caa8dd34a2d
```
</details>

<details>
<summary>Comparing a hashed password to the original</summary>
<br>
Previously, we talked about how to hash a password. Now, we are going to discuss how to verify a hashed password. What is mean is, comparing a hashed password to one that the user provides, and check if the given password is equal to the hashed one. We can do this using the 'varify_hash' function. We
<br></br>

Example:

```python
from pw_gen import simple, hash, verify_hash

# Create a new password
var = simple(20, 'abcdefghijklmnopqrstuvwxyz0123467589')

# Generate new passwords
print(var.generate(3))

# Select a password and print it
print(var.result(1))

# Hash the password we have selected
stored_password = hash(var.result(1))
print(stored_password)

# Have user input for a password, if it is equal to the hashed password then print('The password is correct')
p = input('Password: ')
if verify_hash(stored_password, p) == True:
    print('The password is correct')
```

<br></br>

Output:

```
['ce08vizthnu6qjkvn092', 'aorhkux4h1nzv4dt9r12', '2vy3w83a14uvja0uye7k']
aorhkux4h1nzv4dt9r12
44bba1d156ace3ce5447a43d4c83b8a88947cd610ccfc48366003b67a3729d81216752948958e3074c33f789db27fb359775dc07bcb176db9b7a99237995eb029b9e509ba003d7e259465aa02db888e9b31f84bc3c3e7fa507bb481e48b6f7e8
Password: aorhkux4h1nzv4dt9r12
The password is correct
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
