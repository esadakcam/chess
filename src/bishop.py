from piece import Piece


class Bishop(Piece):
    def __init__(self, img, x, y, color, name):
        super().__init__(img, x, y, color, name)

    def available_moves(self, board, previous_turn_piece):
        moves = []
        for i in range(1, 8):
            if self.board_x + i > 7 or self.board_y + i > 7:
                break   # out of bounds
            if board.get_piece_by_index(self.board_x + i, self.board_y + i) is not None:
                if board.get_piece_by_index(self.board_x + i, self.board_y + i).color != self.color:
                    moves.append((self.board_x + i, self.board_y + i))
                break
            moves.append((self.board_x + i, self.board_y + i))

        for i in range(1, 8):
            if self.board_x + i > 7 or self.board_y - i < 0:
                break   # out of bounds
            if board.get_piece_by_index(self.board_x + i, self.board_y - i) is not None:
                if board.get_piece_by_index(self.board_x + i, self.board_y - i).color != self.color:
                    moves.append((self.board_x + i, self.board_y - i))
                break
            moves.append((self.board_x + i, self.board_y - i))

        for i in range(1, 8):
            if self.board_x - i < 0 or self.board_y - i < 0:
                break   # out of bounds
            if board.get_piece_by_index(self.board_x - i, self.board_y - i) is not None:
                if board.get_piece_by_index(self.board_x - i, self.board_y - i).color != self.color:
                    moves.append((self.board_x - i, self.board_y - i))
                break
            moves.append((self.board_x - i, self.board_y - i))

        for i in range(1, 8):
            if self.board_x - i < 0 or self.board_y + i < 0:
                break   # out of bounds
            if board.get_piece_by_index(self.board_x - i, self.board_y + i) is not None:
                if board.get_piece_by_index(self.board_x - i, self.board_y + i).color != self.color:
                    moves.append((self.board_x - i, self.board_y + i))
                break
            moves.append((self.board_x - i, self.board_y + i))
        return moves
