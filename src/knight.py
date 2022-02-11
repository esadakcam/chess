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

    def update(self, board, x, y, previous_turn_piece):
        if not self.__valid_move(x, y, board, previous_turn_piece):
            return False
        if board.get_piece_by_index(x, y) is not None:
            board.pieces.remove(board.get_piece_by_index(
                x, y))
        self.board_x = x
        self.board_y = y
        self.x = self.board_x * 64
        self.y = self.board_y * 64
        return True

    def __valid_move(self, x, y, board, previous_turn_piece):
        moves = self.available_moves(board, previous_turn_piece)
        for (x_pos, y_pos) in moves:
            if x_pos == x and y_pos == y:
                return True
        return False
