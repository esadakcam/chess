from bishop import Bishop
from rook import Rook


class Queen(Bishop, Rook):
    def __init__(self, img, x, y, color, name):
        Bishop.__init__(self, img, x, y, color, name)
        Rook.__init__(self, img, x, y, color, name)

    def available_moves(self, board, previous_turn_piece):
        bishop_moves = Bishop.available_moves(self, board, previous_turn_piece)
        rook_moves = Rook.available_moves(self, board, previous_turn_piece)
        return bishop_moves + rook_moves
