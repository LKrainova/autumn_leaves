#todo: Функция logger(), которая записывает текст сообщения об ошибке
# в файл test.log

import datetime

FILE_LOG = 'test.log' # Создаём файл, куда будут писаться ошибки

# Задаём функции параметры (сами придумали)

# message_ - то, что будем писать про ошибку, line - на какой строчке встретилась,
# code - дополнительный код для категоризации сообщения об ошибке,
# file - имя файла, в котором была зафиксирована ошибка

# Это всё только определение функции, без запуска

def logger(message_, error_type, line, code, file):
    time = datetime.datetime.now() # Даёт время, которое сейчас
    fd = open(FILE_LOG, 'a', encoding='utf-8') # Открываем файл в режиме append (дозапись)
    error = f"{error_type}; {time}; {code}; {line}; {__file__}; {message_}"
    fd.write(error + '\n')
    fd.close()

# А вот это уже запуск, причём только если мы запускаем из этого же скрипта

if __name__ == '__main__':
    logger(error_type = "ZWIRR!",
           code = 888,
           file = __file__,
           line = 31,
           message_ = "I have done a new record!")





