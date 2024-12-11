#todo: Задан словарь, его значения необходимо внести по соответвующим тегам и атрибутам
# вместо вопросов (?)
# заполненный шаблон записать в файл index.html.

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""


# Решение
# ЗАДАЧА НЕ РЕШЕНА! ПОДСТАНОВКА ПЕРЕМЕННЫХ ДОЛЖНА ОСУЩЕСТВЯТЬСЯ ПО ПЕРЕМЕЩЕНИЮ КАРЕТКИ В ФАЙЛЕ НА БАЗЕ 
# ШАБЛОНА template

# 1. Вносим в наш шаблон данные из словаря:

my_template = f""" 
<!DOCTYPE HTML>
<html>
 <head>
  <title> {page['title']} </title>
  <meta charset={page['charset']}>
 </head>
 <body onload="alert({page['alert']})">

  <p>{page['p']}</p>

 </body>
</html>
"""

print(my_template) # Проверили, что всё внеслось


# 2. Создаём файл index.html и записываем в него заполненный шаблон

my_file = open('index.html', 'w+', encoding='utf-8')
my_file.write(my_template)
my_file.seek(0) # Переместили курсор в начало после прочтения (хотя вроде и без этой команды работает?)
print(my_file.read())
my_file.close()
