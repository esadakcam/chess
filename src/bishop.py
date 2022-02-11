from piece import Piece


class Bishop(Piece):
    def __init__(self, img, x, y, color, name, square):
        super().__init__(img, x, y, color, name)
        self.square = square

    def update(self, board, x, y, previous_turn_piece):
        pass

    def available_moves(self, board, previous_turn_piece):
        moves = []
        for i in range(8):
            if self.board_x + i > 8 or self.board_y + i > 8:
                break   # out of bounds
            if board.get_piece_by_index(self.board_x + i, self.board_y + i) is not None:
                if board.get_piece_by_index(self.board_x + i, self.board_y + i).color != self.color:
                    moves.append((self.board_x + i, self.board_y + i))
                break
            moves.append((self.board_x + i, self.board_y + i))
