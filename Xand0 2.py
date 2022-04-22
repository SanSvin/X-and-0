def hello():
    print("---------------------------")
    print("          X and O          ")
    print("---------------------------")
    print("        начнем игру        ")
    print("  крестики против ноликов  ")
    print("---------------------------")
    print("     формат ввода: x y     ")
    print("    x - номер строки       ")
    print("    y - номер столбца      ")
    print("-----------------2.0-by-ZAV")

def bye():
    print()
    print("---------------------------")
    print("      Спасибо за игру      ")
    print("      до новых встреч      ")
    print("-----------------2.0-by-ZAV")

def xando():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, line in enumerate(field):
        line_str = "  " + str(i) + " | " + ' | '.join(line) + " |"  # извените что не f строка
        print(line_str)
        print("  --------------- ")
    print()

def inxy():
    while True:
        cords = input(" Введите x y: ").split()

        if len(cords) != 2:
            print("Что-то пошло не так!  :( ")
            print("Пожалуйста введите 2 координаты!")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Что-то пошло не так!  :( ")
            print("Пожалуйста введите числа!")
            continue

        x, y = int(x), int(y)

        if x > 2 or y > 2:  # отрицательные значения не возможно ввести isdigit "-" не воспринимает как число
            print("Что-то пошло не так!  :( ")
            print("Пожалуйста введите координаты в диапозоне 0...2")
            continue

        if field[x][y] != " ":
            print("Извените  :( ")
            print("Поле уже занято!")
            continue

        return x, y

def check_win():
    for i in range(8):
       if win_line[i] == ["X", "X", "X"]:
            print()
            print("        !!! ПОБЕДА !!!           ")
            print("Поздравляем команду Крестиков !!!")
            return True

       if win_line[i] == ["0", "0", "0"]:
            print()
            print("       !!! ПОБЕДА !!!          ")
            print("Поздравляем команду Ноликов !!!")
            return True

    return False

# тело программы
hello()
field = [[" "] * 3 for i in range(3)]

win_line = [[" "] * 3 for i in range(8)]
win_line[0] = field[0]
win_line[1] = field[1]
win_line[2] = field[2]

for i in range(3):
    win_line[3][i] = field[i][0]
    win_line[4][i] = field[i][1]
    win_line[5][i] = field[i][2]
    win_line[6][i] = field[i][i]
    win_line[7][i] = field[i][~i]

count = 0
while True:
    count += 1
    xando()
    if count % 2 == 1:
        print(" Ход Крестиков!")
    else:
        print(" Ход   Ноликов!")

    x, y = inxy()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print()
        print("Поздравляю у Вас Ничья!")
        break

bye()