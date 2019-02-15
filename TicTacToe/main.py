#CREATE A TICTACTOE GAME
#2 PLAYERS SITTING AT ONE COMPUTER
#THE BOARD SHOULD BE PRINTED OUT EVERYTIME PLAYER MAKE A MOVE
#ACCEPT USER INPUT AND PLACE THEIR SYMBOL ACCORDINGLY TO THE POSITION
import random


#FUNCTION TO PRINT OUT THE BOARD
def print_board(myboard):
    print("    |    |     ")
    print(f" {myboard[1]}  | {myboard[2]}  | {myboard[3]} ")
    print("    |    |     ")
    print("---------------")
    print("    |    |     ")
    print(f" {myboard[4]}  | {myboard[5]}  | {myboard[6]} ")
    print("    |    |     ")
    print("---------------")
    print("    |    |     ")
    print(f" {myboard[7]}  | {myboard[8]}  | {myboard[9]} ")
    print("    |    |     ")
  
    

#FUNCTION THAT MAKE PLAYER CHOOSE THEIR SYMBOLS
def player_input():
    player1=''
    player2=''
    while player1 != "X" and player1 !="O":
        player1=input("Player 1! please select your symbol (X or O): ").upper()
        if player1=="X":
            player2="O"
        elif player1=="O":
            player2="X"
        else:
            print("Please choose again, symbol should be X or O")
            continue
    return(player1,player2)

#FUNCTION THAT CHECK IF THERE IS WINNER
def check_win(board, mark):
    return (board[1]==board[2]==board[3]==mark or board[4]==board[5]==board[6]==mark or  board[7]==board[8]==board[9]==mark or  board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[3]==board[6]==board[9]==mark or   board[1]==board[5]==board[9]==mark or  board[7]==board[5]==board[3]==mark)

#FUNCTION THAT CHECK IF THE BOARD IS FULL
def check_full(board):
    for item in board:
        if item==' ':
            return False
    return True

#FUNCTION THAT UPDATE THE BOARD AFTER PLAYER MAKE A MOVE
def update_board(myboard,symbol,pos):
    for x,item in enumerate(myboard):
        if x == pos:
            item=item
            myboard[x]=symbol
    print_board(myboard)    

#FUNCTION THAT CHECK IF THE POSITITION THAT PLAYERS MAKE IS CURRENTLY AVAILABLE    
def avail_check(board, position):
    return board[position]==' '

#FUNCTION THAT SEE WHO WILL GO FIRST
def choose_first():
    return random.randint(1,2)
    
#FUNCTION THAT ASK IF PLAYERS WANT TO PLAY AGAIN 
def replay():
    ans=input("Do you want to play again? Y/N: ")
    return ans.upper()=='Y'


#MAIN FUNCTION FOR THE OPERATION OF THE GAME
def tic_tac():
    myboard=[' ']*10
    myboard[0]='$'

    print("Welcome to TICTACTOE game with Python!!!!!")
    print("------------------------------------------")
    print_board(myboard)

    playermarks=player_input()
    turn=choose_first()
    print(f"Player {turn} will go first")
    
    #LOOP THAT LET PLAYER MAKE THEIR MOVE

    while check_win(myboard,playermarks[0])==False and check_win(myboard,playermarks[1])==False and check_full(myboard)==False:
        while turn ==1:
            move=int(input(f"Player {turn} ! Please make your move!!!!: "))
            if move in range(1,10) and avail_check(myboard,move):
                update_board(myboard,playermarks[0],move)
                turn=2
                break
            else:
                print("Invalid move!!!")
                continue

        while turn ==2:
            move=int(input(f"Player {turn} ! Please make your move!!!!: "))
            if move in range(1,10) and avail_check(myboard,move):
                update_board(myboard,playermarks[1],move)
                turn=1
                break
            else:
                print("Invalid move!!!")
                continue            

        if check_full(myboard)==True:
            print("Its a draw match")
            break
            
    #ANNOUNCE THE WINNER 
    else:
        if turn == 2:
            print("CONGRATULATION PLAYER 1 YOU WON THE GAME")
        elif turn==1:
            print("CONGRATULATION PLAYER 2 YOU WON THE GAME")
        
tic_tac()