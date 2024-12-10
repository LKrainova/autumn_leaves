#todo: Модифицировать программу таким образом чтобы она выводила
#  приветствие "Hello", которое до этого записано в файл text.txt
#  через метод write()

"""f = open("text.txt", "w+t")
f.write("Hello\n")"""


# Решение

# То есть нам надо, чтобы программа могла ещё и читать файл, а не только записывать

# Это мы создали файл (ну и заодно сделали запись в него)

f = open("text.txt", "w+")
f.write("Hello\n")
f.close()

# А теперь прочитаем!

my_file = open('text.txt', 'r+')
my_reading = my_file.read()
print(my_reading)
my_file.close()
