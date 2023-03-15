'''
Погружение в Python (семинары)
Урок 2. Простые типы данных
Задание 3.
Напишите программу, которая принимает две строки вида 
“a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions.
'''

from math import lcm, gcd
import fractions

str_1 = input('Введите первую дробь (к примеру: 3/4): ')
str_2 = input('Введите вторую дробь (к примеру: 5/6): ')

a, b = map(int, str_1.split('/'))
c, d = map(int, str_2.split('/'))

# Находим сумму
if b == d:
    g = a + c
    f = b
else:
    f = lcm(b, d)
    g = a * f / b + c * f / d

divisor = gcd(int(g), f)
if divisor:
    g /= divisor
    f /= divisor

result = f'{int(g / f)}' if not g % f else f'{int(g)}/{int(f)}'

print(f'Сумма дробей: {result}')

# Находим произведение
g = a * c
f = d * b

divisor = gcd(int(g), f)
if divisor:
    f /= divisor
    g /= divisor

result = f'{int(g / f)}' if not g % f else f'{int(g)}/{int(f)}'

print(f'Произведение дробей: {result}')
print('-' * 30)
print('Проверка через модуль Fraction')
fraction_1 = fractions.Fraction(a, b)
fraction_2 = fractions.Fraction(c, d)
print(f'Сумма дробей: {fraction_1 + fraction_2}')
print(f'Произведение дробей: {fraction_1 * fraction_2}')