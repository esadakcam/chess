from piece import Piece


class Knight(Piece):
    def __init__(self, img, x, y, color, name):
        super().__init__(img, x, y, color, name)

    def available_moves(self, board, previous_turn_piece):
        moves = []
        if board.get_piece_by_index(self.board_x + 1, self.board_y + 2) is None or board.get_piece_by_index(self.board_x + 1, self.board_y + 2).color != self.color:
            moves.append((self.board_x + 1, self.board_y + 2))
        if board.get_piece_by_index(self.board_x + 1, self.board_y - 2) is None or board.get_piece_by_index(self.board_x + 1, self.board_y - 2).color != self.color:
            moves.append((self.board_x + 1, self.board_y - 2))
        if board.get_piece_by_index(self.board_x - 1, self.board_y + 2) is None or board.get_piece_by_index(self.board_x - 1, self.board_y + 2).color != self.color:
            moves.append((self.board_x - 1, self.board_y + 2))
        if board.get_piece_by_index(self.board_x - 1, self.board_y - 2) is None or board.get_piece_by_index(self.board_x - 1, self.board_y - 2).color != self.color:
            moves.append((self.board_x - 1, self.board_y - 2))
        if board.get_piece_by_index(self.board_x + 2, self.board_y + 1) is None or board.get_piece_by_index(self.board_x + 2, self.board_y + 1).color != self.color:
            moves.append((self.board_x + 2, self.board_y + 1))
        if board.get_piece_by_index(self.board_x + 2, self.board_y - 1) is None or board.get_piece_by_index(self.board_x + 2, self.board_y - 1).color != self.color:
            moves.append((self.board_x + 2, self.board_y - 1))
        if board.get_piece_by_index(self.board_x - 2, self.board_y + 1) is None or board.get_piece_by_index(self.board_x - 2, self.board_y + 1).color != self.color:
            moves.append((self.board_x - 2, self.board_y + 1))
        if board.get_piece_by_index(self.board_x - 2, self.board_y - 1) is None or board.get_piece_by_index(self.board_x - 2, self.board_y - 1).color != self.color:
            moves.append((self.board_x - 2, self.board_y - 1))
        return moves
