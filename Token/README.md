## Flask 
Different methods to use validation in flask token

## Use Of Decorater [link](https://www.freecodecamp.org/news/python-decorators-explained-with-examples/)

Here is the syntax for a basic Python decorator:

```
def my_decorator_func(func):

    def wrapper_func():
        # Do something before the function.
        func()
        # Do something after the function.
    return wrapper_func
```
To use a decorator ,you attach it to a function like you see in the code below. We use a decorator by placing the name of the decorator directly above the function we want to use it on. You prefix the decorator function with an @ symbol.
```
@my_decorator_func
def my_func():

    pass
```

## Functools wraps :-
It will update the decorator with the decorated functions attributes.

```
from functools import wraps

def my_decorator_func(func):

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func

@my_decorator_func
def my_func(my_args):
    '''Example docstring for function'''

    pass
```


## Calling file from different folder

By default, you can't. When importing a file, Python only searches the directory that the entry-point script is running from and sys.path which includes locations such as the package installation directory 

1. To check the available paths

```
import sys
print(sys.path)
```

2. Append the path in which your file is present (This method is not the correct to solve the issue)

```
import sys 
sys.path.append('/home/amitej/Learning/Flask/Token/sqlite3_token_gen')
print(sys.path)
```

3. Now simply call the file name as you call normally

```
from file_name import func_name or class_name
```

4. You can also make a empty ```__int__.py``` file in the directory where the file is located.

5. ```__init__.py``` will make the directory to act like a package and then we can call it in a simple way.