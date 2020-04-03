def win(current_game):
    # HORIZONTAL LOGIC
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Player {row[0]} is winner horizontally (--)!")

    # DIAGNOL LOGIC
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        print(col, row)
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print("Player {diags[0]} is winner diagonallay! (/)")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print("Player {diags[0]} is winner diagonallay (\\)!")

    # VERTICAL LOGIC
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])

        if check.count(check[col]) == len(check) and check[col] != 0:
            print("Player {check[0]} is winner vertically (|)!")


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][col] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map

    except IndexError as e:
        print("Error: Make sure you input row/column as 0, 1 or 2", e)

    except Exception as e:
        print("Something went very wrong!", e)


play = True
players = [1, 2]
while play:
    # GAME MAP
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game = game_board(game, just_display=True)
    while not game_won:
        current_player = 1
        column_choice = int(
            input("What column do you want to play? (0, 1, 2): "))
        row_choice = int(input("What row do you want to play? (0, 1, 2): "))
        game = game_board(game, current_player, row_choice, column_choice)
