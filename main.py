# 1
"""
name = input('Your name: ')
surname = input('Your surname: ')

# print('Dear %s %s!\n'
#       'Welcome to our conference!' % (name, surname)
#       )
ID = name, surname

print('Dear {1} {0}!\n'
      'Welcome to our conference!'.format(*ID)
      )

print('Dear {name} {surname}!\n'
      'Welcome to our conference!'.format(name=name, surname=surname)
      )
"""

# 2
"""
# Перевернутая башня (задача)

Number = int(input('Enter a number: '))

max_number = 1
max_floor = 1
level = 1

while Number > max_number:
    level += 1
    max_number = max_number + level ** 2
    max_floor = max_floor + level

floor = max_floor - (max_number - Number) // level
left_pos = level - (max_number - Number) % level

print('level: ', level)
print('Комната {room} находится на {floor} этаже, {left_pos}-я слева'.format(floor=floor, left_pos=left_pos, room=Number))
"""

# 3
"""
while True:
    data_format = False
    data = input('Enter date in format "dd.mm.yyyy": ')
    ls_data = data.split('.')
    try:
        d, m, y = ls_data
    except ValueError:
        print('Enter date in format "dd.mm.yyyy')
        continue
    if len(ls_data) == 3 and len(d) == 2 and len(m) == 2 and len(y) == 4:
        data_format = True

    if data_format:
        if y.isdigit():
            pass
        else:
            print('Год должен быть числом!')
            continue

        if m.isdigit():
            pass
        else:
            print('Месяц должен быть числом!')
            continue
        if 0 <= int(m) <= 12:
            pass
        else:
            print('Месяц должен быть числом от 1 до 12')
            continue

        if d.isdigit():
            pass
        else:
            print('День должен быть числом!')
            continue
        if int(m) in [1, 3, 5, 7, 8, 10, 12]:
            if 0 <= int(d) <= 31:
                pass
            else:
                print('День должен быть от 1 до 31')
                continue
        else:
            if 0 <= int(d) <= 30:
                pass
            else:
                print('День должен быть от 1 до 30')
                continue
        break
    else:
        print('Введите дату в формате: хх.хх.хххх')
        continue
"""

