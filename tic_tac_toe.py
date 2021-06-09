demoBoard = {'7': '7' , '8': '8' , '9': '9' ,
            '4': '4' , '5': '5' , '6': '6' ,
            '1': '1' , '2': '2' , '3': '3' }

gameBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print("\U0001F929 \U0001F929 \U0001F929")

def tictactoe():
    moves = 9

    player1_name = input("Player 1, what's your name? ")
    player2_name = input("Player 2, what's your name? ")

    while moves > 1:
        print(printBoard(demoBoard))
        print(printBoard(gameBoard))
        player1_move = input(f"""{player1_name},
        What's your move?
        Enter a corresponding # from the demo board:
         """)
        i = player1_move
        if gameBoard[i] != ' ':
            player1_move = input(f"""{player1_name},
            That position has already been taken!
            Please choose another #:
            """)
            i = player1_move
            gameBoard[i] = 'X'
        else:
            gameBoard[i] = 'X'
            print(printBoard(gameBoard))

            moves -= 1
            print(f"moves left: {moves}")


        print(printBoard(demoBoard))
        print(printBoard(gameBoard))
        player2_move = input(f"""{player2_name},
        What's your move?
        Enter a corresponding # from the demo board:
        """)
        i = player2_move
        if gameBoard[i] != ' ':
            player2_move = input(f"""{player2_name},
            That position has already been taken!
            Please choose another #:
            """)
            i = player2_move
            gameBoard[i] = 'O'
        else:
            gameBoard[i] = 'O'
            print(printBoard(gameBoard))

            moves -= 1
            print(f"moves left: {moves}")

        # i = player2_move
        # gameBoard[i] = 'O'
        # print(printBoard(gameBoard))
        #
        # moves -= 1
        # print(f"moves left: {moves}")


tictactoe()
