theboard={'7':' ','8':' ','9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' '
          }
          
def printBoard(board):
	print (f"{board['7']} | {board['8']} | {board[9]} ")
	print ("-+-+-")
	print (f"{board[4]} | {board[5]} | {board[6]} ")
	print ("-+-+-")
	print (f"{board[1]} | {board[2]} | {board[3]} ")

printBoard(4)
	