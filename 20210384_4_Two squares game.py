# This code plays Two squares game in which each player has to choose two squares next to each other or above each other to make a rectangle
# The game continues until one of the two players' turn comes and he does not find two squares next to each other or above each other to make a rectangle
# By : Mariam Mohamed Mohamed : 20210384


board = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']


def display_board():
    print("--------------------")
    print("|", board[0] + "  |", board[1] + "  |",  board[2] + "  |", board[3] + "  |")
    print("---------------------")
    print("|", board[4] + "  |", board[5] + "  |", board[6] + "  |", board[7] + "  |")
    print("---------------------")
    print("|", board[8] + "  |", board[9] + " |", board[10] + " |", board[11] + " |")
    print("---------------------")
    print("|", board[12] + " |", board[13] + " |",board[14] + " |", board[15] + " |")
    print("---------------------")


display_board()


def play():
    global num1
    global num2
    global  Count
    count = 0 # number of turns  taken by the  two players
    over = game_over()
    print(over)
    while not over:
        print("Player 1,")
        num1 = input("please enter 1st number : ")
        num2 = input("please enter 2nd number : ")
        valid = isvalid()
        while not valid: # input is not in board or two numbers are not next to each other or abrove each other
                         # two numbers are on the edge of the board and do not  form rectangle
                         # one of the two numbers are already taken before
            print("please enter valid number!")
            num1 = input("please enter 1st number : ")
            num2 = input("please enter 2nd number : ")
            valid= isvalid()
        update()
        count += 1
        over = game_over()
        if over == True:
            print("Player 1 win!")
            break

        print("Player 2,")
        num1 = input("please enter 1st number : ")
        num2 = input("please enter 2nd number : ")
        valid = isvalid()
        while not valid: # input is not in board or two numbers are not next to each other or abrove each other
                         # two numbers are on the edge of the board and do not form rectangle
                         # one of the two numbers are already taken before
            print("please enter valid number!")
            num1 = input("please enter 1st number : ")
            num2 = input("please enter 2nd number : ")
            valid = isvalid()
        update()
        count += 1
        over = game_over()
        if count == 8: # maximum number of turns that the two players take
            print("Tie!")
            break
        if over == True:
            print("Player 2 win!")
            break


def isvalid():
    global num1
    global num2
    num1 = int(num1)
    num2 = int(num2)
    if (str(num1) not in board or str(num2) not in board): # input is not in board
        return False
    else:
        if (num1 == num2+4) or (num1 == num2+1) or(num1 == num2-1) or (num1 == num2-4): # if two numbers are next to each other or abrove each other
            # if the two numbers are on the edge of the board and do not form rectangle
            if(num1 == 4 and num2 == 5) or (num1 == 5 and num2 == 4) or (num1 == 8 and num2 == 9) or (num1 == 9 and num2  ==8) or (num1 == 12 and num2 == 13) or (num1 == 13 and num2 == 12):
                return False
            else:
                return True
        else:
            return False


def update():
    global num1
    global num2
    board[num1-1] = "X"
    board[num2-1] = "X"
    display_board()


def game_over():
    if (board[0] == "1" and board[1] == "2") or (board[0] == "1" and board[4] == "5") or (board[1] == "2" and board[2] == "3") or \
            (board[1] == "2" and board[5] == "6") or (board[2] == "3" and board[3] == "4") or (board[2] == "3" and board[6] == "7") or (board[3] == "4" and board[7] == "8") \
            or (board[4] == "5" and board[5] == "6") or (board[4] == "5" and board[8] == "9") or (board[5] == "6" and board[6] == "7") or (board[5] == "6" and board[9] == "10") \
            or (board[6] == "7" and board[7] == "8") or (board[6] == "7" and board[10] == "11") or (board[7] == "8" and board[11] == "12") or (board[8] == "9" and board[9] == "10") \
            or (board[8] == "9" and board[12] == "13") or (board[9] == "10" and board[10] == "11") or (board[9] == "10" and board[13] == "14") or \
            (board[10] == "11" and board[11] == "12") or (board[10] == "11" and board[14] == "15") or (board[11] == "12" and board[15] == "16") or \
            (board[12] == "13" and board[13] == "14") or (board[13] == "14" and board[14] == "15") or (board[14] == "15" and board[15] == "16"):
        return False
    else:
        return True

play()