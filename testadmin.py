class Admin(object):
    instance = None
    login = None
    password = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Admin, cls).__new__(cls)
            cls.login = input("Задайте логин: ")
            cls.password = input("Задайте пароль: ")
        return cls.instance
    def getID(self):
        return self.login

x = Admin()
y = Admin()
f = Admin()

print('Проверка')
print(x is y)
print(f.getID())