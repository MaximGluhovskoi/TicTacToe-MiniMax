#Simple TicTacToe solver using a minimax algorithm needs only this file to run
#print_board, is_valid_move, place_player, take_turn
#Global Variables
import random
board = [["-","-","-"],["-","-","-",],["-","-","-"]]
player = "O"


#Functions
def print_board():
    print ("\n      0     1     2")
    for i in range(3):
        print()
        print (i, board[i][0],board[i][1],board[i][2], sep= "     ")
    print("\n")

#returns true if a row,col on the board is open
def is_valid_move(row, col):
    if(row>=0 and row<3 and col>=0 and col<3):
        return "-" == board[row][col]
#places player on row,col on the board
def place_player(player, row, col):
    board[row][col] =  player
#Asks the user to enter a row and col until the user enters a valid location
#Adds user location to the board, and prints the board
def take_turn(player):
    if player == "X":
        print("Player X's turn:\n")
        repeat = True
        while (repeat):
            print("input row number: ", end="")
            row = input()
            print("input column number: ", end="")
            col = input()
            if (("" == str(row)) or ("" == str(col)) or not row.isnumeric() or not col.isnumeric()):
                repeat = True
            else:
                row = int(row)
                col = int(col)
                repeat = not is_valid_move(row, col)
            if (repeat == True):
                print("\n|||input a valid empty space within the board|||\n")
        place_player(player, row, col)
    else:
        print("Player O's turn:\n")
        rand=10#random.randint(2,6)
        runFunc = minimax(player, rand, -1000, 1000)
        place_player(player, runFunc[1], runFunc[2])
    



#check win functions here:
def check_col_win(player):
    for i in range(3):
        cur = 0
        for j in range(3):
            if(board[j][i] == player):
                cur+=1
            if(cur==3):
                return True
    return False       

def check_row_win(player):
    for i in range(3):
        cur = 0
        for j in range(3):
            if(board[i][j] == player):
                cur+=1
            if(cur==3):
                return True
    return False 
    
def check_diag_win(player):
    cur = 0
    curOther = 0
    for i in range(3):
        if(board[i][i] == player):
            cur+=1
        if(board[i][2-i] == player):
            curOther +=1
        if(cur==3 or curOther==3):
            return True

def check_win(player):
    if(check_diag_win(player)):
        return True
    elif(check_row_win(player)):
        return True
    elif(check_col_win(player)):
        return True
    else:
        return False

def check_tie():
    for i in range(3):
        for j in range(3):
            if(board[i][j] == "-"):
                return False
    return True

def minimax(player, depth, alpha, beta):
    optimalRow = -1
    optimalCol = -1
    if check_win("X"):
        return (-10, None, None, None, None)
    elif check_win("O"):
        return (10,None, None, None, None)
    elif check_tie() or depth==0:
        return (0, None, None, None, None)
    
    #implement recursive case
    if player == "O":
        best = -10000
        for i in range(3):
            for j in range(3):
                if is_valid_move(i,j):
                    place_player(player, i, j)
                    #print("player O placed at:", i,j)
                    cur = minimax("X", depth-1, alpha, beta)[0]
                    if best < max(best, cur):
                        best = max(best,cur)
                        optimalRow = i
                        optimalCol = j
                        alpha = max(alpha, cur)
                    place_player("-", i, j)
                    if alpha >= beta:
                        break
                    #print(best, i, j, optimalRow, optimalCol)
                    
                    
        return (best, optimalRow, optimalCol, alpha, beta)
    if player == "X":
        worst = 10000
        for i in range(3):
            for j in range(3):
                if is_valid_move(i,j):
                    place_player(player, i, j)
                    #print("player X placed at:",i,j)
                    cur = minimax("O", depth-1, alpha, beta)[0]
                    if worst > min(worst, cur):
                        worst = min(worst,cur)
                        optimalRow = i
                        optimalCol = j
                        beta = min(beta, cur)
                    place_player("-", i, j)
                    
                    if beta <= alpha:
                        break
                    #print(worst, i, j, optimalRow, optimalCol)

        return (worst, optimalRow, optimalCol, alpha, beta)
        
        
        
        
#Start of program
print("\t\tWelcome to Tic Tac Toe!\n\n\n")
print_board()

#Finish implementing the game here:
while(not check_win(player) and not check_tie()):
    if(player == 'X'):
        player = 'O'
    else:
        player = 'X'
    take_turn(player)
    print_board()

if(check_tie() and not check_win(player)):
    print("The game ended in a tie")
else:
    print("Player " + player + " won the game!")