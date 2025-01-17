import itertools


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # HORIZONTAL LOGIC
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is winner horizontally (--)!")
            return True

    # DIAGONAL LOGIC
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        # print(col, row)
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is winner diagonallay! (/)")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is winner diagonallay (\\)!")
        return True

    # VERTICAL LOGIC
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is winner vertically (|)!")
            return True
    return False


def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        if game_map[row][col] != 0:
            print("This position is occupied! Choose another!")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][col] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: Make sure you input row/column as 0, 1 or 2", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    # GAME MAP
    game_size = int(input("What size game of TicTacToe would you like? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False
        while not played:
            column_choice = int(
                input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(
                input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(
                game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input(
                "The game is over, would you like to play again? (Y/N) ")
            if again.lower() == "y":
                print("Restarting...")
            elif again.lower() == "n":
                print("Byeeeeeeeeee!")
                play = False
            else:
                print("Not a valid answer, so...see ya' later!")
                play = False
