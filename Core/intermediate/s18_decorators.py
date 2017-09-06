from functools import wraps


def wrapper(item):
    def _wrapped_item():
        return "a box of {}".format(str(item()))
    return _wrapped_item


def wrapper2(style):
    def _wrapper(item):
        @wraps(item)
        def wrapped_item():
            return "a {} box of {}".format(style, str(item()))
        return wrapped_item
    return _wrapper


@wrapper
def new_gpu(): return "a new GPU"

print(new_gpu())
print(new_gpu.__name__)


@wrapper
@wrapper
def new_bicycle(): return "a new bicycle"

print(new_bicycle())


@wrapper2("nice")
@wrapper2("big")
def new_toy(): return "a new toy"

print(new_toy())
print(new_toy.__name__)