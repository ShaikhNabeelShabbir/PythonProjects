# create a game tic tak toe 👍


list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = [7, 8, 9]


def check_win():

    if list_a[0] == list_a[1] == list_a[2]:
        print(list_a[2] + " WON!!!")
        quit()
    elif list_b[0] == list_b[1] == list_b[2]:
        print(list_b[2] + " WON!!!")
        quit()
    elif list_c[0] == list_c[1] == list_c[2]:
        print(list_c[2] + " WON!!!")
        quit()
    elif list_a[0] == list_b[0] == list_c[0]:
        print(list_c[0] + " WON!!!")
        quit()
    elif list_a[1] == list_b[1] == list_c[1]:
        print(list_c[1] + " WON!!!")
        quit()
    elif list_a[2] == list_b[2] == list_c[2]:
        print(list_c[2] + " WON!!!")
        quit()
    elif list_a[0] == list_b[1] == list_c[2]:
        print(list_c[2] + " WON!!!")
        quit()
    elif list_c[0] == list_b[1] == list_a[2]:
        print(list_a[2] + " WON!!!")
        quit()
    # elif list_a[0] != list_a[1] != list_a[2] and list_b[0] != list_b[1] != list_b[2] and list_c[0] != list_c[1] != list_c[2] and list_a[0] != list_b[0] != list_c[0] and list_a[1] != list_b[1] != list_c[1] and list_a[2] == list_b[2] == list_c[2]:
    #     print("game drawn")
    #     quit()


def X_TURN():

    x_turn = int(input("\n X turn - Enter a number : "))

    if x_turn == 1 and list_a[0] == 1:
        list_a[0] = "X"
        draw_board()
        check_win()
        O_TURN()
    elif x_turn == 2 and list_a[1] == 2:
        list_a[1] = "X"
        draw_board()
        check_win()
        O_TURN()
    elif x_turn == 3 and list_a[2] == 3:
        list_a[2] = "X"
        draw_board()
        check_win()
        O_TURN()
    elif x_turn == 4 and list_b[0] == 4:
        list_b[0] = "X"
        draw_board()
        check_win()
        O_TURN()
    elif x_turn == 5 and list_b[1] == 5:
        list_b[1] = "X"
        draw_board()
        check_win()
        O_TURN()
    elif x_turn == 6 and list_b[2] == 6:
        list_b[2] = "X"
        draw_board()
        check_win()
        O_TURN()
    elif x_turn == 7 and list_c[0] == 7:
        list_c[0] = "X"
        draw_board()
        check_win()
        O_TURN()
    elif x_turn == 8 and list_c[1] == 8:
        list_c[1] = "X"
        draw_board()
        check_win()
        O_TURN()
    elif x_turn == 9 and list_c[2] == 9:
        list_c[2] = "X"
        draw_board()
        check_win()
        O_TURN()
    else:
        print("Invalid choice!!!")
        draw_board()
        X_TURN()


def O_TURN():

    o_turn = int(input("\n O turn - Enter a number : "))

    if o_turn == 1 and list_a[0] == 1:
        list_a[0] = "O"
        draw_board()
        check_win()
        X_TURN()
    elif o_turn == 2 and list_a[1] == 2:
        list_a[1] = "O"
        draw_board()
        check_win()
        X_TURN()
    elif o_turn == 3 and list_a[2] == 3:
        list_a[2] = "O"
        draw_board()
        check_win()
        X_TURN()
    elif o_turn == 4 and list_b[0] == 4:
        list_b[0] = "O"
        draw_board()
        check_win()
        X_TURN()
    elif o_turn == 5 and list_b[1] == 5:
        list_b[1] = "O"
        draw_board()
        check_win()
        X_TURN()
    elif o_turn == 6 and list_b[2] == 6:
        list_b[2] = "O"
        draw_board()
        check_win()
        X_TURN()
    elif o_turn == 7 and list_c[0] == 7:
        list_c[0] = "O"
        draw_board()
        check_win()
        X_TURN()
    elif o_turn == 8 and list_c[1] == 8:
        list_c[1] = "O"
        draw_board()
        check_win()
        X_TURN()
    elif o_turn == 9 and list_c[2] == 9:
        list_c[2] = "O"
        draw_board()
        check_win()
        X_TURN()
    else:
        print("Invalid choice!!!")
        draw_board()
        O_TURN()


def set_turns():

    X_TURN()


def draw_board():

    print(list_a)
    print(list_b)
    print(list_c)


draw_board()
set_turns()
