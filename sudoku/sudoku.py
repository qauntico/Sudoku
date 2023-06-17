#suduko is a game that's ask you fill certain spaces in a board already partailly filled and the number you are putting when traced in the whole row or column it should not appear again, so each number you are putting when traced in that row or column completely it should not appear there
#so this is a 4x4 board it's simple right?
#This is our pre define 4x4
def gameboard(board):
    print('___________________')
    print(board[12]+'  |  '+board[13]+'  |  '+board[14]+'  |  '+board[15])
    print('___________________')
    print(board[8]+'  |  '+board[9]+'  |  '+board[10]+'  |  '+board[11])
    print('___________________')
    print(board[4]+'  |  '+board[5]+'  |  '+board[6]+'  |  '+board[7])
    print('___________________')
    print(board[0]+'  |  '+board[1]+'  |  '+board[2]+'  |  '+board[3])
    print('___________________')
#this function will help us position the number we have choosen at their various index position which we have also choosen then append the values to a certain list to keep track of our rows and columns
def positioning(board,digit,col1,col2,col3,col4,rol1,rol2,rol3,rol4):
    while True:
        user = input('What number do you want to place at the position you took: ')
        if user in ['1','2','3','4']:
            break
    board[digit] = str(user)
#this is what will help the program know which row and column you placed your number
    if digit in [0,1,2,3]:
        rol1.append(user)
    if digit in [4,5,6,7,8]:
        rol2.append(user)
    if digit in [8,9,10,11]:
        rol3.append(user)
    if digit in [12,13,14,15]:
        rol4.append(user)
    if digit in [0, 4, 8, 12]:
        col1.append(user)
    if digit in [1,5,9,15]:
        col2.append(user)
    if digit in [2,6,10,14]:
        col3.append(user)
    if digit in [3,7,11,15]:
        col4.append(user)
#this function simply validates the user index position and returns it value
def user_input(board):
    while True:
        user_input = input("Enter a index position between 0 and {}: ".format(len(board)-1))
        if user_input.isdigit():
            index = int(user_input)
            if 0 <= index < len(board) and board[index] == ' ':
                return int(user_input)
        print("That position is already filled up or out of range. ")
#this is what then keeps track whether the number you inputed didn't repeat in it subquent row or column
def wincheck(col1,col2,col3,col4,rol1,rol2,rol3,rol4):
    return (len(set(col1))==4 and len(set(col2))==4 and len(set(col3))==4 and len(set(col4))== 4 and len(set(rol1))==4  and len(set(rol2))==4  and len(set(rol3))==4  and len(set(rol4))==4)
def playon():
    user = input('do you want to play sudoku again yes or no: ')
    return user == 'yes'
print('WELCOME TO SUDOKU')
#this is the game logic
while True:
    count = 0
    board = [' ', ' ', '4', '3', '4', ' ', ' ', ' ', '3', '4', '1', ' ', '1', '2', ' ', ' ']
#this is our predefine rows and columns for the program to also keep track
    rol1 = ['4', '3']
    rol2 = ['4']
    rol3 = ['3', '4', '1']
    rol4 = ['1', '2']
    col1 = ['1', '3', '4']
    col2 = ['2', '4']
    col3 = ['1', '4']
    col4 = ['3']

    user = input('Are you ready to start, yes or no: ')
    if user == 'yes':
        gamestart = True
    else:
        gamestart = False
    while gamestart:
        gameboard(board)
        user = user_input(board)
        positioning(board, user, col1, col2, col3, col4, rol1, rol2, rol3, rol4)
        count += 1
        if count == 8:
            if wincheck(col1, col2, col3, col4, rol1, rol2, rol3, rol4):
                print('Your value were correct you won sir')
                break
            else:
                print('You loosed scom back try again')
                break
    if not playon():
        break