# Вебинар №2 / Задача №1
# dalniy_vostok_regions = ('амурская область', 'республика бурятия', 'еврейская автономная область', 'забайкальский край',
#                  'камчатский край', 'магаданская область', 'приморский край', 'республика саха (якутия)',
#                  'сахалинская область', 'хабаровский край', 'чукотский автономный округ')
# base_rate = 8.0  # стандартная базовая ставка 8%
#
# print("""
# Добро пожаловать в наш новый ипотечный калькулятор!
#
# Давайте вместе определим лучшую процентную ставку для Вас в зависимости от Ваших условий :)
#
# Стандартная базовая ставка 8%
# Если Вы из Дальневосточного федерального округа, то базовая ставка для Вас 2%. Не суммируется с другими скидками!
# Если количество несовершеннолетних детей больше 3, то стандартная базовая ставка уменьшается на 1%
# Если Вы наш зарплатный клиент, то стандартная базовая ставка уменьшается на 0.5%
# Если Вы оформите страхование в нашем банке,то стандартная базовая ставка уменьшается на 1.5%
# """)
#
# location = ''
# while not location:
#     location = input('Пожалуйста, укажите, из какого Вы региона? Пример корректного ввода: "Москва", "Московская область",'
#                      ' "Алтайский край" "Республика Татарстан", "Еврейская автономная область", '
#                      '"Чукотский автономный округ" и т.п.\n'
#                      'Чтобы вывести список регионов Дальневосточного федерального округа, пожалуйста, нажмите "*"')
#     if location == '*':
#         for region in dalniy_vostok_regions:
#             print(region.upper())
#         location = ''
#
# rate = base_rate
# if location.lower() in dalniy_vostok_regions:
#     rate = 2.0
#     print(f'Ваша ставка {rate}%')
# else:
#     try:
#         child_qty = int(input('Сколько у Вас несовершеннолетних детей? Пример корректного ввода: "0", "1", "2" и т.п.'))
#     except ValueError:
#         print('Для правильного расчета Вашей процентной ставки, нужно ввести число!')
#         child_qty = 0
#     salary_client = input('Вы наш зарплатный клиент? Пример корректного ввода: "Да" или "Нет".')
#     insurance_client = input('Вы будете оформлять страхование у нас? Пример корректного ввода: "Да" или "Нет".')
#     # считаем, что все остальные скидки суммируются, т.е. если, например, заемщик одновременно является
#     # и клиентом банка и многодетным (> 3 детей) и оформляет у нас страховку, то общая скидка: "1.0 + 0.5 + 1.5 = 3%"
#     if child_qty > 3:
#         rate = rate - 1.0
#     if salary_client.lower() == 'да':
#         rate = rate - 0.5
#     if insurance_client.lower() == 'да':
#         rate = rate - 1.5
#     print(f'Ваша ставка {rate}%')
#
# ####################################################################################################################
#
# # Вебинар №2 / Задача №2
# print('Определение знака зодиака по дате рождения\n'
#       'Ссылка на источник: https://ru.wikipedia.org/wiki/%D0%97%D0%BD%D0%B0%D0%BA%D0%B8_%D0%B7%D0%BE%D0%B4%D0%B8%D0%B0%D0%BA%D0%B0\n'
#       'Колонка "Западная астрология (вариант I)" в таблице')
# try:
#     date = int(input('Введите число, например "21": '))
# except ValueError:
#     date = 0
#
# month = input('Введите месяц, например "март": ')
#
# if month.lower() == 'март' and 21 <= date <= 31:
#     zodiac = 'Овен'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'март' and 0 < date < 21:
#     zodiac = 'Рыбы'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'апрель' and 20 <= date <= 30:
#     zodiac = 'Телец'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'апрель' and 0 < date < 20:
#     zodiac = 'Овен'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'май' and 21 <= date <= 31:
#     zodiac = 'Близнецы'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'май' and 0 < date < 21:
#     zodiac = 'Телец'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'июнь' and 21 <= date <= 30:
#     zodiac = 'Рак'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'июнь' and 0 < date < 21:
#     zodiac = 'Близнецы'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'июль' and 23 <= date <= 31:
#     zodiac = 'Лев'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'июль' and 0 < date < 23:
#     zodiac = 'Рак'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'август' and 23 <= date <= 31:
#     zodiac = 'Дева'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'август' and 0 < date < 23:
#     zodiac = 'Лев'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'сентябрь' and 23 <= date <= 30:
#     zodiac = 'Весы'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'сентябрь' and 0 < date < 23:
#     zodiac = 'Дева'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'октябрь' and 23 <= date <= 31:
#     zodiac = 'Скорпион'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'октябрь' and 0 < date < 23:
#     zodiac = 'Весы'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'ноябрь' and 22 <= date <= 30:
#     zodiac = 'Стрелец'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'ноябрь' and 0 < date < 22:
#     zodiac = 'Скорпион'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'декабрь' and 22 <= date <= 31:
#     zodiac = 'Козерог'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'декабрь' and 0 < date < 22:
#     zodiac = 'Стрелец'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'январь' and 20 <= date <= 31:
#     zodiac = 'Водолей'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'январь' and 0 < date < 20:
#     zodiac = 'Козерог'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'февраль' and 19 <= date <= 29:
#     zodiac = 'Рыбы'
#     print('Ваш знак: ', zodiac)
# elif month.lower() == 'февраль' and 0 < date < 19:
#     zodiac = 'Водолей'
#     print('Ваш знак: ', zodiac)
# else:
#     zodiac = None
#     print('Пожалуйста правильно введите число и месяц рождения! См. примеры ввода в тексте запроса')

#######################################################################################################################

