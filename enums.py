

def Colour(colour):
    colours = {
        "white":True,
        "black":False}
    return colours[colour]

def Piece(piece):
    roles = ["pawn","rook","knight","bishop","queen","king"]
    pieces = {}
    i = 1
    for role in roles:
        pieces[role] = i
        i += 1
    return pieces[piece]

def Tile(tile):
    cols = ("a","b","c","d","e","f","g","h")
    rows = (1,2,3,4,5,6,7,8)
    tiles = {}
    i = 1
    for col in cols:
        for row in rows:
            tiles[f"{col}{row}"] = i
            i += 1
    return tiles[tile]

def Row(tile):
    cols = ("a","b","c","d","e","f","g","h")
    rows = (1,2,3,4,5,6,7,8)
    tiles = {}
    for row in rows:
        for col in cols:
            if tile == Tile(f"{col}{row}"):
                return row
    raise Exception
