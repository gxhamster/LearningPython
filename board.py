theBoard = {
    'top-L': '0', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
    'low-L': ' ', 'low-M': 'X', 'low-R': ' ',
}



def showBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'        
def move():
    global turn
    for i in range(9):
        showBoard(theBoard)
        move = input('Enter move: ')
        theBoard[move] = turn
        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'




move()