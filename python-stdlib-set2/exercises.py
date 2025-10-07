import os
import datetime
import itertools
import math
import collections
import re
import random
import requests
import json

def is_third_tuesday(date):
    """ Проверить, является ли день третьим вторником месяца

    Аргументы:
        - date:str - дата в формате YYYY-MM-DD

    Возвращает:
        - bool

    Пример:
    >>> is_third_tuesday("2022-08-16")
    True

    Указания:
        - использовать библиотеку datetime
        - авторское решение занимает 2 строки
    """
    d = datetime.date.fromisoformat(date)
    return d.weekday() == 1 and 15 <= d.day <= 21

def files_in_dir(directory):
    """ Вернуть список файлов в директории `directory` (без папок)

    Аргументы:
        - directory:str - абсолютный путь к директории

    Возвращает:
        - list: список файлов в директории

    Указания:
        - гарантируется, что такая директория существует
        - использовать модуль os (os.lisdir, os.path.isfile, os.path.join)
        - авторское решение занимает 87 символов
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def permutations(s):
    """ Вернуть список кортежей из всех возможных перестановок множества `s`

    Аргументы:
        - s: множество

    Возвращает:
        - list: список кортежей перестановок

    Пример:
    >>> permutations(set("ABC"))
    [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
    
    Указания:
        - использовать модуль itertools
        - авторское решение занимает 48 символов
    """
    return list(itertools.permutations(s))

def ball_volume(rad):
    """ Вычислить объём шара по его радиусу

    Аргументы:
        - rad:float - радиус шара

    Возвращает:
        - float: объём шара
    
    Указания:
        - число pi можно найти в библиотеке math
        - авторское решение занимает 27 символов
    """
    return 4/3*math.pi*rad**3

def binary2decimal(bin):
    """ Перевести двоичное число в десятичное

    Аргументы:
        - bin:int - двоичное число, состоящее из нулей и единиц

    Возвращает:
        - int: десятичное число

    Указания:
        - можно использовать или не использовать методы itertools, math, map, range, sum
        - авторское решение занимает 98 символов
    """
    return int(str(bin), 2)
    #return sum(int(d) * 2 ** i for i, d in enumerate(reversed(str(bin))))
    #return sum(int(d) * 2 ** i for d, i in zip(reversed(str(bin)), itertools.count()))

def popular_word(text):
    """ Вернуть самое используемое слово в тексте `text`

    Аргументы:
        - text:str - текст

    Возвращает:
        - str: самое повторяющееся слово

    Указания:
        - гарантируется, что такое слово существует и единственно
        - слова считаются одинаковыми, если полностью совпадают с учётом регистра
        - воспользоваться библиотекой collections и re
        - обратить внимание на r-строки
        - авторское решение занимает 66 символов
    """
    return collections.Counter(re.findall(r'\w+', text)).most_common(1)[0][0]
    # находим все слова (последовательности символов, потому r'\w+')
    # извлекаем самый частый элемент, его первый подэлемент

def parse_nobel_json(year):
    """ Используя json базу данных лауреатов Нобелевской премии вернуть 
    `[winner1, ...]` - список фамилий лауреатов Нобелевской премии по физике в году `year`
    Если в json нет данных за запрашиваемый год, то вернуть `None`

    Аргументы:
        - year:int - год вручения Нобелевской премии

    Возвращает:
        - list: список нобелевских лауреатов

    Пример:
    >>> parse_nobel_json(2018)
    ['Ashkin', 'Mourou', 'Strickland']

    Указания:
        - json база лежит по адресу http://api.nobelprize.org/v1/prize.json
        - получить ответ на запрос можно с помощью requests.get
        - обработать ответ можно с помощью json
        - авторское решение занимает 5 строк
    """
    data = requests.get("http://api.nobelprize.org/v1/prize.json").json()
    prizes = [p for p in data["prizes"] if p["year"] == str(year) and p["category"] == "physics"]
    if not prizes:
        return None
    return [laureate.get("surname") for laureate in prizes[0]["laureates"] if "surname" in laureate]

def random_choice(list, n):
    """ Вернуть `n` случайно выбранных элементов без повторений из списка `list`, 
    если `n` не больше длины `list`, иначе вернуть `None`
    
    Аргументы:
        - list:list - список объектов
        - n:int - количество объектов

    Возвращает:
        - list - список случайно выбранных объектов
    
    Указания:
        - использовать библиотеку random
        - авторское решение занимает 57 символов
    """
    return random.sample(list, n) if n <= len(list) else None

def calculate_age(birthday):
    """ Вернуть возраст человека (в годах) на сегодняшний день

    Аргументы:
        - birthday:str - дата рождения в формате YYYY-MM-DD

    Возвращает:
        - int
    
    Указания:
        - использовать библиотеку datetime
        - авторское решение занимает 2 строки
    """
    bd = datetime.date.fromisoformat(birthday)
    return datetime.date.today().year - bd.year - ((datetime.date.today().month, datetime.date.today().day) < (bd.month, bd.day))

def iterable_deque(iterable):
    """ Создать из итерируемого объекта (список, кортеж, строка) `deque`, добавить в его начало число 10 и вернуть

    Аргументы:
        - iterable - итерируемый объект

    Возвращает:
        - deque
    
    Пример:
    >>> iterable_deque(['a', 'b', 'c'])
    deque([10, 'a', 'b', 'c'])

    Указания:
        - использовать библиотеку collections
        - авторское решение занимает 3 строки
    """
    d = collections.deque(iterable)
    d.appendleft(10)
    return d

if __name__=="__main__":
    print( is_third_tuesday("2022-08-16") )
    print( files_in_dir(os.getcwd()) )
    print( permutations(set("ABC")) )
    print( ball_volume(1) ) # 4.1887...
    print( binary2decimal(101) ) # 5
    print( popular_word("The first, the second, the third") ) # the
    print( parse_nobel_json(2018) )
    print( random_choice([1, 2, 3, 4, 5], 2) )
    print( calculate_age("1997-01-01") ) #25 (если сейчас 2022 год)
    print( iterable_deque((1, 2, 3, 4)) )
