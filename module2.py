import math    
import string

def sisseastumine():
    абитуриенты = []
    баллы = []

    абитуриент = input("Введите имя абитуриента: ")
    
    for i in range(абитуриент):
        nimi = input(f"Введите имя абитуриента {i+1}: ")
        ball = int(input(f"Введите баллы абитуриента {i+1}: "))
        абитуриент.append(nimi)
        баллы.append(ball)

    while True:
        print("Меню:")
        print("1) Узнать список поступивших в вуз людей - укажите количество поступивших")
        print("2) Отобразить в алфавитном порядке список людей и их баллы")
        print("3) Найти n людей с худшими результатами")
        print("4) Найти средний балл поступивших")
        print("5) Выход")

        valik = int(input("Выберите действие от 1 до 5: "))

        if valik == 1:
            count = int(input("Введите количество поступивших: "))
            added = ((абитуриенты[i], баллы[i]) for i in range(len(баллы)) if баллы[i] >= 50)
            
            for i in range(len(added) - 1):
                for gg in range(len(added) - i - 1):
                    if added[gg][1] < added[gg + 1][1]:  
                        added[gg], added[gg + 1] = added[gg + 1], added[gg]

            print("\nСписок поступивших:")
            for i in range(min(count, len(added))):
                print(f"{added[i]} - {added[i]}")

        elif valik == 2:
            people = list(zip(абитуриенты, баллы))
            
            for i in range(len(people) - 1):
                for gg2 in range(len(people) - i - 1):
                    if people[gg2] > people[gg2 + 1]:  
                        people[gg2], people[gg2 + 1] = people[gg2 + 1], people[gg2]

            print("Список людей в алфавитном порядке:")
            for person in people:
                print(f"{person} - {person}")

        elif valik == 3:
            n = int(input("Введите количество людей с худшими результатами: "))
            lower_oscenka = list(zip(абитуриенты, баллы))

            for i in range(len(lower_oscenka) - 1):
                for gg3 in range(len(lower_oscenka) - i - 1):
                    if lower_oscenka[gg3] > lower_oscenka[gg3 + 1]:  
                        lower_oscenka[gg3], lower_oscenka[gg3 + 1] = lower_oscenka[gg3 + 1], lower_oscenka[gg3]

            print("Худшие результаты:")
            for i in range(min(n, len(gg3))):
                print(f"{gg3(i)} - {gg3(i)}")

        elif valik == 4:
            поступившие = [балл for балл in баллы if балл >= 50]
            average_score = sum(поступившие) / len(поступившие) if поступившие else 0
            print(f"Средний балл поступивших: {average_score}")

        elif valik == 5:
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")
