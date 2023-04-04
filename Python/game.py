# tic tac toe
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # using a single list to replicate 3x3 board
        self.current_winner = None # keep track of winner 
        
    def print_board(self):
        # getting the row ready
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row) + '|')
            
    @staticmethod
    def print_board_nums():
        # tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row) + '|')
            
# available moves after you make a move
    def available_moves(self):
        # return[]
        moves = []
        for(i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
                
    def empty_squares(self):
        return " " in self.board 
    def num_empty_square(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make the move(assign square to letter)
        # then return true. if invalvid, return false
        
    
        
 def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()
    
    letter = "x" # starting letter
    # iterate while the game still has empty squares
    # (we dont' ave to worry about winner because it'll 
    # return that which breaks the loop)
    while game.empty_square():
        # get the move from the appropriate player
        if letter == "0":
            sqare = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
    # define a function to make a move
