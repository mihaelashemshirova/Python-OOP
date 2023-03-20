from collections import deque


def custom_reduce(func, elements):
    elements = deque(elements)

    arguments_count = func.__code__.co_argcount

    while len(elements) > 1:
        arguments = [elements.pop() for _ in range(arguments_count)]
        elements.appendleft(func(*arguments))

    return elements[0]


print(custom_reduce(lambda a, b: a + b, [1, 2, 3, 4]))
