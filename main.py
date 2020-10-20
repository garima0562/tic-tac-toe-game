#*************global variable**************

#game board
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

# if game is till going
game_still_going = True

# who won or tie?
winner = None

# whose turn is it
current_player = "x"


def display_board():
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[6] + "|" + board[7] + "|" + board[8])

def play_game():
  #display initial board
  display_board()
  
#while the game is still going
  while game_still_going:
    #handle a single turn of an arbitary player
    handle_turn(current_player)

    #check if the game has ended
    check_if_game_over()

    #flip to the other player
    flip_player()

  if winner == "x" or winner == "o":
    print(winner + "  won...")
  elif winner == None:
    print("tie")

 #handle a single turn of an arbitary player

def handle_turn(player):

  print(player + "'s turn.")
  position = input("choose a position from 1-9: ")

  valid = False
  while not valid:
    while position not in ['1','2','3','4','5','6','7','8','9']:
      position = input("choose a position from 1-9:")
    
    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("you can't go there. go again")

  board[position] = player

  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():
# set global variable just like that
  global winner

  #check rows
  row_winner = check_rows() 
  #check column 
  column_winner = check_column() 
  #check diagonals
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return

def check_rows():
  #set up global variable
  global game_still_going
  #check if any row have same column
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  #if any row does have a match , flag that there is win
  if row_1 or row_2 or  row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]

  return

def check_column():

  global game_still_going
  #check if any row have same column
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  #if any row does have a match , flag that there is win
  if column_1 or column_2 or  column_3:
    game_still_going = False
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():
  global game_still_going
  #check if any row have same column
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = board[2] == board[4] == board[6] != "-"
  #if any row does have a match , flag that there is win
  if diagonals_1 or diagonals_2 :
    game_still_going = False
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[2]
  
  return

def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return

def flip_player():
  # global variabe we need
  global current_player
  # if current player was x the change it into o
  if current_player == "x":
    current_player = "o"
  #if 0 the change in x
  elif current_player == "o":
    current_player = "x"
  return



play_game()
















#board
#display board
#play game
#handle turn
#check Win

#check Tie
#flip player