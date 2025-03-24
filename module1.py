import MyModulele

usernames = []
passwords = []

def main():
    while True:
        print("Добро пожаловать в программу!")
        print("Войдите или зарегистрируйтесь")
        print("1 - Войти")
        print("2 - Зарегистрироваться")
        print("3. Смена пароля")
        print("4. Восстановление пароля")
        print("5. Выход")

        try:
            choice = int(input("Выберите пункт: "))
        except ValueError:
            print("Ошибка! Введите число.")
            continue
        
        if choice == 1:
            MyModulele.login()
        elif choice == 2:
            MyModulele.register()
        elif choice == 3:
            MyModulele.change_password()
        elif choice == 4:
            MyModulele.recover_password()
        elif choice == 5:
            print("Выход из программы.")
            break  
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
