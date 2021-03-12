# password_generator

```password_generator``` is a library for dealing with generating secure randomised passwords that are customisable and strong simultaneously.

## Installation

Use the package manager [pip]() to install password_generator.

```bash
(library is not yet published on pypi)
```
<br></br>
## Usage
### Simple passwords (Less Arguements)
```python
from password_generator import simple

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
from password_generator import complex

var = complex(20, 'both', True, False)

print(var.generate(3))
print(var.result(1))
```

#### Output (Please note that output varys depending on arguements provided)

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
Example:

```python
from password_generator import simple

var = simple(20, 'abcdfghijklmnopqrstuvwxyz0123456789')
```

Now for the second way option. To create a "complex" password we must give the object 4 parameters: password length, string method (lowercase, uppercase or both), numbers (True or False) and special characters (True or False)
<br></br>
Example:

```python
from password_generator import complex

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
from password_generator import simple

var = simple(20, 'abcdfghijklmnopqrstuvwxyz0123456789')

# Generating password

var.generate(3) # Will generate 3 invisble passwords
print(var.generate(3)) # Will generate 3 visible passwords
```

Example 2:
```python
from password_generator import complex

var = complex(20, 'both', True, False)

# Generating password

var.generate(3) # Will generate 3 invisble passwords
print(var.generate(3)) # Will generate 3 visible passwords
```
</details>

<details>
<summary>Getting specific passwords from the list of generated passwords</summary>
<br>
Blank
</details>

<details>
<summary>Hashing a password</summary>
<br>
Blank
</details>

<details>
<summary>Verifying a hashed password</summary>
<br>
Blank
</details>

<br></br>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
https://opensource.org/licenses/MIT

## PYPI page:
(library is not yet published on pypi)
