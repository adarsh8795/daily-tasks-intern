print('welcome to the tic tac toe game')




def bprint(board):
  for i in board:
    print(f'{i}\n')

def takeinput():
    inp=10
    while inp not in range(0,9):
      inp=int(input('at which index you want to put:'))
    return inp
    


def checker(board):
    if board[0][0] == board[0][1]==board[0][2] :
        if board[0][0]=='O':
             print("player 2 won")
              
        else:
             print("player 1 won")
    elif board[1][0] == board[1][1] == board[1][2]:
        if board[1][0]=='O':
             print("player 2 won")
        else:
            print("player 1 won")
          
    elif board[2][0] == board[2][1]==board[2][2]:
        if board[2][0]=='O':
             print("player 2 won")
          
        else:
            print("player 1 won")
           
    elif board[0][0]== board[1][0]==board[2][0]:
        if board[1][0]=='O':
             print("player 2 won")
        else:
             print("player 1 won")
           
    elif board[0][2]== board[1][2]==board[2][2]:
        if board[0][2]=='O':
             print("player 2 won")
           
        else:
             print("player 1 won")
           
    elif board[0][0] == board[1][1]==board[2][2]:
        if board[0][0]=='O':
           
             print("player 2 won")
        else:
          
            print("player 1 won")
           
    elif board[2][0]== board[1][1]==board[0][2]:
        if board[0][2]=='O':
             print("player 2 won")
           
        else:
            print("player 1 won")
           
    else:
        print("tie")
        return 0

def update(y,steps,board):
    if steps%2==0:
        if y<3:
            board[0][y]='X'
        elif y<6:
            board[1][y%3]='X'
        else:
            board[2][y%3]='X'
        

         
    else:
        if y<3:
            board[0][y]='O'
        elif y<6:
            board[1][y%3]='O'
        else:
            board[2][y%3]='O'


def start():
   res= input('ready to play y or n :')
   if res=='y':
     board=[['1','2','3'],
     ['4','5','6'],
     ['7','8','9']]
     for i in range(0,9):
       bprint(board)
       x = takeinput()
       update(x,i,board)
       if(i>3):
        checker(board) 
   else:
    start()


    
start()

