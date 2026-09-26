print()
print("------TIC - TAC - TOE------")
print()
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
counter = 0
winning_positions = [
    [0, 4, 8],
    [2, 4, 6],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
loop_run = True

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

print_board(board)

def check_winner(winning_position):
    global loop_run
    for i in winning_position:
        x_counter = 0
        o_counter = 0
        for j in i:
            if board[j] == "X":
                x_counter += 1
            elif board[j] == "O":
                o_counter += 1
        if x_counter == 3:
            print("Player X is the winner.")
            loop_run = False
            break
        elif o_counter == 3:
            print("Player O is the winner.")
            loop_run = False
            break
    if loop_run == True and counter == 9:
        print("Match Draw!")

while loop_run and counter < 9:
    if counter % 2 == 0:
        while True:
            try:
                choice = int(input("Player X, enter your position: "))
                if choice < 0 or choice > 8:
                    print("Player X, please enter a valid position.")
                    continue
                if board[choice] == "X" or board[choice] == "O":
                    print("Player X, enter an empty position.")
                    continue
            except ValueError:
                print("Player X, please enter a valid position.")
                continue
            except IndexError:
                print("Player X, please enter a valid position.")
                continue
            break
        board[choice] = "X"
        counter += 1
        print_board(board)
        check_winner(winning_positions)
    else:
        while True:
            try:
                choice = int(input("Player O, enter your position: "))
                if choice < 0 or choice > 8:
                    print("Player O, please enter a valid position.")
                    continue
                if board[choice] == "X" or board[choice] == "O":
                    print("Player O, enter an empty position.")
                    continue
            except ValueError:
                print("Player O, please enter a valid position.")
                continue
            except IndexError:
                print("Player O, please enter a valid position.")
                continue
            break
        board[choice] = "O"
        counter += 1
        print_board(board)
        check_winner(winning_positions)
