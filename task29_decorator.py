from datetime import datetime

def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1

        """Инфа по функции"""
        result = fn(*args, **kwargs)

        """Инфа по времени вызова"""
        func_calling_moment = datetime.now() # Формат отстой
        func_calling_time = func_calling_moment.strftime('%d.%m.%Y, в %H.%M.%S')
        """Собственно, само сообщение (которое нам надо записать в лог-файл!)"""
        log_txt = str(f'Функция {fn.__name__} была вызвана {wrapper.counter} раз(а), {func_calling_time}. \n')
        write_the_log(log_txt)
        return result

    wrapper.counter = 0

    return wrapper


def write_the_log(self):
    with open('debug.log', 'a+', encoding = 'utf-8') as f:
        f.write(self)


@logging_decorator
def substract(a,b):
    result = a - b
    return result

@logging_decorator
def add(a,b,c):
    result = a + b + c
    return result

@logging_decorator
def bird_singing(zwik_type_1, zwik_type_2):
    print(f'What does the bird say??? It says {zwik_type_1}, {zwik_type_2}')


add(82,9000, 315)
add(900,228, 800)
substract(100,480)
substract(100,480)
substract(100,480)
bird_singing('Zwick-zwirick!', "Zwirr, zwirr!")
bird_singing('Zwick-zwirick!', "Zwirr, zwirr!")
bird_singing('Zwick-zwirick!', "Zwirr, zwirr!")
bird_singing('Zwick-zwirick!', "Zwirr, zwirr!")
bird_singing('Zwick-zwirick!', "Zwirr, zwirr!")