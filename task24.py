# todo: Числа в буквы
"""
Замените числа, написанные через пробел, на буквы. Не числа не изменять.

Пример.
Input	                            Output
8 5 12 12 15	                    hello
8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

"""

# Сгенерируем английский алфавит

from string import ascii_lowercase
alph = list(ascii_lowercase)
print(alph)

# У нас 0 - это пробел, добавим его вручную

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Создадим словарь, где ключом будет цифра, а значением - буква из алфавита.

dictionary = {k:v for k,v in enumerate(alphabet)}
print(dictionary)

# Делаем список из строки

line_a = '8 5 12 12 15 , 0 23 15 18 12 4 !'
line = [i for i in line_a.split()]
print(line)
'''line = ['8', '5', '12', '12', '15', ',', '0', '23', '15', '18', '12', '4', '!']'''

# Итерируемся по словарю, если цифра в словаре, переводим её в букву,
# если другой элемент, оставляем, как есть

list = [dictionary[int(i)] if i.isdigit() and int(i) in dictionary else i for i in line]
print(list)
final = ''.join(list)
print(final)