# """Домашнее задание к лекции 3.«Введение в типы данных и циклы»"""
#
# # Задача №1
# print('Задача №1')
# print()
#
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
#
# if len(boys) == len(girls):
#     for boy, girl in zip(sorted(boys, key=str.lower), sorted(girls, key=str.lower)):
#         print(f'{boy.capitalize()} и {girl.capitalize()}')
# else:
#     print('Количество мальчиков не равно количеству девочек! Знакомство не состоится, т.к. кто-то останется без пары!')
#
# #######################################################################################################################
#
# print()
# print('*' * 50)
# print()
#
# #######################################################################################################################
#
# # Задача №2
# print('Задача №2')
# print()
#
# cook_book = [
#   ['салат',
#       [
#         ['картофель', 100, 'гр.'],
#         ['морковь', 50, 'гр.'],
#         ['огурцы', 50, 'гр.'],
#         ['горошек', 30, 'гр.'],
#         ['майонез', 70, 'мл.'],
#       ]
#   ],
#   ['пицца',
#       [
#         ['сыр', 50, 'гр.'],
#         ['томаты', 50, 'гр.'],
#         ['тесто', 100, 'гр.'],
#         ['бекон', 30, 'гр.'],
#         ['колбаса', 30, 'гр.'],
#         ['грибы', 20, 'гр.'],
#       ],
#   ],
#   ['фруктовый десерт',
#       [
#         ['хурма', 60, 'гр.'],
#         ['киви', 60, 'гр.'],
#         ['творог', 60, 'гр.'],
#         ['сахар', 10, 'гр.'],
#         ['мед', 50, 'мл.'],
#       ]
#   ]
# ]
#
# persons = 5
#
# for dish, ingredients in cook_book:
#     print(f'{dish.capitalize()}:')
#     # ingredients_for_all_persons = map(lambda ingredient_: [ingredient_[0], ingredient_[1] * persons, ingredient_[2]],
#     #                                   ingredients)
#     # print(list(ingredients_for_all_persons))
#     for ingredient in ingredients:
#         print(f'{ingredient[0]}, {ingredient[1] * persons}{ingredient[2]}')
#     print()

#######################################################################################################################

# """Домашнее задание к лекции 4.«Коллекции данных. Словари. Множества»"""
#
# # Задача №1
# print('Задача №1')
# print()
#
#
# geo_logs = [
#     {'visit1': ['Москва', 'Россия']},
#     {'visit2': ['Дели', 'Индия']},
#     {'visit3': ['Владимир', 'Россия']},
#     {'visit4': ['Лиссабон', 'Португалия']},
#     {'visit5': ['Париж', 'Франция']},
#     {'visit6': ['Лиссабон', 'Португалия']},
#     {'visit7': ['Тула', 'Россия']},
#     {'visit8': ['Тула', 'Россия']},
#     {'visit9': ['Курск', 'Россия']},
#     {'visit10': ['Архангельск', 'Россия']}
# ]
#
# # # Альтернативный способ в 1 строку кода:
# # filtered_geo_logs = filter(lambda item: item[list(item.keys())[0]][1].lower() == 'россия', geo_logs)
# # print(list(filtered_geo_logs))
#
# filtered_geo_logs = []
# for data in geo_logs:
#     if data[list(data.keys())[0]][1].lower() == 'россия':
#         filtered_geo_logs.append(data)
#
# print(list(filtered_geo_logs))
#
# ####################################################################################################################
#
# # Задача №2
#
# print('*' * 50)
# print('Задача №2')
#
# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}
#
# # result = set()
# # ids_sets = list(result.update(set(list_item)) for list_item in ids.values())
# # print(list(result))
# # print(ids_sets)
#
# uniq_ids = set()
# for list_item in ids.values():
#     set_item = set(list_item)
#     uniq_ids.update(set_item)
#
# print(list(uniq_ids))
#
# ####################################################################################################################
#
# # Задача №3
#
# print('*' * 50)
# print('Задача №3')
#
# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт'
#     ]
#
# # frequency_list = {len(query.split()): 1 for query in queries}
# # print(frequency_list)
#
# frequencies = {}
# for query in queries:
#     word_qty = len(query.split())
#     if word_qty in frequencies:
#         frequencies[word_qty] += 1
#     else:
#         frequencies[word_qty] = 1
#
# relative_frequencies = {}
# for key in sorted(frequencies.keys()):
#     relative_frequencies[key] = frequencies[key] / len(queries) * 100
#     print('Поисковых запросов из', key, 'слов -', '%.2f' % relative_frequencies[key], '%')
# # print(frequencies)
# # print(relative_frequencies)
#
# ####################################################################################################################
#
# print('*' * 50)
# print('Задача №4')
#
# stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
#
# # Альтенативные способы решения (Не лучшие способы, т.к. высокие затраты времени и памяти на сортировку коллекции):
# # Альтернативный способ №1
# # sorted_stats = sorted(stats.items(), key=lambda x: x[1])
# # print(sorted_stats)
# # print(sorted_stats[-1][0])
#
# # Альтернативный способ №2а
# # sorted_stats = {key: val for key, val in sorted(stats.items(), key=lambda x: x[1])}
# # Альтернативный способ №2б
# # sorted_stats = {key: stats[key] for key in sorted(stats, key=stats.get)}
# # print(tuple(sorted_stats.items())[-1][0])
#
# best_channel = tuple(stats.keys())[0] if stats else None
# for key in stats:
#     if best_channel and stats[key] > stats[best_channel]:
#         best_channel = key
# print('Лучший рекламный канал:', best_channel)
#
# ####################################################################################################################
#
# print('*' * 50)
# print('Задача №5')
#
# custom_list = ['2018-01-01', 'yandex', 'cpc', 100]
#
# custom_dict = {}
# key = custom_list[-2]
# dict_previous = {key: custom_list[-1]}
# for i in range(len(custom_list) - 2):
#     custom_dict = {}
#     key = custom_list[-3 - i]
#     custom_dict[key] = dict_previous
#     dict_previous = custom_dict
# print(custom_dict)

