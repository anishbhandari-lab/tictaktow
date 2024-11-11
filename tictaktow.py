board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentplayer = "X"
winner = None
gamerunning = True

#printing game board
def gameboard(board):
    print(board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("---------------")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("---------------")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8])

# taking player input
def playerinput(board):
    inp = int(input("Enter number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentplayer
    else:
        print("You can only write a number from 1 to 9, or choose an empty spot.")

# checking win or tie
def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False
def checkvertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False
def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False
def checkwinner():
    if checkvertical(board) or checkhorizontal(board) or checkdiagonal(board):
        print(f"The winner is {winner}")
        return True
    return False
def checktie():
    global gamerunning
    if "-" not in board and winner is None:
        print("It's a tie.")
        gamerunning = False
# switch the player
def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"
#win or tie
while gamerunning:
    gameboard(board)
    playerinput(board)
    if checkwinner():
        gamerunning = False
        break
    checktie()
    switchplayer()
gameboard(board)
