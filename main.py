def new_board():
    board = [[None for i in range(3)] for j in range(3)]
    # board[0][1] = 'X'
    # board [1][1] = 'O'
    return board

def render(board):
    index = 0
    for i in range(3):
        for j in range(3):
            index += 1
            if board[i][j] is None:
                print(str(index) + " ", end = "")    
            else:
                print(str(board[i][j]) + " ", end = "") 
             
        print()

def get_move():
    print("Which number would you like to place on?")
    num = int(input())
    if num <= 0 or num > 9:
        print("Invalid input!")
        get_move()
    else:
        move_dict = {1:[0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6:[1, 2], 7:[2, 0], 8: [2, 1], 9: [2, 2]}
        return move_dict[num]

def is_valid_move(board, move_coordinates):
    if board[move_coordinates[0]][move_coordinates[1]] is None:
        return True
    else:
        return False

def make_move(board, move_coordinates, player):
   temp = new_board()
   for i in range(3):
       for j in range(3):
           temp[i][j] = board[i][j]
    
   if is_valid_move(board, move_coordinates):
       temp[move_coordinates[0]][move_coordinates[1]] = player
   else:
       raise Exception("Square is already occupied!")
   
   return temp

def is_board_full(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != None:
                count += 1
    return count == 9

def get_winner(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != None and board[1][1] != None and board[2][2] != None:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != None and board[1][1] != None and board[2][0] != None:
        return board[0][2]
    elif board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != None and board[0][1] != None and board[0][2] != None:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != None and board[1][1] != None and board[1][2] != None:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != None and board[2][1] != None and board[2][2] != None:
        return board[2][0]
# move1 = get_move()
# print(move1)
# board = make_move(board, move1, 'X')
# #board = make_move(board, move1, 'Y')
# render(board)

player = 'X'
move_num = 0
board = new_board()
render(board) 
while(get_winner(board) == None):
    move = get_move()
    board = make_move(board, move, player)
    render(board)
    move_num += 1
    if move_num % 2 != 0: player = 'O'
    else: player = 'X'

if player == 'X': player = 'O'
elif player == 'O': player = 'X'
print("Winner is {0}!".format(player))