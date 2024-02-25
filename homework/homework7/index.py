from typing import List
import time

print('--task 1: ', [num for num in range(11, 100, 2)])

print('--task 2: ', [num**2 for num in range(1, 11)])

print('--task 3: ', [num for num in range(100, 1000)
      if num % 3 == 0 or num % 5 == 0])

# start task 4


def get_count_unique_elems(list: List[int]) -> int:
    count = 0
    prev_elem = None

    for elem in list:
        if prev_elem != elem:
            count += 1
        prev_elem = elem

    return count


print('--task 4: ',
      get_count_unique_elems([1, 2, 2, 3, 3, 'str', 'str', False]))

# end task 4


# start task 5
input5 = '10 2'
numbers5 = [int(num) for num in input5.split()]


def sum_adjacent_numbers(numbers: List[int]) -> str:
    length = len(numbers)
    result = []

    if (length == 1):
        result.append(numbers[0])
    else:
        for k in range(length):
            if (k == 0):
                result.append(numbers[k+1] + numbers[length - 1])
            elif (k == (length - 1)):
                result.append(numbers[0] + numbers[k - 1])
            else:
                result.append(numbers[k-1] + numbers[k+1])

    return result


print('--task 5: ', " ".join(map(str, sum_adjacent_numbers(numbers5))))
# end task 5


# start task 6
list6 = [1, 'str', 'str', False, 3, None, None, 5, 'str2', 7]
doubled_list6 = [num for num in list6 if list6.count(num) == 1]
print('--task 6: ', doubled_list6)

# end task 6


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        _time = end_time - start_time

        print(f"elapsed time ({func.__name__}): {_time:.0f} sec" if func.__name__ ==
              'registration' else f"elapsed time ({func.__name__}): {_time:.10f} sec")

        return result

    return wrapper

# start task 8


@timing_decorator
def registration():
    username = input("entry name: ")
    email = input("entry email: ")
    password = input("entry password: ")

    print("registration completed")


registration()
# end task 8

# start task 7


def is_prime(num: int) -> bool:
    if num == 0:
        return False
    if num == 1:
        return True
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                return False
        else:
            return True


@timing_decorator
def get_primes(start: int, end: int) -> List[int]:
    primes = []
    for num in range(start, end + 1):
        if (is_prime(num)):
            primes.append(num)
    return primes


print('--task 7, primes: ', get_primes(0, 100))
# end task 7


# start task is_power
def is_power(n: int) -> bool:
    if n == 1:
        return True
    elif n % 2 == 0:
        return is_power(n // 2)
    else:
        return False


print('--is_power: ', is_power(1))
# end task is_power

# Сгенерировать список всех простых чисел до  100 с помощью генератора.
primes = (num for num in range(0, 100) if is_prime(num))
print('--prime list: ', list(primes))
