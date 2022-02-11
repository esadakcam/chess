from piece import Piece


class Rook(Piece):
    def __init__(self, img, x, y, color, name):
        super().__init__(img, x, y, color, name)

    def available_moves(self, board, previous_turn_piece):
        moves = []
        for i in range(1, 8):
            if self.board_x + i < 8:
                if board.get_piece_by_index(self.board_x + i, self.board_y) is None:
                    moves.append((self.board_x + i, self.board_y))
                elif board.get_piece_by_index(self.board_x + i, self.board_y).color != self.color:
                    moves.append((self.board_x + i, self.board_y))
                    break
                else:
                    break
        for i in range(1, 8):
            if self.board_x - i >= 0:
                if board.get_piece_by_index(self.board_x - i, self.board_y) is None:
                    moves.append((self.board_x - i, self.board_y))
                elif board.get_piece_by_index(self.board_x - i, self.board_y).color != self.color:
                    moves.append((self.board_x - i, self.board_y))
                    break
                else:
                    break
        for i in range(1, 8):
            if self.board_y + i < 8:
                if board.get_piece_by_index(self.board_x, self.board_y + i) is None:
                    moves.append((self.board_x, self.board_y + i))
                elif board.get_piece_by_index(self.board_x, self.board_y + i).color != self.color:
                    moves.append((self.board_x, self.board_y + i))
                    break
                else:
                    break
        for i in range(1, 8):
            if self.board_y - i >= 0:
                if board.get_piece_by_index(self.board_x, self.board_y - i) is None:
                    moves.append((self.board_x, self.board_y - i))
                elif board.get_piece_by_index(self.board_x, self.board_y - i).color != self.color:
                    moves.append((self.board_x, self.board_y - i))
                    break
                else:
                    break
        return moves
