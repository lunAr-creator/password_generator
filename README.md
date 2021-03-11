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
from pass_gen import simplepass

'''
the int '20' represents password length and the alphabet + numbers
represent the characters the password will be produced from
'''
var = simplepass(20, 'abcdefghijklmnopqrstuvwxyz0123467589')

'''
the int '3' represents the number of passwords the program will output
'''
var.generate(3)
```

#### Output (Please note that output varies depending on arguements provided)

```python
pridxzc291n8h2d2hrs9
lcczdyyv3mo22am1zg69
kudkbgzfe1qpewyp7o71
```

### Complex passwords (More Arguements)

```python
from pass_gen import complexpass

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
NA3beANS3ENLozf4bOtY
sf578TVh5QIoMCPkmoOF
hl6xQPVSsk4YJfkezA66
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
https://opensource.org/licenses/MIT

## PYPI page:
IT IS NOT YET PUBLISHED ON PYPI
