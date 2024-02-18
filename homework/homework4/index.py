print("----------task 1")

# string1 = input("Enter text: ")
string1 = 'this is test string'

print(f"1.1: {string1[2]}")
print(f"1.2: {string1[-2]}")
print(f"1.3: {string1[:5]}")  # до 5го включительно
print(f"1.4: {string1[:-2]}")  # без двух последних
print(f"1.5: {string1[::2]}")  # Чет index
print(f"1.6: {string1[1::2]}")  # Нечет index
print(f"1.7: {string1[::-1]}")  # Обратный порядок (все символы)
print(f"1.8: {string1[::-2]}")  # Обратный порядок (через один)
print(f"1.9: {len(string1)}")

print("----------task 2")

string2 = 'test stringt'
print(string2[0] == string2[-1])

print("----------task 3")
string3 = "яблоко"
print(string3[1:5])
print(string3[3:])

print("----------task 4")
string4 = "*"
print(string4*5)

print("----------task 5")  # палиндромом
string5 = "шалаш1"
print(string5 == string5[::-1])

print("----------task 6")
string6 = "af"
count = string6.count('f')

if count == 1:
    print('single: ', string6.find('f'))
elif count > 1:
    print('all: ', count)

print("----------task 7")
string7 = "sdfsdf1sdfsdf2sd fdsfdsf1"
print(string7.replace('1', 'ONE'))


print("----------task 8")
string8 = "adfsdf"
first_index = string8.find('f')
second_index = string8.find('f', first_index + 1)


if (first_index == -1):
    print(2)
elif (second_index == -1):
    print(1)
else:
    print('second_index', second_index)


print("----------task 10")
string10 = '192.168.0.1'
string10_2 = string10.replace('.', ' ')
print(string10_2)
numbers = [int(num) for num in string10_2.split()]
print(sum(numbers))
