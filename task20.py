#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

"""Содержимое файла import_this.txt

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

выходные данные:
Complex is better than complicated.
Simple is better than complex.
Explicit is better than implicit.
Beautiful is better than ugly."""



# Решение:

# Сначала создадим сам файл и запишем туда текст:

my_file = open('import_this.txt', 'w+')
orwell = f'''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
my_file.write(orwell)
my_file.close()


# Потом считаем файл построчно:

line_reading = open('import_this.txt', 'r+')
lines = line_reading.readlines()
for i in lines:
    print(i)
line_reading.close()


# И выведем строки наоборот:

line_reading = open('import_this.txt', 'r+')
lines = line_reading.readlines()
for i in lines[::-1]:
    print(i)
line_reading.close()
