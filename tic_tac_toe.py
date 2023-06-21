from typing import List, Tuple
from itertools import cycle
from colorama import Fore, Style, init


def display_gameboard(game_board: List[List[str]]):
    print("     c1   c2   c3")  # column number
    for row_count, row in enumerate(game_board):  # row_count variable will give row number
        colored_row = ""
        for item in row:
            if item == 'E':
                colored_row += "     "
            elif item == 'X':
                colored_row += Fore.MAGENTA + "  X  " + Style.RESET_ALL
            elif item == 'O':
                colored_row += Fore.LIGHTCYAN_EX + "  O  " + Style.RESET_ALL
        print(f"r{row_count + 1}", colored_row)


def evaluate_result(game_board: List[List[str]]) -> Tuple[bool, str, str]:
    # horizontal win strategy
    for row in game_board:
        # # Approach 1
        # column_1 = row[0]
        # column_2 = row[1]
        # column_3 = row[2]
        # if column_1 == column_2 == column_3 and column_1 != 'E':
        #     return True, column_1

        # Approach 2
        if row.count(row[0]) == len(row) and row[0] != 'E':
            return True, row[0], "horizontally (-)"

    # vertical win strategy
    for col in range(len(game_board[0])):
        check = []
        for row in game_board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 'E':
            return True, check[0], "vertically (|)"

    # diagonal win strategy
    # For \ diagonal
    diags = []
    for ix in range(len(game_board)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 'E':
        return True, diags[0], "diagonally (\\)"

    # For / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game_board)))):
        diags.append(game[idx][reverse_idx])
    if diags.count(diags[0]) == len(diags) and diags[0] != 'E':
        return True, diags[0], "diagonally (/)"

    # No more space left to play (Entire Game Board is full)
    if not any('E' in row for row in game_board):
        return False, 'E', "No more space left to play (Entire Game Board is full)"
    return False, None, None


def move_played_by_player(game_map: List[List[str]], player: str = 'E', row: int = 0, column: int = 0) -> bool:
    if player != 'E' and game_map[row][column] == 'E':
        game_map[row][column] = player

    display_gameboard(game_board=game_map)
    is_won, by_player, game_msg = evaluate_result(game_board=game_map)
    if is_won:
        print(Fore.GREEN, "\n################################################"
                          "###################################################")
        print(f"Congratulations to player_{by_player} for winning this Game {game_msg}")
        print("###################################################################################################")
        return True
    if is_won is False and by_player == 'E':
        print(Fore.CYAN, "\n##############################################"
                         "#####################################################")
        print(game_msg)
        print("###################################################################################################")
        return True
    return False


# display_gameboard(game_board=game)
# move_played_by_player(game_map=game, player='X')
if __name__ == "__main__":
    init()
    play = True
    players = ['X', 'O']
    player_iterator = cycle(players)
    rows = ['r1', 'r2', 'r3']
    columns = ['c1', 'c2', 'c3']
    while play:
        print(Fore.LIGHTBLUE_EX, "Welcome to TIC TAC TOE!!!")
        game = [['E', 'E', 'E'],  # E -> Position is Empty
                ['E', 'E', 'E'],  # X -> Position chose by player X
                ['E', 'E', 'E']]  # O -> Position chose by player O

        print(Style.RESET_ALL)
        display_gameboard(game_board=game)
        is_game_finished = False
        while not is_game_finished:
            # current_player = 'X'
            current_player = next(player_iterator)
            column_choice = input(f"Player {current_player}, Enter the column you wanna use (c1, c2, c3): ")
            row_choice = input(f"Player {current_player}, Enter the row you wanna use (r1, r2, r3): ")
            column_chose = columns.index(column_choice)
            row_chose = rows.index(row_choice)
            is_game_finished = move_played_by_player(game_map=game, player=current_player,
                                                     row=row_chose, column=column_chose)
        print(Fore.RED, "")
        next_game = input("Want to play another game? (Yes/No): ")
        if next_game.lower() == 'no':
            play = False
