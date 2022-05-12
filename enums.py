from enum import Enum,Flag,auto

class Colour(Flag):
    white = True
    black = False

Piece = Enum("Piece",["pawn","rook","knight","bishop","queen","king"])
Tile = Enum("Tile",[f"{col}{row}" for col in "abcdefgh "for row in "12345678"])
