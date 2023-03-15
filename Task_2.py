'''
Погружение в Python (семинары)
Урок 2. Простые типы данных
Задание 2.
Напишите программу, которая получает целое число 
и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата.

'''
'''   
extended_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert_to_base_of(num: int, base: int) -> str:
    """convert a decimal number to any base system"""
    return '' if num == 0 else convert_to_base_of(num // base, base) + extended_digits[num % base]

print(f'converted num: {convert_to_base_of(11, 2)}, right res: {bin(11)}')
print(f'converted num: {convert_to_base_of(111, 8)}, right res: {oct(111)}')
print(f'converted num: {convert_to_base_of(1117, 16)}, right res: {hex(1117)}')
print(f'converted num: {convert_to_base_of(111797, 32)}')
'''

num = int(input('Введите целое положительное число: '))
 
s = ''
h = '0123456789ABCDEF'
while num > 0:
    #s = h[num % 16] + s
    s = h[num % 16] + s
    num = num // 16
 
print('Введенное число в шестнадцатеричной системе: ' + s)
print('Проверка полученного результата с помощью функции "hex": ')

print(hex(int(input('Введите то же самое число: ')))[2:].upper())