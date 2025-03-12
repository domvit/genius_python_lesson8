# Завдання 1: Інкапсуляція
#
# Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):
#
# Ім'я (name) Електронна пошта (email) Пароль (password) Напишіть публічні методи для установки
# і отримання значень цих полів (геттери і сеттери). Потім створіть об'єкт класу "Користувач"
# і встановіть значення полів, а також виведіть їх на екран.

class User:
    def __init__(self):
        self.__name = None
        self.__email = None
        self.__password = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password


user = User()
user.set_name("Олександр")
user.set_email("olexandr@example.com")
user.set_password("secure123")

print("Ім'я:", user.get_name())
print("Електронна пошта:", user.get_email())
print("Пароль:", user.get_password())