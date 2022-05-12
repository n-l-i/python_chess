from enums import Colour,Tile,Piece,Row
from copy import deepcopy as copy

def init_board():
    tiles = {}
    for row in range(1,9):
        for col in "abcdefgh":
            tile = Tile(f"{col}{row}")
            if row in (1,2):
                colour = Colour("white")
            elif row in (7,8):
                colour = Colour("black")
            else:
                continue
            if row in (2,7):
                piece = Piece("pawn")
            elif col in ("a","h"):
                piece = Piece("rook")
            elif col in ("b","g"):
                piece = Piece("knight")
            elif col in ("c","f"):
                piece = Piece("bishop")
            elif col == "d":
                piece = Piece("queen")
            elif col == "e":
                piece = Piece("king")
            tiles[tile] = {"colour":colour,"piece":piece}
    return tiles

def board_to_str(board):
    colours = {
        Colour("white"):"w",
        Colour("black"):"b"}
    pieces = {
        Piece("pawn"):"Pa",
        Piece("rook"):"Ro",
        Piece("knight"):"Kn",
        Piece("bishop"):"Bi",
        Piece("queen"):"Qu",
        Piece("king"):"Ki"}
    string = "\n"
    string += "   -╎"
    for _ in range(8):
        string += "---╎"
    string += "-\n"
    for row in (8,7,6,5,4,3,2,1):
        string += f"  {row} ╎"
        for col in "abcdefgh":
            tile = Tile(f"{col}{row}")
            if tile not in board:
                string += "   ╎"
                continue
            colour = board[tile]["colour"]
            piece = board[tile]["piece"]
            string += f"{colours[colour]}{pieces[piece]}╎"
        string += "\n"
        string += "   -╎"
        for _ in range(8):
            string += "---╎"
        string += "-\n"
    
    string += "     "
    for col in "ABCDEFGH":
        string += f" {col}  "
    string += "\n"
    return string

def move_piece(board,start_tile,end_tile):
    board = copy(board)
    if isinstance(start_tile,str) and isinstance(end_tile,str):
        start_tile,end_tile = Tile(start_tile),Tile(end_tile)
    piece = board.pop(start_tile)
    if piece["piece"] == Piece("pawn") and Row(end_tile) in (1,8):
        piece["piece"] = Piece("queen")
    board[end_tile] = piece
    return board
