
print("--task 1")

print(17/2*3+2)
print(2+17/2*3)
print(19 % 4+15/2*3)
print(15+6-10*4)
print(17/2 % 2*3**3)


print("--task 2")
# WTF? с таска 1 ?


print("--task 3")
print(11-1.5*3)


print("--task 4")
quantity_1 = 2
quantity_2 = 5
print(quantity_1 + quantity_2)


print("--task 5")
days = 5
print(f"{days} суток = {days * 24} часов {days * 24 * 60} минут {days * 24 * 60 * 60} секунд")

print("--task 6")
total_days = 182
print(f"Прошло {total_days // 7} полных недель")

print("--task 7")
side_1 = 150
side_2 = 65  # autocorrect autopep8
square_side = 30

rectangle_area = side_1 * side_2
square_area = square_side * square_side

print(f"Можно отрезать {rectangle_area//square_area} квадратов")

print("--task 8")
seconds = 4000

hours = seconds // 3600
remaining_seconds = seconds % 3600
minutes = remaining_seconds // 60
remaining_seconds = remaining_seconds % 60

print(f"{hours} час")
print(f"{minutes} минут")
print(f"{remaining_seconds} секунд")

print("--task 9")
cash = 361

hundred = cash // 100
remaining_cash = cash % 100

fifty = remaining_cash // 50
remaining_cash = remaining_cash % 50

ten = remaining_cash // 10
remaining_cash = remaining_cash % 10

one = remaining_cash // 1

print(f"{hundred} купюры по 100 рублей")
print(f"{fifty} купюры по 50 рублей")
print(f"{ten} купюры по 10 рублей")
print(f"{one} купюры по 1 рублю")


print("--task 10")

h = 10
x = 2
y = 1

"""
При условии, что начинает ползти с самого низа в начале дня
"""

days = h // (x-y)
remaining_days = h % (x-y)

print(f"Всего {days + remaining_days } дней")


print("--task 11")

mkad = 56
V = 90
T = 0
M = 34

total_time = T + M / 60
distance = V * total_time
position = distance % mkad

print(
    f"Байкер остановится на ометке {position} или на отметке {mkad - position}")
