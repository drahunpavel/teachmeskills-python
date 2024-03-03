import math

if __name__ == '__main__':

    ''' Напишите программу которые будет ловить IndexError, когда вы пытаетесь взять индекс элемента, которого нет в списке. '''
    try:
        list_1 = [1, 2, 3]
        print(list_1[4])
    except IndexError as e:
        print(f"Caught an IndexError: {e}")
    # --------------------------------------------------------------------

    ''' Напишите программу которые будет ловить TypeError, когда вы пытаетесь скаткатенировать строку и число.'''
    try:
        num_value = 3
        str_value = 'three'
        print(num_value + str_value)
    except TypeError as e:
        print(f"Caught an TypeError: {e}")
    # --------------------------------------------------------------------

    ''' Напишите программу которая вычисляет площадь треугольника по формуле Герона,
    однако если пользователь введёт длину хоть одной стороны треугольника равную 0, то программа должна бросить исключение ArithmeticError.
    '''

    def calculate_area(a: int, b: int, c: int) -> int:
        if a == 0 or b == 0 or c == 0:
            raise ArithmeticError("One or more sides is zero")

        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    try:
        side_a, side_b, side_c = 0, 4, 5
        area = calculate_area(side_a, side_b, side_c)
        print(f"Area: {area:.0f}")

    except ArithmeticError as e:
        print(f"Caught an ArithmeticError: {e}")
    # --------------------------------------------------------------------

    ''' Дана строка. Проверьте есть ли в ней цифры, иначе бросьте ValueError.'''

    def has_numbers(str: str) -> bool:
        has_digit = False
        for char in str:
            if char.isdigit():
                has_digit = True

        if not has_digit:
            raise ValueError("No numbers")

        return has_digit

    string = 'Hello world'
    try:
        has_numbers(string)
    except ValueError as e:
        print(f"Caught an ValueError: {e}")
    # --------------------------------------------------------------------

    '''
    Дан словарь, который содержит некоторые ключи и значения по этим ключам, пользователь не знает этих ключей. 
    Бросьте ошибку KeyError в том случае когда пользователь пытается просмотреть значение по ключу, которого нет в словаре.
    '''

    dict = {'a': 1, 'b': 2, 'c': 3}

    def get_dict_value_by_key(key: str) -> any:
        try:
            return dict[key]
        except KeyError:
            raise KeyError(f"Key '{key}' not found in the dictionary")

    try:
        print(get_dict_value_by_key('c1'))
    except KeyError as e:
        print(f"Caught an KeyError: {e}")
    # --------------------------------------------------------------------

    '''
    Даны два списка чисел. Найдите все числа, которые не содержатся одновременно в этих двух списках.
    '''
    # разность для множеств (set)
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]

    set1 = set(list1)
    set2 = set(list2)

    # print(set1, set2)

    unique_list = list(set1.symmetric_difference(set2))
    print('unique_list: ', unique_list)

    # --------------------------------------------------------------------

    '''
    Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
    '''

    def check_numbers(num_arr: list[int]) -> None:
        print('check_numbers input: ', num_arr)
        seen_numbers = set()
        for num in num_arr:
            if (num in seen_numbers):
                print('YES')
            else:
                print('NO')
                seen_numbers.add(num)

    # input_value_1 = (input("Entry numbers: ")).split()
    input_value_1 = [1, 2, 3, 3, 5, 5]
    check_numbers(input_value_1)
    # --------------------------------------------------------------------

    '''
    В ходе исследований ученые делают некие замеры, результаты которых заносят в базу данных. 
    Однако для анализа результатов нет необходимости держать в базе "лишние", повторяющиеся данные. 
    Напишите программу, которая выводит максимальное количество записей, 
    после удаления которых анализ результатов будет произведен верно. Список элементов вводится через пробел.

    Sample Input:
    6311 9423 142 142 8654 909 Error 6311 142 909 404 502 828 404 9423
    Sample Output:
    6'''

    # множество - уникальные значения

    # input_value_2 = input("Entry: ").split()
    input_value_2 = ['6311', '9423', '142', '142', '8654', '909',
                     'Error', '6311', '142', '909', '404', '502', '828', '404', '9423']
    set3 = set(input_value_2)

    print('result: ', len(input_value_2) - len(set3))
    # --------------------------------------------------------------------

    '''
    Создайте словарь, связав его с переменной school, и наполните данными, которые бы отражали количество учащихся в разных 9 классах (9а, 9б, 9в, 9м, 9ф и т. п.). 
    Внесите изменения в словарь согласно следующему: 
    '''
    school = {
        '9а': 17,
        '9б': 15,
        '9в': 19,
        '9м': 22,
    }
    print('--school-1', school)
    # в одном из классов изменилось количество учащихся
    school['9а'] = 13
    print('--school-2', school)
    # в школе появился новый класс
    school['9г'] = 30
    print('--school-3', school)
    # в школе был расформирован (удален) другой класс
    del school['9м']
    print('--school-4', school)
    # Вычислите общее количество учащихся 9 классов в школе
    print('--school-5', sum(school.values()))
    # print('--test', school.keys())

    # --------------------------------------------------------------------

    '''
    Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. 
    Все слова в словаре различны. Для введённого слова вывести его синоним или написать что его нет.
    '''

    synonyms_dict = {
        'fast': 'quick',
        'big': 'large',
        'small': 'tiny',
        'bad': 'terrible',
        'old': 'ancient',
        'new': 'modern',
        'hot': 'spicy',
        'cold': 'chilly',
    }

    def find_synonym(word: str) -> str:
        return synonyms_dict.get(word, None)

    # input_value_3 = input("Entry: ")
    input_value_3 = 'cold1'
    synonym = find_synonym(input_value_3)

    print('synonym: ', synonym) if synonym is not None else print(
        'synonym: not found')

    # --------------------------------------------------------------------

    '''
    Стремясь стать программистом, важно не только постоянно учиться, но и понимать язык, на котором говорят Ваши коллеги. Чтобы систематизировать знания, 
    Вы решили написать программу, которая составляет маленький словарь из сленговых выражений. 
    Программа принимает на вход строки до символа точки, состоящие из понятий и их определений, разделенных знаком тире. 
    После заполнения словаря программе передается натуральное число m – количество запросов, а затем m строк, каждая из которых представляет собой одно понятие. 
    Если это понятие есть в словаре, необходимо вывести его определение, в обратном случае – "Не найдено".

    Sample Input:
    DNS – компьютерная система для получения, хранения и обработки информации о доменных именах
    Интрасеть – это замкнутая внутренняя сеть какой-либо организации, работающая по Интернет-протоколу TCP/IP
    Фича – недокументированная дополнительная возможность, фишка
    Мейнфрейм – большой компьютер, имеющий высокую вычислительную мощность
    .
    4
    Бэкап
    Фича
    Линуксоид
    DNS
    Sample Output:
    Не найдено
    недокументированная дополнительная возможность, фишка
    Не найдено
    компьютерная система для получения, хранения и обработки информации о доменных именах

    '''

    slang_dict = {}

    while True:
        input_value_4 = input("Entry example value: ")
        if input_value_4 == '.':
            break

        # без лишних проверок на регистры, пробелы и тд.
        concept, definition = input_value_4.split(' – ')
        # print('--concept', concept)
        # print('--definition', definition)
        slang_dict[concept] = definition

    num_queries = int(input('Entry num queries:'))

    for _ in range(num_queries):
        query = input('Entry concept: ')
        print(slang_dict.get(query, 'not found'))

    # --------------------------------------------------------------------

    '''
    Коля устал запоминать телефонные номера и заказал у Вас программу, которая заменила бы ему телефонную книгу. 
    Коля может послать программе два вида запросов: строку, содержащую имя контакта и его номер, разделенные пробелом, или просто имя контакта. 
    В первом случае программа должна добавить в книгу новый номер, во втором – вывести номер контакта. 
    Ввод происходит до символа точки. Если введенное имя уже содержится в списке контактов, необходимо перезаписать номер.
    Sample Input:
    Ben 89001234050
    Mary
    Alice 210-220
    Alice
    Alice 404-502
    Ben
    Nick +4(908)273-22-42
    Nick
    Alice
    Robert 51234047129
    .
    Sample Output:
    не найдено
    210-220
    89001234050
    +4(908)273-22-42
    404-502
    '''

    phone_dict = {}

    while True:
        input_value_6 = input("Entry contact: ")
        if input_value_6 == '.':
            break

        contact_info = input_value_6.split()
        name = contact_info[0]

        if (len(contact_info) == 2):
            phone = contact_info[1]
            phone_dict[name] = phone
        else:
            found_phone = phone_dict.get(name, 'phone not found')
            print('--found phone: ', found_phone)

    # --------------------------------------------------------------------


'''
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге. 
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику. 
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в 
этой строке число его повторений (без учёта регистра) в формате "слово количество". 
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.

Sample Input 1:
a aa abC aa ac abc bcd a
Sample Output 1:
ac 1
a 2
abc 2
bcd 1
aa 2
'''

# input_value_5 = input("Entry: ")
input_value_5 = 'a aa abC aa ac abc bcd a a avc abC'.split()


def get_word_count(word_arr: list[str]) -> None:

    book_dict = {}

    for word in word_arr:
        found_word = book_dict.get(word, None)
        if found_word is None:
            book_dict[word] = 1
        else:
            book_dict[word] = book_dict[word] + 1

    return book_dict


book_dict_result = get_word_count(input_value_5)
print('--book_dict: ', book_dict_result)

# --------------------------------------------------------------------
