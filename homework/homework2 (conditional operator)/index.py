print("--task 1")

number = 13
print(number % 10 == 3)

print("--task 2")

input = input("Введите три числа через пробел: ")
A, B, C = input.split()
print(int(A) < 0 or int(B) < 0 or int(C) < 0)


print("--task 3")

n1, k1 = 2, 4
n2, k2 = 3, 8
n3, k3 = 11, 3

print(f"Для {n1} и {k1}: {n1 % 2 == k1 % 2}")
print(f"Для {n2} и {k2}: {n2 % 2 == k2 % 2}")
print(f"Для {n3} и {k3}: {n3 % 2 == k3 % 2}")

print('--task 4')

input = int(input("Введите число X: "))
result = input % 3 == 0 and input % 10 == 5

if result:
    print(result)

print('--task 5')

number_t5 = 44

tens = number_t5 // 10
ones = number_t5 % 10
sum = tens + ones

if 10 <= sum <= 99:
    print("Да")
else:
    print("Нет")


print('--task 6')

number_t6 = 4444

thousands = number_t6 // 1000
hundreds = (number_t6 % 1000) // 100
tens = (number_t6 % 100) // 10
ones = number_t6 % 10

result = thousands == hundreds == tens == ones


print('--task 7')
a = 1
b = 17
c = 9

if a >= b and a >= c:
    max_number = a
elif b >= a and b >= c:
    max_number = b
else:
    max_number = c

print(f"max_number: {max_number}")


print('--task 8')

year = int(input('Введите год: '))

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print('Високосный')
else:
    print('Не Високосный')

print('--task 9')

x1 = 4
y1 = 4
x2 = 7
y2 = 8

is_one_color = (x1 + y1) % 2 == (x2 + y2) % 2

if (is_one_color):
    print('Один цвет')
else:
    print('Разные цветв')


print('--task 10')


x1 = 3
y1 = 3
x2 = 7
y2 = 7

is_danger = x1 == x2 or y1 == y2 or (
    x1 - x2 == y1 - y2) or (x1 - x2 == y2 - y1)

if (is_danger):
    print('Угрожает')
else:
    print('Не угрожает')