######################################################################################################################

"""Домашнее задание к лекции 5. «Функции — использование встроенных и создание собственных»"""
# Ссылка на задание:  https://github.com/netology-code/py-homeworks-basic/tree/master/5.functions

# Предполагается, что номер документа должен быть уникальным и документ с 1 уникальным номером должен храниться только на 1 полке !!!

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "101", "name": "Михаил Светлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '101'],
    '2': ['10006'],
    '3': []
}


# Задачи №1 и №2
# Предполагается, что номер документа должен быть уникальным и документ с 1 уникальным номером должен храниться только на 1 полке !!!

def get_name(document_list):
    """Функция принимает на вход список документов и возвращает имя человека по номеру документа.
    Каждый документ должен быть структурой данных "словарь".
    Если документ не найден, то возвращается None"""

    document_number = input('Введите номер документа: ')
    for index, document in enumerate(document_list):
        if document.get('number') == document_number:
            document_index = index
            print('Имя: ', document_list[document_index].get('name'))
            return document_list[document_index].get('name')
    print('Документ не найден!')
    return None


def get_shelf(directories_dict, doc_number=None):
    """Функция принимает на вход объект с информацией о местонахождении документов на полках и возвращает
     номер полки по номеру документа.
    Объект на входе функции должен быть структурой данных "словарь".
    Если документ не найден, то возвращается None"""

    if doc_number is None:
        document_number = input('Введите номер документа: ')
    else:
        document_number = doc_number
    for key, vals in directories_dict.items():
        if document_number in vals:
            print(f'Номер полки с документом № {document_number}: {key}')
            return key
    print('Документ не найден!')
    return None


def get_all_document_numbers(document_list):
    """Получить список номеров всех документов из каталога 'document_list' """
    doc_numbers = []
    for item in document_list:
        doc_numbers.append(item.get('number'))
    return doc_numbers


