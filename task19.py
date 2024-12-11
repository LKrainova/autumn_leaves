# todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
"""– id - номер по порядку (от 1 до 10);
– текст из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
#
Каждое значение из списка должно находится на отдельной строке.
Выход:
1 % "C4.5"
2 % "k - means"
и т.д."""


# Решение
# РЕШЕНИЕ НЕ РАБОТАЕТ ПРИ ПЕРВОМ ЗАПУСКЕ. ИСПРАВИТЬ!!! 


id = list(range(1,11))
algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

my_file = open('algoritm.csv', 'r+', encoding = 'utf-8 ')

for i in range(len(algoritm)):
    my_file.write(f'{id[i]}, {algoritm[i]}')
    print(f'{id[i]}, {algoritm[i]}')

my_file.close()
