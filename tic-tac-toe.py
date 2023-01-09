def choose_turn(arr):
    print("Выберете поле:")
    i, j = map(int, input().split())

    arr[i - 1][j - 1] = 'X'


def win_condition(i, j, arr):
    if arr[i][j - 1] == arr[i][(j + 1) % 3] == 'O':
        return True
    elif arr[i][(j + 1) % 3] == arr[i][j - 1] == 'O':
        return True
    elif arr[i - 1][j] == arr[(i + 1) % 3][j] == 'O':
        return True
    elif arr[(i + 1) % 3][j] == arr[i - 1][j] == 'O':
        return True
    elif arr[i - 1][j - 1] == arr[(i + 1) % 3][(j + 1) % 3] == 'O':
        return True
    elif arr[i - 1][(j + 1) % 3] == arr[(i + 1) % 3][j - 1] == 'O':
        return True

    return False


def def_condition(arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == '':
                continue
            else:
                if i == 1 and j == 1:
                    # central point
                    if arr[i][j] == arr[i - 1][j - 1] == 'X' and arr[i + 1][j + 1] != 'O':
                        arr[i + 1][j + 1] = 'O'
                        return
                    elif arr[i][j] == arr[i - 1][j + 1] == 'X' and arr[i + 1][j - 1] != 'O':
                        arr[i + 1][j - 1] = 'O'
                        return
                    elif arr[i][j] == arr[i + 1][j - 1] == 'X' and arr[i - 1][j + 1] != 'O':
                        arr[i - 1][j + 1] = 'O'
                        return
                    elif arr[i][j] == arr[i + 1][j + 1] == 'X' and arr[i - 1][j - 1] != 'O':
                        arr[i - 1][j - 1] = 'O'
                        return
                    elif arr[i][j] == arr[i][j + 1] == 'X' and arr[i][j - 1] != 'O':
                        arr[i][j - 1] = 'O'
                        return
                    elif arr[i][j] == arr[i][j - 1] == 'X' and arr[i][j + 1] != 'O':
                        arr[i][j + 1] = 'O'
                        return
                    elif arr[i][j] == arr[i + 1][j] == 'X' and arr[i - 1][j] != 'O':
                        arr[i - 1][j] = 'O'
                        return
                    elif arr[i][j] == arr[i - 1][j] == 'X' and arr[i + 1][j] != 'O':
                        arr[i + 1][j] = 'O'
                        return

                else:
                    # other points
                    if arr[i][j] == arr[i][(j + 1) % 3] == 'X' and arr[i][(j + 2) % 3] != 'O':
                        arr[i][(j + 2) % 3] = 'O'
                        return
                    elif arr[i][j] == arr[i][j - 1] == 'X' and arr[i][j - 2] != 'O':
                        arr[i][j - 2] = 'O'
                        return
                    elif arr[i][j] == arr[(i + 1) % 3][j] == 'X' and arr[(i + 2) % 3][j] != 'O':
                        arr[(i + 2) % 3][j] = 'O'
                        return
                    elif arr[i][j] == arr[i - 1][j] == 'X' and arr[i - 2][j] != 'O':
                        arr[i - 2][j] = 'O'
                        return

    a, b = randint(0, 2), randint(0, 2)
    if arr[a][b] == 'X':
        while arr[a][b] != '':
            a, b = randint(0, 2), randint(0, 2)
    arr[a][b] = 'O'
    return


def variants_of_turn(arr):
    win = False
    i_win, j_win = None, None

    for i in range(3):
        for j in range(3):
            if arr[i][j] != '':
                continue
            else:
                if win_condition(i, j, field):
                    win = True
                    i_win = i
                    j_win = j
    if win:
        arr[i_win][j_win] = 'O'
        return
    else:
        def_condition(arr)


def end_game(arr):
    for i in range(3):
        if arr[i].count('X') == 3:
            print('You win! Congratulations!')
            sys.exit()
        elif arr[i].count('O') == 3:
            print('You lose! Try again!')
            sys.exit()

    for j in range(3):
        mas = ['', '', '']
        for i in range(3):
            mas[i] = arr[i][j]

        if mas.count('X') == 3:
            print('You win! Congratulations!')
            sys.exit()
        elif mas.count('O') == 3:
            print('You lose! Try again!')
            sys.exit()

    if arr[0][0] == arr[1][1] == arr[2][2] == 'X':
        print('You win! Congratulations!')
        sys.exit()
    elif arr[0][2] == arr[1][1] == arr[2][0] == 'X':
        print('You win! Congratulations!')
        sys.exit()
    elif arr[0][0] == arr[1][1] == arr[2][2] == 'O':
        print('You lose! Try again!')
        sys.exit()
    elif arr[0][2] == arr[1][1] == arr[2][0] == 'O':
        print('You lose! Try again!')
        sys.exit()

    s = 0
    for i in range(3):
        s += arr[i].count('')

    if s == 0:
        print("We haven't a winner")
        sys.exit()


def lets_play():
    while True:

        choose_turn(field)

        for i in range(3):
            print(field[i])
        print('\n')

        end_game(field)

        variants_of_turn(field)

        for i in range(3):
            print(field[i])
        print('\n')

        end_game(field)


if __name__ == "__main__":
    from random import randint
    import sys

    field = [['', '', ''],
             ['', '', ''],
             ['', '', '']]

    map_of_field = [['1 1', '1 2', '1 3'],
                    ['2 1', '2 2', '2 3'],
                    ['3 1', '3 2', '3 3']]

    for i in range(3):
        print(map_of_field[i])

    lets_play()
