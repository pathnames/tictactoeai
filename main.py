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

def make_move(board, move_coordinates, player):
   temp = new_board()
   for i in range(3):
       for j in range(3):
           temp[i][j] = board[i][j]
    
   if temp[move_coordinates[0]][move_coordinates[1]] is None:
       temp[move_coordinates[0]][move_coordinates[1]] = player
   else:
       raise Exception("Square is already occupied!")
   
   return temp

board = new_board()
render(board) 
move1 = get_move()
print(move1)
board = make_move(board, move1, 'X')
board = make_move(board, move1, 'Y')
render(board)