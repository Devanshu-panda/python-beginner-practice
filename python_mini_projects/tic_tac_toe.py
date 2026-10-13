import groq
from groq import Groq
client = Groq()

import random as rnd

def menu_function():
    print("====================================")
    print("      TIC - TAC - TOE      ")
    print("====================================")
    print("Select Game Mode")
    print()
    print("[1] Player vs Player\n[2] Player vs Computer (Easy)\n[3] Player vs Computer (Intelligent)\n[4] Exit")
    print()
    while True:
        try:
            print("=====================================")
            choice = int(input("Enter your choice(1-4): "))
            print("====================================")
            if choice > 4 or choice < 1:
                print("Enter a valid choice.")
                continue
            break
        except ValueError:
            print("====================================")
            print("Please enter a valid choice.")
    return choice

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

def reset_parameters():
    global board
    global counter
    global loop_run
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    counter = 0
    loop_run = True

def print_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(board, winning_position):
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
            print(player_1 + " is the winner.")
            loop_run = False
            break
        elif o_counter == 3:
            print(player_2 + " is the winner.")
            loop_run = False
            break
    if all(x in ["X", "O"] for x in board) and loop_run == True:
        loop_run = False
        print("Match Draw!")

def groq_move(board, feedback = ""):
    empty_position = []
    for i in board:
        if i not in ["X", "O"]:
            empty_position.append(i)

    board_text = str(board)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": """
                                            You are playing Tic-Tac-Toe as O against X.

                                            The board has positions 0 to 8.
                                            X and O represent occupied positions.
                                            Numbers represent empty positions.

                                            Analyze all 8 winning combinations before choosing a move.
                                            Follow these priorities in order:
                                            1. Win immediately if possible.
                                            2. Block X if it can win on its next move.
                                            3. Create a fork to gain two possible winning moves.
                                            4. Block X from creating a fork.
                                            5. Take the center (position 4) if available.
                                            6. Take the opposite corner if appropriate.
                                            7. Take an available corner.
                                            8. Take an available side.
                                            9. If you can't find a winning posiotion then play any move for draw.

                                            Choose only from the supplied empty positions.
                                            Return exactly one position number from 0 to 8.
                                            Do not provide any explanation.
                                            """
            },
            {
                "role": "user",
                "content": (
                            f"Current board: {board_text}\n"
                            f"Empty positions: {empty_position}\n"
                            f"{feedback}"
                )
            }
        ],
        temperature=0
    )
    move_text = response.choices[0].message.content.strip()
    return move_text
3
# Player vs Player Model
def player_vs_player(board):
    global counter
    while loop_run and counter < 9:
        if counter % 2 == 0:
            while True:
                try:
                    move = int(input( player_1 + " enter your position: "))
                    if move < 0 or move > 8:
                        print(player_1 + ", please enter a valid position.")
                        continue
                    if board[move] == "X" or board[move] == "O":
                        print(player_1 + ", enter an empty position.")
                        continue
                except ValueError:
                    print(player_1 + ", please enter a valid position.")
                    continue
                break
            board[move] = "X"
            counter += 1
            print_board(board)
            check_winner(board, winning_positions)
        else:
            while True:
                try:
                    move = int(input(player_2 + " enter your position: "))
                    if move < 0 or move > 8:
                        print(player_2 + " please enter a valid position.")
                        continue
                    if board[move] == "X" or board[move] == "O":
                        print(player_2 + " enter an empty position.")
                        continue
                except ValueError:
                    print(player_2 + " please enter a valid position.")
                    continue
                break
            board[move] = "O"
            counter += 1
            print_board(board)
            check_winner(board, winning_positions)

# Player vs Computer (Easy) Model
def player_vs_computer_easy(board):
    global counter
    while loop_run and counter < 9:
        if counter % 2 == 0:
            while True:
                try:
                    move = int(input(player_1 + " enter your position: "))
                    if move < 0 or move > 8:
                        print(player_1 + ", please enter a valid position.")
                        continue
                    if board[move] == "X" or board[move] == "O":
                        print(player_1 + ", enter an empty position.")
                        continue
                except ValueError:
                    print(player_1 + ", please enter a valid position.")
                    continue
                break
            board[move] = "X"
            counter += 1
            print_board(board)
            check_winner(board, winning_positions)
        else:
            empty_position = []
            for i in board:
              if i not in ["X", "O"]:
                  empty_position.append(i)
            move = rnd.choice(empty_position)
            print(f"Computer chose {move}.")
            board[move] = "O"
            counter += 1
            print_board(board)
            check_winner(board, winning_positions)

#Player vs Computer (Hard):
def player_vs_computer_hard(board):
    global counter
    while loop_run and counter < 9:
        if counter % 2 == 0:
            while True:
                try:
                    move = int(input(player_1 + " enter your position: "))
                    if move < 0 or move > 8:
                        print(player_1 + ", please enter a valid position.")
                        continue
                    if board[move] == "X" or board[move] == "O":
                        print(player_1 + ", enter an empty position.")
                        continue
                except ValueError:
                    print(player_1 + ", please enter a valid position.")
                    continue
                break
            board[move] = "X"
            counter += 1
            print_board(board)
            check_winner(board, winning_positions)
        else:
            empty_position = [x for x in board if x not in ["X", "O"]]
            feedback = ""
            for attempt in range(3):
                move_text = groq_move(board, feedback)

                try:
                    move = int(move_text)
                except ValueError:
                    feedback = (
                        f"Your response was invalid. "
                        f"Return only a position from {empty_position}."
                    )
                    continue

                if move in empty_position:
                    break

                feedback = (
                    f"Position {move} is occupied. "
                    f"Choose only from {empty_position}."
                )

            else:
                print("Groq failed after 3 attempts. Using a random legal move.")
                move = rnd.choice(empty_position)

            print(f"Computer chose {move}.")
            board[move] = "O"
            counter += 1
            print_board(board)
            check_winner(board, winning_positions)

#Calling functions
while True:
    choice = menu_function()

    if choice == 4:
        print("Thanks for playing Tic-Tac-Toe!")
        break

    elif choice == 1:
        player_1 = input("Player 1, enter your name: ").title()
        player_2 = input("Player 2, enter your name: ").title()
        print_board(board)
        player_vs_player(board)

    elif choice == 2:
        player_1 = input("Player, enter your name: ").title()
        player_2 = "Computer"
        print_board(board)
        player_vs_computer_easy(board)

    elif choice == 3:
        player_1 = input("Player, enter your name: ").title()
        player_2 = "Computer"
        print_board(board)
        try:
            player_vs_computer_hard(board)

        except groq.APIError:
            print("\nThis mode is not available right now.")
            print("Please choose another mode.\n")

    reset_parameters()
