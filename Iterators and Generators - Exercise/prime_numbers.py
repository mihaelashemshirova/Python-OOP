from typing import List


def get_primes(numbers: List[int]):
    for number in numbers:
        if number <= 1:
            continue
        
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            yield number
