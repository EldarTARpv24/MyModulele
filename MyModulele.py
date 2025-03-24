import math    # ввод математических и строковых комманд
import string

usernames = []  # список пользователей
passwords = []  # список паролей

def login():        # создание функции login
    username = input("Sisestage sisselogimine: ")
    password = input("Sisestage parool: ")

    if username in usernames and passwords[usernames.index(username)] == password:   # если username есть в usernames и пароль соответств той позиции username из usernames, в которую он вложен
        print("Olete edukalt sisse loginud!")
    else:
        print("Vale sisselogimine või parool.")

def register():   # создание функции register
    username = input("Registreerimiseks sisestage oma sisselogimine: ")   # запрос имени
    if username in usernames:   # если есть username в usernames, тогда невозможно рег
        print("See sisselogimine on juba hõivatud.")
    else:
        password = input("Registreerimiseks sisestage parool: ")
        usernames.append(username)    # добавляет в конец новый username в usernames
        passwords.append(password)    # добавляет в конец новый пароль в passwords
        print(f"Kasutaja {username} edukalt registreeritud!")

def change_password():      # создание функции change_password
    username = input("Parooli muutmiseks sisestage sisselogimine: ")
    if username in usernames:    # если есть username в usernames
        old_password = input("Sisestage vana parool: ")      # треюуется ввести старый пароль, чтобы сделать новый
        if passwords[usernames.index(username)] == old_password:  # если пароль соответств паролю, приаязанному к username, то предлагает сменить
            new_password = input("Sisestage uus parool: ")
            passwords[usernames.index(username)] = new_password   # смена пароля на новый
            print("Parooli muutmine õnnestus.")
        else:
            print("Vale vana parool.")
    else:
        print("Kasutajat ei leitud.")

def recover_password():    # создание функции recover_password
    username = input("Parooli taastamiseks sisestage oma sisselogimine: ")
    if username in usernames:
        print(f"Teie parool: {passwords[usernames.index(username)]}")   # если есть username в usernames, тогда показывает пароль, который соответств позиции этого пользователя
    else:
        print("Kasutajat ei leitud.")
