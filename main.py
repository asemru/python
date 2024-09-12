import sys
from pprint import *
from inspect import getmodule
import math

def introspection_info(obj):
    a = {'type': type(obj).__name__}
    try:
        a['модуль'] = obj.__module__
    except:
        a['модуль'] = '__main__'
    a['методы'] = dir(obj)[0], dir(obj)[1] #Выводит только два первых так как если вывести всё то в консоль выведится очень длиная строка
    try:
        a['атрибуты'] = vars(obj)
    except:
        a['атрибуты'] = '[...]'

    return a



number_info = introspection_info(42)
print(number_info)







