# todo Задача 1. Чтение матрицы, load_matrix(filename)

"""
Дан файл, содержащий таблицу целых чисел вида
(в каждой строке через пробел записаны числа)

11 12 13 14 15 16
21 22 23 24 25 26
31 32 33 34 35 36

Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
Если в каждой строке находится одинаковое количество чисел,
функция возвращает список списков целых чисел.
В противном случае возвращает False.

Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

"""

# Решение

f = open('load_matrix.txt', 'r+')
lines = f.readlines()
f.close()

spisok = [line.split() for line in lines]
#print(spisok)
count = [len(i) for i in spisok]
#print(count)

comp_1 = [print(spisok) if len(set(count)) == 1 else False]
print(comp_1)




