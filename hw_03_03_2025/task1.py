# Задание 1. Разработка и тестирование системы управления пользователями
#  Описание: Разработайте класс User, который хранит информацию о пользователе
# (имя, email, возраст). Затем создайте класс UserManager, который управляет
# пользователями: добавляет их, удаляет и ищет по email.
#  Что нужно сделать:
# • Реализовать классы User и UserManager.
# • Написать модульные тесты для проверки работы:
# o Добавления и удаления пользователей.
# o Поиска пользователей по email.
# o Обработки ошибок (например, добавления пользователя с уже
# существующим email).

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f'{self.name}, {self.email}, {self.age}'

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email, age):
        new_user = User(name, email, age)
        for user in self.users:
            if user.email == email:
                return 'Пользователь с таким email существует'
        self.users.append(new_user)
        return self.users
    
    def del_user(self, ind):
        self.users.pop(ind)
        return self.users
    
    def search_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return 'Такой email существует'
        return 'Такого email нету'

# user_manager = UserManager()
# user_manager.add_user('John', 'superpsina@hotmail.com', 42)
# print(user_manager.add_user('John', 'superpsina@hotmail.com', 42))

# # user_manager.add_user('обама', 'obama@hotmail.com', 5)
# # user_manager.add_user('Я', 'myemail.ru', 'я не помню')

# # user_manager.del_user(1) # удалили обаму
# # print(user_manager.search_by_email('superpsina@hotmail.com'))
# # user_manager.search_by_email('obama@hotmail.com')
# print(user_manager.users)