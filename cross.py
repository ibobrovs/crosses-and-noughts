# План написания:
# 1. среда (поле, границы)
# 2. объекты (X и 0)
# 3. взаимолействие с игроком (ввод хода, вывод результата)

#1.
field = [[" "] * 3 for i in range(3) ]

def show():
    print()
    print('    | 0 | 1 | 2 | ')
    print('  --------------- ')
    for i, row in enumerate(field):
        row_str = f'  {i} | {' | '.join(row)} | '
        print(row_str)
        print('  --------------- ')
    print()

show()

# 2.

def ask():
    while True:
        x, y = map(int, input(' Ход:').split())

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(' Координаты расположены вне поля')
            continue

        if field[x][y] != " ":
            print(' Ячейка занята')
            continue

        return x, y


ask()

def ask():
    while True:
        coords = input(' Ход:').split()

        if len(coords) != 2:
            print(' Используйте только 2 числа')
            continue

        x, y = coords

        if not (x.isdigit()) or not (y.isdigit()):
            print(' Используйте только 2 числа')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(' Координаты расположены вне поля')
            continue

        if field[x][y] != " ":
            print(' Ячейка занята')
            continue
        return x, y


ask()


 # 3.

def win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_coord:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print('Выиграл X!')
            return True
        if symbols == ["0", "0", "0"]:
            print('Выиграл 0!')
            return True
    return False
field = [' x'] * 3



field = [
    [" ", "X", " "],
    [" ", "X", " "],
    [" ", "X", " "]
]

win()
