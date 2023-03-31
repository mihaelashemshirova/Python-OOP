from typing import Dict


class Cached:

    def __init__(self, func):
        self.func = func
        self.cache: Dict = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result


@Cached
def example(x):
    result = x ** 2 + 3 * x + 1
    return result


print(example(2))  # slow
print(example(2))  # fast
print(example(3))  # slow
print(example(3))  # fast
