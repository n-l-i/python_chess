from board import init_board,board_to_str
from enums import Colour

class Game():
    def __init__(self,player_white=None,player_black=None):
        self.board = init_board()
        self.turn = Colour.white
        print(board_to_str(self.board))
    
    def run(self):
        pass
