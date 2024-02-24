

import math
from typing import List, Union


def minimum(a: int, b: int, c: int) -> int:
    if (a <= b and a <= c):
        return a
    elif (b <= a and b <= c):
        return b
    else:
        return c


print('--task 1: ', minimum(11, 11, 34))

print('--task 2: ', minimum(minimum(5, 2, 8),
      minimum(12, 111, 9), minimum(4, 7, 3)))


def distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))


print('--task 3: ', distance(2, 3, 6, 9))


def is_prime(n: int) -> bool:
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
        return True


print('--task 4: ', is_prime(8))


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


print('--task 5: ', fib(7))


def closest_mod_5(x: int) -> int:
    y = x % 5
    if (y) == 0:
        return x
    return x + (5 - y)


print('--task 6: ', closest_mod_5(6))


def modify_list(some_list: List[int]):
    new_list = []
    for num in some_list:
        if num % 2 == 0:
            new_list.append(num // 2)

    some_list.clear()
    some_list.extend(new_list)


list = [22, 21, 24, 25, 26, 27, 30, 31, 32]
print('--task 7 before: ', list)
modify_list(list)
print('--task 7 after: ', list)


def find_min_num(list1: List[int], list2: List[int]) -> Union[int, bool]:
    filtered_list = [num for num in list1 if num not in list2]

    if (filtered_list):
        return min(filtered_list)
    else:
        return False


list1 = [1, 5, 3, 8, 2]
list2 = [1, 7, 2, 9]
print('--task 9: ', find_min_num(list1, list2))


def insert_reverse(numbers: List[int]) -> List[str]:
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(str(num))
            result.append(str(str(num)[::-1]))
        else:
            result.append(str(num))
    return result


numbers = [13, 14, 15, 16]
print('--task 10: ', insert_reverse(numbers))