def print_all_documents_to_stdout(document_list):
    """Функция принимает на вход список документов и выводит на экран (stdout) полную информацию обо всех документах,
    отсортированную по заданному ключу.
    Каждый документ должен быть структурой данных "словарь".
    Функция возвращает None"""

    # Превращение входных данных (list of dict) в список строк, если это нужно :)
    # result = (' '.join(document.values()) for document in document_list)

    # Заданные константы функции
    sort_keys = ("type", "name")  # поддерживаемые параметры сортировки
    default_sort_key = "type"  # параметр сортировки списка вывода по умолчанию
    # sort_types = ("up", "down")  # "up" - сортировка по возрастанию, "down" - по убыванию
    is_reversed = False  # по умолчанию сортировка списка выполняется "по возрастанию"

    sort_key = input('Введите, по какому параметру сортировать вывод документов: "type" или "name": ')
    sort_type = input('Введите "up" или "down". "up" - сортировка по возрастанию, "down" - по убыванию: ').lower()
    reverse_type = is_reversed

    if sort_key in sort_keys:
        print(f'Вывод отсортирован по параметру "{sort_key}"')
        if sort_type == 'up':
            print('Вывод отсортирован во возрастанию')
        elif sort_type == 'down':
            print('Вывод отсортирован во убыванию')
            reverse_type = not is_reversed
        else:
            print(f'Тип сортировки "{sort_type}" не поддерживается. Вывод отсортирован во возрастанию (значение по умолчанию)')
    else:
        print(f'Сортировка по параметру "{sort_key}" в настоящий момент не поддерживается! '
              f'Вывод отсортирован по параметру по умолчанию "{default_sort_key}"')
        sort_key = default_sort_key
        if sort_type == 'up':
            print('Вывод отсортирован во возрастанию')
        elif sort_type == 'down':
            print('Вывод отсортирован во убыванию')
            reverse_type = not is_reversed
        else:
            print(f'Тип сортировки "{sort_type}" не поддерживается. Вывод отсортирован во возрастанию (значение по умолчанию)')

    sorted_document_list = sorted(document_list, reverse=reverse_type, key=lambda item: item.get(sort_key).lower())
    for document in sorted_document_list:
        print(f'{document.get("type")} "{document.get("number")}" "{document.get("name")}"')
    return sorted_document_list


def add_document(document_list, directories_dict):
    """Функция принимает на вход список документов (каталог) и словарь (номера полок с номерами документов).
    Функция добавляет новый документ в каталог и на полку, только если номер документа уникальный и существует
    полка с заданным номером.
    """

    doc_type = doc_number = doc_name = None
    try:
        doc_type, doc_number, doc_name = input('Пожалуйста, введите тип, номер документа и имя'
                                               ' через запятую, например: invoice, 111, Ivan Ivanov: ').split(',')
    except ValueError:
        print('Документ не создан! Нужно ввести 3 значения через запятую, например: invoice, 111, Ivan Ivanov')

    if doc_number is not None:
        doc_type, doc_number, doc_name = doc_type.strip(' .'), doc_number.strip(' .'), doc_name.strip(' .')
        existing_doc_numbers = get_all_document_numbers(document_list)
        if doc_number not in existing_doc_numbers:
            shelf_number = input(f'Введите номер полки, на которой новый документ будет храниться. '
                                 f'Доступны следующие полки: {", ".join(directories_dict.keys())}: ')
            if shelf_number in directories_dict.keys():
                new_document = dict(type=doc_type, number=doc_number, name=doc_name)
                # Добавляем документ в каталог
                document_list.append(new_document)
                # Добавляем документ на полку
                directories_dict[shelf_number].append(doc_number)
                print('Документ успешно добавлен!')
            else:
                print('Документ не создан, т.к. Вы ввели несуществующий номер полки для хранения! '
                      f'Доступны следующие полки: {", ".join(directories_dict.keys())}: ')
        else:
            print('Документ не создан, т.к. документ с таким номером уже есть в каталоге. '
                  'Номер документа должен быть уникальным!')
    return document_list, directories_dict


def get_doc_index_by_doc_number(document_list, document_number):
    """Получить индекс документа из каталога (списка) 'document_list' с определенным номером,
     заданным параметром 'document_number' """
    for index, dict_ in enumerate(document_list):
        if dict_.get('number') == document_number:
            return index
    return None


def delete_document(document_list, directories_dict):
    """Удалить локумент из каталога 'document_list' и с полки 'directories_dict' """

    doc_number = input('Введите номер документа: ')
    if doc_number in get_all_document_numbers(document_list):
        index = get_doc_index_by_doc_number(document_list, doc_number)
        # Удаляем документ из каталога:
        document_list.pop(index)

        # Удаляем документ с полки:
        shelf_number = get_shelf(directories_dict, doc_number)
        directories_dict[shelf_number].remove(doc_number)
        print(f'Документ №{doc_number} удален из каталога и с полки №{shelf_number}')
    else:
        print('Документ с данным номером не существует!')


