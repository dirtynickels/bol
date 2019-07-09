import inspect
def checkargs(function):
    def _f(*arguments):
        for index, argument in enumerate(inspect.getfullargspec(function)[0]):
            if not isinstance(arguments[index], function.__annotations__[argument]):
                raise TypeError("{} is not of type {}".format(arguments[index], function.__annotations__[argument]))
        return function(*arguments)
    _f.__doc__ = function.__doc__
    return _f

if __name__ == "__main__":
    #@checkargs
    def num_test(a: float, d: float = 0.0) -> int:
        assert isinstance(a, float)
        assert isinstance(d, float)
        b = a + d
        print(type(a))
        print(type(d))
        return b


    print(inspect.getfullargspec(num_test))
    print(num_test(8.0, 10.0))