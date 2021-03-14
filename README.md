# pw-gen

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
from pw_gen import simple

var = simple(20, 'abcdefghijklmnopqrstuvwxyz0123467589')

print(var.generate(3))
print(var.result(1))
```

#### Output (Please note that output varies depending on arguments provided)

```
['mr3s7swtr1k0l6as2m9a', 'b6uev6v4dhcbrptj0i89', 'q7gy2xm6szpyj1snbmz6']
b6uev6v4dhcbrptj0i89
```

### Complex passwords (More Arguments)

```python
from pw_gen import complex

var = complex(20, 'both', True, False)

print(var.generate(3))
print(var.result(1))
```

#### Output (Please note that output varies depending on arguments provided)

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

var = Simple(20, 'abcdfghijklmnopqrstuvwxyz0123456789')

#or

var = Simple(20) 

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

<br></br>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
https://opensource.org/licenses/MIT

## PYPI page:
https://pypi.org/project/pw-gen/
