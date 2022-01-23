name = input("Please Enter your name - \n")
print("Welcome " +name)

board = [" " for space in range(10)]

def insertLetter(Letter, pos):
    board[pos] = Letter

def Freespace(pos):
    return board[pos] == " "

def isbaordfull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def BoardDesign(board):
    print("\n")
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print("\n")

def validInput():
    dummyvalueinput = True
    
    while dummyvalueinput == True:
        x = input("Would you like to play tic tac toe with me? \nPlease enter y/Y to play or n/N to not to play - \n")
        if x.lower() == 'y':
            returnvalue = 'yes'
            print("You have selected to play \n")
            print("************************ Welcome to the game zone ************************\n")
            break

        elif x.lower() == 'n':
            returnvalue = 'no'
            print("You selected to not to play \n")
            print("************************ Sad to know, You don't like to play with me ************************\n")
            break
            
        else:
            returnvalue = "NA"
            print("You have entered invalid input. \nPlease enter y/Y to play or n/N to not to play - \n")
            continue
        
    return returnvalue


def returnedvalue():
    if validInput() == "no":
        print("************************ Sad to know, You don't like to play with me ************************\n")
        print("How about you change your mind?\n")
        validInput()
    

    return finalchoose

#WINNERCHECK
def Iswinner(boardpos, dummylet):
    return ((boardpos[1]==dummylet and boardpos[2]==dummylet and boardpos[3]==dummylet) or 
            (boardpos[4]==dummylet and boardpos[5]==dummylet and boardpos[6]==dummylet) or 
            (boardpos[7]==dummylet and boardpos[8]==dummylet and boardpos[9]==dummylet) or 
            (boardpos[1]==dummylet and boardpos[4]==dummylet and boardpos[7]==dummylet) or 
            (boardpos[2]==dummylet and boardpos[5]==dummylet and boardpos[8]==dummylet) or 
            (boardpos[3]==dummylet and boardpos[6]==dummylet and boardpos[9]==dummylet) or 
            (boardpos[1]==dummylet and boardpos[5]==dummylet and boardpos[9]==dummylet) or 
            (boardpos[3]==dummylet and boardpos[5]==dummylet and boardpos[7]==dummylet))
#PLAYERMOVE
def playermove():
    run = True
    while run:
        move = input("Enter your postion between 1 to 9 to place X")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if Freespace(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print("Sorry this place is occupied")

            else:
                print("Enter a value between 1 to 9")

        except:
            print("Please Enter a Valid number Between 1 to 9")

#COMPUTERMOVE
def computermove():
    possiblemoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    # This create a list of number between 1 to 9 which are empty ignoring the filled spaces.
    move = 0

    for let in ['O', 'X']: #We are writing for both player and computer to insert X or O

        for i in possiblemoves:
            boardcopy = board[:] # we are creating a dict here
            boardcopy[i] = let
            if Iswinner(boardcopy, let):
                move = i
                return move

    cornerlist = []

    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornerlist.append(i)

    if len(cornerlist) > 0:
        move = selectRandom(cornerlist)
        return move

    if 5 in possiblemoves:
        move = 5
        return move

    edgeslist = []

    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgeslist.append(i)

    if len(edgeslist) > 0:
        move = selectRandom(edgeslist)
        return move


#Random
def selectRandom(lis):
    import random
    ln = len(lis)
    r = random.randrange(0, ln)
    return lis[r]

# Main Logic
def main():    
    print("Welcome to the game!")
    BoardDesign(board)

    while not(isbaordfull(board)):
        if not(Iswinner(board , 'O')):
            playermove()
            BoardDesign(board)
        else:
            print("Sorry you lost the game! computer beat you {}".format(name))
            break

        if not(Iswinner(board , 'X')):
            move = computermove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('Computer placed an o on position' , move , ': ')
                BoardDesign(board)
        else:
            print("you win! {}". format(name))
            break




    if isbaordfull(board):
        print("Tie game")



while True:
    
    if (validInput() == 'yes'):        
        print('--------------------')
        board = [' ' for x in range(10)]
        main()
        
    else:
        break
