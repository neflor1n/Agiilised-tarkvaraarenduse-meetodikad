def logsKuvamine(logs):
    addition = 0
    subtraction = 0
    multiplication = 0
    division = 0
    for elem in logs:
        if elem == "Сложение":
            addition += 1
        elif elem == "Вычитание":
            subtraction += 1
        elif elem == "Умножение":
            multiplication += 1
        elif elem == "Деление":
            division += 1
    return [addition, subtraction, multiplication, division]


logs = []  

while True:
    print("\n--------------------------- Калькулятор ---------------------------")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Выйти из программы")
    print("------------------------------------------------------------------")

    option = int(input("Выберите операцию (1-5): "))

    if option == 5:
        print("Выход из программы. Пока!")
        break

    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    print("------------------------------------------------------------------")

    match option:
        case 1:
            logs.append("Сложение")
            result = a + b
            print(f"Результат: {a} + {b} = {result}")
        case 2:
            logs.append("Вычитание")
            result = a - b
            print(f"Результат: {a} - {b} = {result}")
        case 3:
            logs.append("Умножение")
            result = a * b
            print(f"Результат: {a} * {b} = {result}")
        case 4:
            logs.append("Деление")
            if b != 0:
                result = a / b
                print(f"Результат: {a} / {b} = {result}")
            else:
                print("Ошибка: деление на ноль!")
                logs.pop()  
                continue
        case _:
            print("Ошибка: неизвестная операция.")
            continue

    print("Статистика операций: [Сложение, Вычитание, Умножение, Деление]")
    print(logsKuvamine(logs))
