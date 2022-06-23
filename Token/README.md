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