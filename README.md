# password_generator

```password_generator``` is a library for dealing with generating secure randomised passwords that are customisable and strong simultaneously.

## Installation

Use the package manager [pip]() to install password_generator.

```bash
(library is not yet published on pypi)
```

## Usage
### Simple passwords (Less Arguements)
```python
from password_generator import simple

var = simple(20, 'abcdefghijklmnopqrstuvwxyz0123467589')

print(var.generate(3)) 
print(var.result(1)) 
```

#### Output (Please note that output varies depending on arguements provided)

```python
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
## Creating passwords - In depth
### Creating an object


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
https://opensource.org/licenses/MIT

## PYPI page:
(library is not yet published on pypi)
