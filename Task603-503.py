# Создайте программу для игры в ""Крестики-нолики"".
from random import randint
from os import system


def print_fiels(list_cell):
    print('     Y0 ', ' Y1 ', ' Y2')
    print('X0', list_cell[0])
    print('X1', list_cell[1])
    print('X2', list_cell[2])


# def cell_letter(count):
#     if count % 2 == 1:
#         cell = 'x'
#     else:
#         cell = '0'
#     return cell


def check_empty(x, y, list_cell):
    if list_cell[x][y] == ' ':
        return True
    # else: return False


def check_win(list_cell):
    win = True
    # С помощью \ мы делаем перенос строки
    if list_cell[0][0] == list_cell[0][1] == list_cell[0][2] != ' ' or \
    list_cell[1][0] == list_cell[1][1] == list_cell[1][2] != ' ' or \
    list_cell[2][0] == list_cell[2][1] == list_cell[2][2] != ' ' or \
    list_cell[0][0] == list_cell[1][0] == list_cell[2][0] != ' ' or \
    list_cell[0][1] == list_cell[1][1] == list_cell[2][1] != ' ' or \
    list_cell[0][2] == list_cell[1][2] == list_cell[2][2] != ' ' or \
    list_cell[0][0] == list_cell[1][1] == list_cell[2][2] != ' ' or \
    list_cell[2][2] == list_cell[1][1] == list_cell[0][0] != ' ':
        return win
    else: return False


system('cls')
list_cell = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print_fiels(list_cell)

status = False
count = 0

while not status and count < 9:
    count += 1
    x, y = 5, 5  # Произвольное число не лежащее между 0 и 2
    while (x < 0 or 2 < x) or (y < 0 or 2 < y):
        print('Введите целое число от 0 до 2')
        x = int(input('Кооринаты хода строка X 0-2: '))
        y = int(input('Координаты хода стлбец Y 0-2: '))
    if check_empty(x, y, list_cell):
        cell_letter = lambda count: 'x' if  count %2 else '0'  #Использовали lambda
        list_cell[x][y] = cell_letter(count)
    else:
        print('Ячейка занята, вы потеряли ход )))))')
    input("Для продолжения нажмите любую клавишу")
    system('cls')
    print_fiels(list_cell)
    status = check_win(list_cell)
    if status:
        print('Victory')
    if count > 9:
        print('Ничья')
