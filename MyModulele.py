import math    # ввод математических и строковых комманд
import string

usernames = []  # список пользователей
passwords = []  # список паролей

def login():        # создание функции login
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    if username in usernames and passwords[usernames.index(username)] == password:   # если username есть в usernames и пароль соответств той позиции username из usernames, в которую он вложен
        print("Вы успешно вошли!")
    else:
        print("Неверный логин или пароль.")

def register():   # создание функции register
    username = input("Введите логин для регистрации: ")   # запрос имени
    if username in usernames:   # если есть username в usernames, тогда невозможно рег
        print("Этот логин уже занят.")
    else:
        password = input("Введите пароль для регистрации: ")
        usernames.append(username)    # добавляет в конец новый username в usernames
        passwords.append(password)    # добавляет в конец новый пароль в passwords
        print(f"Пользователь {username} успешно зарегистрирован!")

def change_password():      # создание функции change_password
    username = input("Введите логин для смены пароля: ")
    if username in usernames:    # если есть username в usernames
        old_password = input("Введите старый пароль: ")      # треюуется ввести старый пароль, чтобы сделать новый
        if passwords[usernames.index(username)] == old_password:  # если пароль соответств паролю, приаязанному к username, то предлагает сменить
            new_password = input("Введите новый пароль: ")
            passwords[usernames.index(username)] = new_password   # смена пароля на новый
            print("Пароль успешно изменен.")
        else:
            print("Неверный старый пароль.")
    else:
        print("Пользователь не найден.")

def recover_password():    # создание функции recover_password
    username = input("Введите логин для восстановления пароля: ")
    if username in usernames:
        print(f"Ваш пароль: {passwords[usernames.index(username)]}")   # если есть username в usernames, тогда показывает пароль, который соответств позиции этого пользователя
    else:
        print("Пользователь не найден.")
