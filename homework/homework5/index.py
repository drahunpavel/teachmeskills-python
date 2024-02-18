print("----------task 1")

for _ in range(20):
    print("10")

print("----------task 2")
# number_input2 = int(input("Entry N: "))
number_input2 = 4
cubes_string = ' '.join(str(i ** 3) for i in range(1, number_input2 + 1))
print(cubes_string)


print("----------task 3")
numbers_string3 = ' '.join(str(i) for i in range(100, -101, -1))
print(numbers_string3)


print("----------task 4")
number_input4 = 4
numbers_string4 = ' '.join(str(i)
                           for i in range(number_input4, number_input4*10, 2))
print(numbers_string4)


print("----------task 5")
sum_numbers = 0
for number in range(100, 501):
    sum_numbers += number

print(sum_numbers)


print("----------task 6")
product_numbers = 1
for number in range(5, 21):
    product_numbers *= number

print(product_numbers)


print("----------task 6")
number6 = 4
factorial_result = 1
for i in range(1, number6 + 1):
    factorial_result *= i

print(factorial_result)


print("----------task 7")
number_input7 = 8
sum_numbers7 = 0
i = 0
while i <= number_input7:
    if i % 2 == 0:
        sum_numbers7 += i
    i += 1

print(sum_numbers7)


print("----------task 8")
number_input8 = 6
product_numbers8 = 1
k = 1

while k <= number_input8:
    if k % 2 == 0:
        product_numbers8 *= k
    k += 1

print(product_numbers8)


print("----------task 9")
number_input9 = 100
t = 1
result_arr = []
while t**2 < number_input9:
    result_arr.append(str(t**2))
    t += 1

print('result_arr', result_arr)
print('result_string', ' '.join(result_arr))


print("----------task 10")
number_input10 = 40
idx = 0

while idx < len(result_arr) and int(result_arr[idx]) <= number_input10:
    idx += 1

print(
    f"input: {number_input10}, output: {idx < len(result_arr) and result_arr[idx]}")


print("----------task 11")
number_input11 = 469
# number_str = str(abs(number_input11))
number_str = str(number_input11)
print(number_str[0])
# через while -


print("----------task 12")
number_input12 = 555
number_str12 = str(abs(number_input12))
sum_digits = 0
idx12 = 0
while idx12 < len(number_str12):
    sum_digits += int(number_str12[idx12])
    idx12 += 1

print('sum_digits', sum_digits)


print("----------task 13")
number_input13 = 5391
number_str13 = str(abs(number_input13))
idx13 = 0
min_digit = 9

while idx13 < len(number_str13):
    print(number_str13[idx13])
    if (int(number_str13[idx13]) < min_digit):
        min_digit = int(number_str13[idx13])
    idx13 += 1

print('min_digit', min_digit)


print("----------task 14")
string_input14 = 'sdfdsfz fgzfgfg zz'
result_string14 = ''
idx14 = 0

while idx14 < len(string_input14):
    result_string14 += string_input14[idx14]

    if string_input14[idx14] == 'z':
        result_string14 += '!'

    idx14 += 1

print('result_string14', result_string14)


print("----------task 15")
string_input15 = 'sdfdsfz fgzfgfg zz'
result_string15 = ''
idx15 = 0
seen_chars = set()

while idx15 < len(string_input15):
    current_char = string_input15[idx15]

    if current_char not in seen_chars:
        result_string15 += current_char
        seen_chars.add(current_char)

    idx15 += 1

print('result_string15', result_string15)


print("----------task 16")
string_input16 = 'ab1 cCbb1 B1b1'
result_string16 = ''
idx16 = 0

while idx16 < len(string_input16):
    current_char = string_input16[idx16]
    if current_char == 'b' and idx16 + 1 < len(string_input16) and string_input16[idx16 + 1].isdigit():
        result_string16 += string_input16[idx16 + 1]
        idx16 += 1
    else:
        result_string16 += current_char

    idx16 += 1

filtered_string = ''.join(
    char for char in result_string16 if not (char.islower()))
print('string_input16', string_input16)
print('result_string16', result_string16)
print('filtered_string', filtered_string)


print("----------task 17")
string_input17 = 'textk text simplek simple kke3'
words = string_input17.split()
print(sum(1 for word in words if word.endswith('k')))


print("----------task 18")
number_input18 = 666

declination_array = ["корова", "коровы", "коров"]
for i in range(1, number_input18 + 1):

    if i % 100 in {11, 12, 13, 14}:
        print(f"На лугу {i} {declination_array[2]}")
    elif i % 10 == 1:
        print(f"На лугу {i} {declination_array[0]}")
    elif 2 <= i % 10 <= 4:
        print(f"На лугу {i} {declination_array[1]}")
    else:
        print(f"На лугу {i} {declination_array[2]}")
