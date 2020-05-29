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
       
render(new_board()) 