def move_document(document_list, directories_dict):
    """Переместить документ на другую полку"""

    doc_number = input('Введите номер документа, который Вы хотите переместить на другую полку: ')
    new_shelf_number = input('Введите номер полки: ')
    if doc_number in get_all_document_numbers(document_list):
        current_shelf_number = get_shelf(directories_dict, doc_number)
        if new_shelf_number in directories_dict.keys() and new_shelf_number != current_shelf_number:
            # Перемещаем документ на другую полку
            directories_dict[current_shelf_number].remove(doc_number)
            directories_dict[new_shelf_number].append(doc_number)
            print('Документ №{0} перемещен полку №{1}!'.format(doc_number, new_shelf_number))
        elif new_shelf_number in directories_dict.keys() and new_shelf_number == current_shelf_number:
            print('Документ №{0} уже находится на полке №{1}!'.format(doc_number, current_shelf_number))
        else:
            print(f'Полки №{new_shelf_number} не существует! Доступны следующие полки: {", ".join(directories_dict.keys())}: ')
    else:
        print('Документ с №{} не найден!'.format(doc_number))


def add_shelf(directories_dict):
    """Добавить новую полку в перечень 'directories_dict' """

    new_shelf_number = input(f'Введите новый номер полки. Уже есть следующие полки: {", ".join(directories_dict.keys())}: ')
    if new_shelf_number not in directories_dict.keys():
        directories_dict[new_shelf_number] = []
        print(f'Полка №{new_shelf_number} добавлена!')
    else:
        print(f'Полка с №{new_shelf_number} уже существует!')


####################################################################################################################
# Альтернативный вариант реализации меню

# menu = {
#     'p': (get_name, (documents,)),
#     'q': (quit, (0,)),
#     'help': (print, ('"p" - узнать имя по номеру документа\n'
#                      '"s" - узнать номер полки по номеру документа\n'
#                      '"q" - выход\n',)),
# }
#
# while True:
#     in_data = input('Введите команду или "q" для выхода. Чтобы узнать список доступных команд, введите "help": ')
#     if in_data in menu:
#         menu.get(in_data)[0](*menu.get(in_data)[1])
#     else:
#         print('Такой команды нет! Чтобы вывести список доступных команд, введите "help"')
#         continue
####################################################################################################################


menu = {
    'p': {'func': get_name, 'args': (documents,)},
    's': {'func': get_shelf, 'args': (directories,)},
    'l': {'func': print_all_documents_to_stdout, 'args': (documents,)},
    'a': {'func': add_document, 'args': (documents, directories)},
    'd': {'func': delete_document, 'args': (documents, directories)},
    'm': {'func': move_document, 'args': (documents, directories)},
    'as': {'func': add_shelf, 'args': (directories,)},
    'q': {'func': quit, 'args': (0,)},
    'help': {'func': print, 'args': ('"p" - узнать имя по номеру документа\n'
                                     '"s" - узнать номер полки по номеру документа\n'
                                     '"l" - вывести на экран список всех документов, отсортированный по заданному ключу\n'
                                     '"a" - добавить новый документ в каталог и на полку\n'
                                     '"d" - удалить документ из каталога и с полки, где он "хранится"\n'
                                     '"m" - переместить документ на другую полку\n'
                                     '"as" - добавить новую полку\n'
                                     '"help" - список команд\n'
                                     '"q" - выход\n',)},
}


def main():
    while True:
        input_data = input('Введите команду или "q" для выхода. Чтобы узнать список доступных команд, введите "help": ')
        if input_data in menu:
            menu_number = menu.get(input_data)
            menu_number.get('func')(*menu_number.get('args'))
        else:
            print('Такой команды нет! Чтобы вывести список доступных команд, введите "help"')
            continue


def summa(a, b):
    return a + b


if __name__ == "__main__":
    main()
