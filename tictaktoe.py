def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, col in enumerate(row):
            row_str += col
            if j <= len(col):
                row_str += "|"
        print(row_str)
        if i < len(board):
            print("------")


def get_move(turn, board, turn_move):
    print("now its ", turn, "turn")
    while True:
        try:
            row = int(input("Row: "))
            col = int(input("col"))
        except:
            print("cound not convet to int")
        if(turn_move<9):
          if row < 1 or row > len(board):
              print("cannot enter")
          elif col < 1 or col > len(board[row-1]):
              print("cannot enter")
          elif board[row-1][col-1] != " ":
              print("an elemt aldredy exist")
          else:
              break
        else:
            break  
    board[row-1][col-1] = turn


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
turn_move = 0
while turn_move < 9:
    print("the turn move is", turn_move)
    print_board(board)
    get_move("X", board,turn_move)
    turn_move += 1
    print_board(board)
    get_move("0", board,turn_move)
    turn_move += 1
   
    print_board(board)
    


print("the game is tie")
