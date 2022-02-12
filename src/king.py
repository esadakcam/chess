from piece import Piece


class King(Piece):
    def __init__(self, img, x, y, color, name):
        super().__init__(img, x, y, color, name)

    def __base_moves(self, board):
        moves = []
        if board.get_piece_by_index(self.board_x + 1, self.board_y + 1) is None or (board.get_piece_by_index(self.board_x + 1, self.board_y + 1).color != self.color and board.get_piece_by_index(self.board_x + 1, self.board_y + 1).guarded == False):
            moves.append((self.board_x + 1, self.board_y + 1))
        if board.get_piece_by_index(self.board_x + 1, self.board_y - 1) is None or (board.get_piece_by_index(self.board_x + 1, self.board_y - 1).color != self.color and board.get_piece_by_index(self.board_x + 1, self.board_y - 1).guarded == False):
            moves.append((self.board_x + 1, self.board_y - 1))
        if board.get_piece_by_index(self.board_x - 1, self.board_y + 1) is None or (board.get_piece_by_index(self.board_x - 1, self.board_y + 1).color != self.color and board.get_piece_by_index(self.board_x - 1, self.board_y + 1).guarded == False):
            moves.append((self.board_x - 1, self.board_y + 1))
        if board.get_piece_by_index(self.board_x - 1, self.board_y - 1) is None or (board.get_piece_by_index(self.board_x - 1, self.board_y - 1).color != self.color and board.get_piece_by_index(self.board_x - 1, self.board_y - 1).guarded == False):
            moves.append((self.board_x - 1, self.board_y - 1))
        if board.get_piece_by_index(self.board_x + 1, self.board_y) is None or (board.get_piece_by_index(self.board_x + 1, self.board_y).color != self.color and board.get_piece_by_index(self.board_x + 1, self.board_y).guarded == False):
            moves.append((self.board_x + 1, self.board_y))
        if board.get_piece_by_index(self.board_x - 1, self.board_y) is None or (board.get_piece_by_index(self.board_x - 1, self.board_y).color != self.color and board.get_piece_by_index(self.board_x - 1, self.board_y).guarded == False):
            moves.append((self.board_x - 1, self.board_y))
        if board.get_piece_by_index(self.board_x, self.board_y + 1) is None or (board.get_piece_by_index(self.board_x, self.board_y + 1).color != self.color and board.get_piece_by_index(self.board_x, self.board_y + 1).guarded == False):
            moves.append((self.board_x, self.board_y + 1))
        if board.get_piece_by_index(self.board_x, self.board_y - 1) is None or (board.get_piece_by_index(self.board_x, self.board_y - 1).color != self.color and board.get_piece_by_index(self.board_x, self.board_y - 1).guarded == False):
            moves.append((self.board_x, self.board_y - 1))
        return moves

    def available_moves(self, board, previous_turn_piece):
        moves = self.__base_moves(board)
        i = 0
        while i < len(moves):
            if self.__check_reachable(moves[i], board, previous_turn_piece) == False:
                del moves[i]
            else:
                i += 1
        return moves

    def __check_reachable(self, move, board, previous_turn_piece):
        previous_pos = (self.board_x, self.board_y)
        self.board_x, self.board_y = move
        for piece in board.pieces:
            if piece.color == self.color:
                continue
            if piece.name == self.name:
                if move in piece.__base_moves(board):
                    self.board_x, self.board_y = previous_pos
                    return False
                continue
            if move in piece.available_moves(board, previous_turn_piece):
                self.board_x, self.board_y = previous_pos
                return False

        self.board_x, self.board_y = previous_pos
        return True
