def even_parameters(func):

    def wrapper(*args):
        for arg in args:
            if isinstance(arg, int):
                if arg % 2 == 0:
                    continue

            return "Please use only even numbers!"

        return func(*args)

    return wrapper


@even_parameters
def func(*args):
    return sum(args)


result = func(4, 4, 4)
print(result)
