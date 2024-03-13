
# fmt: off
import sys
import csv
import json
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_directory, '..', '..'))

sys.path.append(project_root)
from homework.homework8.index import get_word_count




'''
Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного файла есть восклицательный знак. 
info.txt

jdasdqwd wqdqwd 
dqwd dqwd qd dqwd!
Ewqe eqwe q eq!
Dad das
Dasd das asd as

Sample Output:
dqwd dqwd qd dqwd!
Ewqe eqwe q eq!
'''

with open(os.path.join(current_directory, 'info.txt'), 'r') as file:
    lines_with_exclamation = [line.strip() for line in file if '!' in line]

for line in lines_with_exclamation:
    print('--line: ', line)
# --------------------------------------------------------------------

'''
Создать файл input.txt и записать в него 10 чисел через пробел. Считать из него эти числа. Затем записать их произведение в файл output.txt.
'''
with open(os.path.join(current_directory, 'input.txt'), 'w') as input_file:
    numbers = "1 2 3 4 5 6 7 8 9 10"
    input_file.write(numbers)

with open(os.path.join(current_directory, 'input.txt'), 'r') as input_file:
    numbers_str = input_file.read()
    numbers_list = list(map(int, numbers_str.split()))

result = 1
for number in numbers_list:
    result *= number

# print('--result', result)
with open(os.path.join(current_directory, 'output.txt'), 'w') as output_file:
    output_file.write(str(result))

# --------------------------------------------------------------------

'''
Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара, цену единицы. 
Вывести список товаров стоимость которых превышает 1 000 000 р.

goods.txt

tv-set 300 5000
cars 700 20000
plane 11 100000
doors 1000 350

Sample Output:
[“plane”, “cars”]
'''

# todo tv-set 300 5000 тоже попадает под условие

with open(os.path.join(current_directory, 'goods.txt'), 'r') as goods_file:
    data = goods_file.readlines()

expensive_goods = []

for item in data:
    #  при условии формата name - quantity - price
    parts = item.split()
    name, quantity, price = parts[0], int(parts[1]), int(parts[2])

    total_price = quantity * price

    if (total_price > 1000000):
        expensive_goods.append(name)

print('--expensive_goods: ', expensive_goods)
# --------------------------------------------------------------------

'''
Написать программу “Викторина”. У вас есть 2 файла. В первом содержаться 10 вопросов(каждый вопрос в своей строке) 
во втором 10 ответов( каждый ответ как и вопрос в своей строке). 
Вам нужно считывать по 1 вопросу из файла с вопросами и давать на них ответ. 
Если ответ верный, добавлять к счётчику верных ответов 1 балл. В конце программа выводит количество верных ответов на вопросы.

Questions.txt

Столица Великобритании?
Страна производитель Пежо?
…

Answers.txt 

Лондон
Франция
…

Sample Output:
Столица Великобритании?
Страна производитель Пежо?
Верных ответов: 1

Sample Input:
Лондон
Италия
'''
with open(os.path.join(current_directory, 'questions.txt'), 'r') as questions_file:
    questions = questions_file.readlines()

with open(os.path.join(current_directory, 'answers.txt'), 'r') as answers_file:
    answers = answers_file.readlines()

number_correct_answers = 0

for index, question in enumerate(questions):
    answer = input(f"{question}: ")

    if (answer.lower().strip() == answers[index].lower().strip()):
        number_correct_answers += 1

print('--number_correct_answers: ', number_correct_answers)
# --------------------------------------------------------------------

'''
Создать словарь в качестве ключа которого будет 5-ти значное число, 
а в качестве значений кортеж состоящий из 2-ух элементов – имя(str) и возраста(int). 
Сделать 5-6 элементов словаря и записать данный словарь на диск в файл json формата
'''

data = {
    11111: ('Alice', 25),
    22222: ('Bob', 30),
    33333: ('Charlie', 22),
    44444: ('David', 28),
    55555: ('Eva', 35)
}

with open(os.path.join(current_directory, 'data.json'), 'w') as json_file:
    json.dump(data, json_file)

# --------------------------------------------------------------------

'''
Прочитать сохранённый json – файл и записать данные на диск в csv файл. 
Первое значение каждой строки должно начинаться со слова person, значения разделить ;
'''

with open(os.path.join(current_directory, 'data.json'), 'r') as json_file:
    person_data = json.load(json_file)

csv_filename = os.path.join(current_directory, 'output.csv')


with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';')

    for person in person_data.values():
        # print('--person', person)
        csv_writer.writerow(['person'] + [person[0]] + [str(person[1])])
# --------------------------------------------------------------------

'''
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, 
сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое. Для решение вам необходимо открыть файл для чтения 7.txt .
Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
'''

with open(os.path.join(current_directory, '7.txt'), 'r') as txt_7_file:
    txt_7_file = txt_7_file.read()

words = txt_7_file.split()
lowercase_words = [word.lower() for word in words]
book_dict_result = get_word_count(lowercase_words)

max_word = max(book_dict_result, key=book_dict_result.get)
print(f'max_word: {max_word} - count {book_dict_result[max_word]}')
# --------------------------------------------------------------------

'''
Вашей задачей будет восстановление исходной строки обратно. Напишите программу, которая считывает из файла строку, 
соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст. 
Для решение вам необходимо открыть файл для чтения 8.txt .
Sample Input:
a3b4c2e10b1
Sample Output:
Aaabbbbcceeeeeeeeeeb
'''

def decode_string(encoded_string: str) -> str:
    decoded_string = ''
    current_char = ''
    count = 0

    for char in encoded_string:
        if char.isalpha():
            decoded_string += current_char * max(count, 1)
            current_char = char
            count = 0
        elif char.isdigit():
            count = count * 10 + int(char)

    decoded_string += current_char * max(count, 1)

    return decoded_string.capitalize()

with open(os.path.join(current_directory, '8.txt'), 'r') as file:
    encoded_string = file.read().strip()

decoded_string = decode_string(encoded_string)

print('--encoded_string: ', encoded_string)
print('--decoded_string: ', decoded_string)
# --------------------------------------------------------------------