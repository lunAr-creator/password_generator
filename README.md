# password_generator

```password_generator``` is a library for dealing with generating secure randomised passwords that are customisable and strong simultaneously.

## Installation

Use the package manager [pip]() to install password_generator.

```bash
IT IS NOT YET PUBLISHED ON PYPI
```

## Usage
### Simple passwords (Less Arguements)
```python
from passwprd_generator import password

'''
the int '20' represents password length and the alphabet + numbers
represent the characters the password will be produced from
'''
var = simplepass(20, 'abcdefghijklmnopqrstuvwxyz0123467589')

'''
the int '3' represents the number of passwords the program will output
'''
var.generate(3) # This wull generate a password that is invisible (you cant see it as an output)
print(var.generate(3)) # This will generate a password that is visible (as part of a list)

'''
Reference passwords using result
'''
print(result[1]) # Will print the second password
```

#### Output (Please note that output varies depending on arguements provided)

```python
['mr3s7swtr1k0l6as2m9a', 'b6uev6v4dhcbrptj0i89', 'q7gy2xm6szpyj1snbmz6']
b6uev6v4dhcbrptj0i89
```

### Complex passwords (More Arguements)

```python
from password_generator import complex

'''
the int '20' represents password length, 'both' represents lower and uppercase
letters (can be just 'lower' or 'upper'), 1st 'True' corresponds with digits (can be 'False')
and 'False' stands for special characters (can be 'True')
'''

var = complexpass(20, 'both', True, False)

'''
the int '3' represents the number of passwords the program will output
'''
var.generate(3)

```

#### Output (Please note that output varys depending on arguements provided)

```python

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
https://opensource.org/licenses/MIT

## PYPI page:
IT IS NOT YET PUBLISHED ON PYPI
