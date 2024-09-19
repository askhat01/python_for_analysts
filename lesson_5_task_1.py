import os

print('Задача 1')
string = "C:/Askhat/Desktop/GreekBrains/python_advanced/seminar_5.py"

def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходная строка: {string} \nКортеж из пути: {fun(string)}')