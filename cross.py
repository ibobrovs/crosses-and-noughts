# План написания:
# 1. среда (поле, границы)
# 2. объекты (X и 0)
# 3. взаимолействие с игроком (ввод хода, вывод результата)

# 1.
table = [
    [ ' ', ' ', ' '],
    [ ' ', ' ', ' '],
    [ ' ', ' ', ' ']
]
def field():
    print()
    print('   | 0 | 1 | 2 | ')
    print('  -------------')
    for i, row in enumerate(table):
        row_str = f' {i} | {'| '.join(row)} | '
        print(row_str)
        print('  -------------')
    print()
field()

# 2.

def coord():
    while True:
        x, y = map(int, input(' Ход:').split())

        if 0 > x or 2 < y or 0 > y or 2 < y:
            print(' Координаты расположены вне поля!')
        if len(x, y) != 2:
            print(' Используйте только 2 числа')
        continue
    return x, y
coord()

# 3.

def result():
    res_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 (0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2))
    for coord in res_coord:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbol == ['X', 'X', 'X']:
            print('Выиграл X!')
        if symbol == ['0', '0', '0']:
            print('Выиграл 0!')
field = [' x'] * 3