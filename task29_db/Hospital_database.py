
#todo: Выбрать из файла db_design.pdf вариант задания. Спроектировать ER модель на сайте
# https://editor.ponyorm.com . Сгенерировать скрипт и создать схему для СУБД PostgreSQL.
# Наполнить модель данными. Написать запросы к заданию на стороне клиента python.

'''Задание 7. Больница'''

import psycopg2
import database_config

class Database:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = self.connect()

    def connect(self):
        try:
            return psycopg2.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port,
                database = self.db
            )
        except psycopg2.OperationalError as e_1:
            print('Проблема с подключением: либо вы некорректно ввели данные, либо базы данных не существует, либо прервался интернет')
            print(e_1)
        except psycorg2.ProgrammingError as e_2:
            print('Проверьте правильность вашего SQL-запроса')
            print(e_2)

    def execute(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            query_results = cur.fetchall()
            print(query_results)
            return query_results

        except Exception as query_error:
            print(query_error)

        finally:
            cur.close()


'''Варианты запросов:'''

'''1) Выдавать сведения о мед.работниках'''
q1 = 'select * from doctors;'

'''2) Выдавать сведения обо всех врачах, наблюдающих за определенным пациентом'''

q2 = """select doctors.name, doctors.speciality from doctors
inner join doctors_patients on doctors.id = doctors_patients.id_doctors
inner join patients on doctors_patients.id_patients = patients.id
where patients.full_name = 'Shakira';"""

'''3) Выдавать сведения о пациентах'''
q3 = 'select * from patients;'

'''4) Выдавать сведения обо всех пациентах, наблюдаемых у определенного доктора '''
q4 = """ 
select
patients.full_name,
patients.age,
patients.date_of_admission,
patients.gender,
patients.room_number
from doctors
inner join doctors_patients on doctors.id = doctors_patients.id_doctors
inner join patients on doctors_patients.id_patients = patients.id
where doctors.name = 'Lukasz Kowalczyk'; 
"""

""" Нахождение пациентов по палатам"""
q5 = """   
select full_name, age, date_of_admission, gender
from patients
where room_number like '100%';
"""

db = Database(database_config.host, database_config.port, database_config.user, database_config.password, database_config.db)

results = db.execute(q1)

print(f'Данные по вашему запросу: {results}')

















