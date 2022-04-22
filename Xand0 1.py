import random


def hello():
    print("------------------------------")
    print("            X and O           ")
    print("------------------------------")
    print("          начнем игру         ")
    print("       люди против машин      ")
    print("------------------------------")
    print("       формат ввода: x y      ")
    print("      x - номер строки        ")
    print("      y - номер столбца       ")
    print("--------------------1.0-by-ZAV")


def bye():
    print()
    print("------------------------------")
    print("        Спасибо за игру       ")
    print("        до новых встреч       ")
    print("--------------------1.0-by-ZAV")


def xando():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, line in enumerate(field):
        line_str = "  " + str(i) + " | " + ' | '.join(line) + " |"  # извените что не f строка
        print(line_str)
        print("  --------------- ")


def refield():
    win_line[0] = field[0]
    win_line[1] = field[1]
    win_line[2] = field[2]
    for i in range(3):
        win_line[3][i] = field[i][0]
        win_line[4][i] = field[i][1]
        win_line[5][i] = field[i][2]
        win_line[6][i] = field[i][i]
        win_line[7][i] = field[i][~i]


def h_con():
    while True:
        cords = input(" Введите x y: ").split()

        if len(cords) != 2:  # воспринимает 2 символа - 2 числа по 1 символу (отрицательное число ввести не возможно)
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

        field[x][y] = "X"
        refield()
        break


def reline(line: int):
    if 0 <= line <= 2:
        field[line] = win_line[line]

    if line == 3:
        for i in range(3):
            field[i][0] = win_line[3][i]

    if line == 4:
        for i in range(3):
            field[i][1] = win_line[4][i]

    if line == 5:
        for i in range(3):
            field[i][2] = win_line[5][i]

    if line == 6:
        for i in range(3):
            field[i][i] = win_line[6][i]

    if line == 7:
        for i in range(3):
            field[i][~i] = win_line[7][i]

    refield()


def ii_con():
    i_xod = 0
    for i in range(8):
        if win_line[i] == [" ", "0", "0"]:
            win_line[i][0] = "0"
            i_xod = 1
            reline(i)
            break

        if win_line[i] == ["0", " ", "0"]:
            win_line[i][1] = "0"
            i_xod = 2
            reline(i)
            break

        if win_line[i] == ["0", "0", " "]:
            win_line[i][2] = "0"
            i_xod = 3
            reline(i)
            break

        if win_line[i] == [" ", "X", "X"]:
            win_line[i][0] = "0"
            i_xod = 4
            reline(i)
            break

        if win_line[i] == ["X", " ", "X"]:
            win_line[i][1] = "0"
            i_xod = 5
            reline(i)
            break

        if win_line[i] == ["X", "X", " "]:
            win_line[i][2] = "0"
            i_xod = 6
            reline(i)
            break

    if i_xod == 0:
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if field[x][y] == " ":
                field[x][y] = "0"
                refield()
                break


def check_win():
    for i in range(8):
        if win_line[i] == ["X", "X", "X"]:
            print()
            print("        !!! ПОБЕДА !!!          ")
            print("   Игрок победил компьютер !!!  ")
            return True

        if win_line[i] == ["0", "0", "0"]:
            print()
            print("        !!! ПОБЕДА !!!          ")
            print("  Компьютер победил игрока !!!  ")
            return True

    return False


# тело программы
hello()
field = [[" "] * 3 for i in range(3)]
win_line = [[" "] * 3 for j in range(8)]
xando()
con = 0
while True:
    con += 1

    if con % 2 == 1:
        print(" Ход Игрока!")
        h_con()

    else:
        print(" Ход Компьютера!")
        ii_con()

    xando()

    if check_win():
        break

    if con == 9:
        print()
        print("Поздравляю Ничья!")
        break

bye()
