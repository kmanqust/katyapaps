import datetime
import sqlite3
import random
import math


class User():
    def __init__(self, FirstName: str, LastName: str, Card_id: int):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Card_id = Card_id
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO User (firstname, lastname, card_id) VALUES ('{FirstName}', '{LastName}', {Card_id})")
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM User WHERE card_id = {self.Card_id}")
        conn.commit()
        conn.close()
        del self

    def CreateEx(self, Ex: float, Time: datetime.date, cat: str):
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO Expense (card_id, expense, time, category) VALUES ({self.Card_id}, {Ex}, '{Time}', '{cat}')")
        conn.commit()
        conn.close()

    def CreateIn(self, In: float, Time: datetime.date, cat: str):
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO Income (card_id, income, time, category) VALUES ({self.Card_id}, {In}, '{Time}', '{cat}')")
        conn.commit()
        conn.close()

    def DeleteEx(self, Ex: float, Time: datetime.date, cat: str):
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute(
            f"DELETE FROM Expense WHERE card_id = {self.Card_id} AND expense = {Ex} AND time = '{Time}' AND category = '{cat}'")
        conn.commit()
        conn.close()

    def DeleteIn(self, In: float, Time: datetime.date, cat: str):
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute(
            f"DELETE FROM Income WHERE card_id = {self.Card_id} AND income = {In} AND time = '{Time}' AND category = '{cat}'")
        conn.commit()
        conn.close()

    def EditEx(self, Ex: float, Time: datetime.date, cat: str, Ex1: float, Time1: datetime.date, cat1: str):
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE Expense SET expense = {Ex1}, time = '{Time1}', category = '{cat1}' WHERE expense = {Ex} AND time = '{Time}' AND category = '{cat}'")
        conn.commit()
        conn.close()

    def EditIn(self, In: float, Time: datetime.date, cat: str, In1: float, Time1: datetime.date, cat1: str):
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE Expense SET expense = {In1}, time = '{Time1}', category = '{cat1}' WHERE expense = {In} AND time = '{Time}' AND category = '{cat}'")
        conn.commit()
        conn.close()


class BankAPI:
    def getInfo(self, card_id):
        conn = sqlite3.connect('Bank.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Bank WHERE card_id = {card_id}")
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        for result0 in result:
            self.__InsertData(result0)

    def __InsertData(self, result0):
        conn = sqlite3.connect('paps.db')
        cursor = conn.cursor()
        if result0[1] < 0:
            cursor.execute(
                f"INSERT INTO Expense (card_id, expense, time, category) VALUES ({result0[0]}, {math.fabs(result0[1])}, '{result0[2]}', '{result0[3]}')")
        else:
            cursor.execute(
                f"INSERT INTO Income (card_id, income, time, category) VALUES ({result0[0]}, {result0[1]}, '{result0[2]}', '{result0[3]}')")
        conn.commit()
        conn.close()


class Generator:
    def RandomUser(self):
        pass

    def UserCreate(self, card_id):
        pass


class GeneratorSQL:
    def RandomUser(self):
        card_id = random.randint(1000000000000000, 9999999999999999)
        money0 = random.randint(0, 9) / 10
        if random.randint(0, 1) == 1:
            money1 = 0 - random.randint(100, 10000)

        else:
            money1 = random.randint(100, 10000)
        money = money1 + money0
        start_date = datetime.date(2010, 1, 1)
        end_date = datetime.date.today()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        if random.randint(0, 1) == 1:
            cat = "Прочее"
        else:
            cat = "Работа"
        conn = sqlite3.connect('Bank.db')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO Bank (card_id, money, time, category) VALUES ({card_id}, {money}, '{random_date}', '{cat}')")
        conn.commit()
        conn.close()

    def UserCreate(self, card_id):
        money0 = random.randint(0, 9) / 10
        if random.randint(0, 1) == 1:
            money1 = 0 - random.randint(100, 10000)
        else:
            money1 = random.randint(100, 10000)
        money = money1 + money0
        start_date = datetime.date(2010, 1, 1)
        end_date = datetime.date.today()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        if random.randint(0, 1) == 1:
            cat = "Прочее"
        else:
            cat = "Работа"
        conn = sqlite3.connect('Bank.db')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO Bank (card_id, money, time, category) VALUES ({card_id}, {money}, '{random_date}', '{cat}')")
        conn.commit()
        conn.close()


class GeneratorTXT:
    def RandomUser(self):
        card_id = random.randint(1000000000000000, 9999999999999999)
        money0 = random.randint(0, 9) / 10
        if random.randint(0, 1) == 1:
            money1 = 0 - random.randint(100, 10000)

        else:
            money1 = random.randint(100, 10000)
        money = money1 + money0
        start_date = datetime.date(2010, 1, 1)
        end_date = datetime.date.today()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        if random.randint(0, 1) == 1:
            cat = "Прочее"
        else:
            cat = "Работа"
        with open('Info.txt', 'a') as file:
            file.write(f'{card_id}, {money}, {random_date}, {cat} \n')

    def UserCreate(self, card_id):
        money0 = random.randint(0, 9) / 10
        if random.randint(0, 1) == 1:
            money1 = 0 - random.randint(100, 10000)
        else:
            money1 = random.randint(100, 10000)
        money = money1 + money0
        start_date = datetime.date(2010, 1, 1)
        end_date = datetime.date.today()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        if random.randint(0, 1) == 1:
            cat = "Прочее"
        else:
            cat = "Работа"
        with open('Info.txt', 'a') as file:
            file.write(f'{card_id}, {money}, {random_date}, {cat} \n')

class Generator:
    def __init__(self):
        self.state = GeneratorSQL()

    def RandomUser(self):
        self.state.RandomUser()

    def User(self, card_id):
        self.state.UserCreate(card_id)

    def change_state(self, generator):
        self.state = generator

gen0 = GeneratorSQL()
gen1 = GeneratorTXT()
generator = Generator() # По умолчания создается SQL Генератор
generator.change_state(gen1) # Заменяем генератор SQL на генератор TXT
generator.RandomUser()

# DELETE FROM User WHERE card_id LIKE '%%'
# DELETE FROM Income WHERE card_id LIKE '%%'
# DELETE FROM Expense WHERE card_id LIKE '%%'
