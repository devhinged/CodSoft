import random

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
player = "X"
player2 = "O"
winner = None
GameStarts = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board, currentPlayer):
    ins = input(f"Player {currentPlayer}, enter a number b/w (1 to 9): ")

    if not ins:
        print("Input cannot be blank. Enter a valid number.")
        return False

    ins = int(ins)
    if ins >= 1 and ins <= 9 and board[ins-1] == " ":
        board[ins-1] = currentPlayer
    elif ins < 1 or ins > 9:
        print("Enter a valid number b/w (1 to 9)")
        return False
    elif not ins:
        print("The string is blank. Enter a valid number")
        return False
    else:
        print("That space is already taken")
        return False
    return True

def aiMove(board, currentPlayer, opponent):
    for i in range(9):
        if board[i] == " ":
            board[i] = opponent
            if checkWin(board, opponent):
                board[i] = currentPlayer
                return
            board[i] = " "
    for i in range(9):
        if board[i] == " ":
            board[i] = currentPlayer
            if checkWin(board, currentPlayer):
                return
            board[i] = " "
    available_moves = [i for i in range(9) if board[i] == " "]
    if available_moves:
        move = random.choice(available_moves)
        board[move] = currentPlayer

def checkWin(board, currentPlayer):
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == currentPlayer:
            return True

    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] == currentPlayer:
            return True

    if board[0] == board[4] == board[8] == currentPlayer or board[2] == board[4] == board[6] == currentPlayer:
        return True

    return False

def winOrTie(board, currentPlayer):
    global winner
    winner = None
    if checkWin(board, currentPlayer):
        winner = f"Player {currentPlayer} ({'X' if currentPlayer == 'X' else 'O'})"
        return True
    if " " not in board:
        winner = "Tie"
        return True
    return False

while GameStarts:
    printBoard(board)

    while not playerInput(board, player):
        pass

    if winOrTie(board, player):
        printBoard(board)
        print(f"{winner} wins!")
        GameStarts = False
    else:
        aiMove(board, player2, player)
        if winOrTie(board, player2):
            printBoard(board)
            print(f"{winner} wins!")
            GameStarts = False
