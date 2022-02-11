from piece import Piece


class Pawn(Piece):
    def __init__(self, img, x, y, color, name):
        super().__init__(img, x, y, color, name)
        self.__enpassant_position = None

    def __available_moves_for_white(self, moves, board, previous_turn_piece):
        if self.board_y == 6:
            if board.get_piece_by_index(self.board_x, self.board_y - 2) is None:
                moves.append((self.board_x, self.board_y - 2))
        if board.get_piece_by_index(self.board_x, self.board_y - 1) is None:
            moves.append((self.board_x, self.board_y - 1))
        if board.get_piece_by_index(self.board_x + 1, self.board_y - 1) is not None and board.get_piece_by_index(self.board_x + 1, self.board_y - 1).color == "black":
            moves.append((self.board_x + 1, self.board_y - 1))
        if board.get_piece_by_index(self.board_x - 1, self.board_y - 1) is not None and board.get_piece_by_index(self.board_x - 1, self.board_y - 1).color == "black":
            moves.append((self.board_x - 1, self.board_y - 1))
        self.__enpassant_for_white(moves, previous_turn_piece)

    def __available_moves_for_black(self, moves, board, previous_turn_piece):
        if self.board_y == 1:
            if board.get_piece_by_index(self.board_x, self.board_y + 2) is None:
                moves.append((self.board_x, self.board_y + 2))
        if board.get_piece_by_index(self.board_x, self.board_y + 1) is None:
            moves.append((self.board_x, self.board_y + 1))
        if board.get_piece_by_index(self.board_x + 1, self.board_y + 1) is not None and board.get_piece_by_index(self.board_x + 1, self.board_y + 1).color == "white":
            moves.append((self.board_x + 1, self.board_y + 1))
        if board.get_piece_by_index(self.board_x - 1, self.board_y + 1) is not None and board.get_piece_by_index(self.board_x - 1, self.board_y + 1).color == "white":
            moves.append((self.board_x - 1, self.board_y + 1))
        self.__enpassant_for_black(moves, previous_turn_piece)

    def __enpassant_for_white(self, moves, previous_turn_piece):
        if not previous_turn_piece or self.board_y != 3 or previous_turn_piece.name != "pawn":
            return
        if self.board_x == previous_turn_piece.board_x + 1:
            moves.append((self.board_x - 1, self.board_y - 1))
            self.__enpassant_position = (self.board_x - 1, self.board_y - 1)
        elif self.board_x == previous_turn_piece.board_x - 1:
            moves.append((self.board_x + 1, self.board_y - 1))
            self.__enpassant_position = (self.board_x + 1, self.board_y - 1)

    def __enpassant_for_black(self, moves, previous_turn_piece):
        if not previous_turn_piece or self.board_y != 4 or previous_turn_piece.name != "pawn":
            return
        if self.board_x == previous_turn_piece.board_x + 1:
            moves.append((self.board_x - 1, self.board_y + 1))
            self.__enpassant_position = (self.board_x - 1, self.board_y + 1)
        elif self.board_x == previous_turn_piece.board_x - 1:
            moves.append((self.board_x + 1, self.board_y + 1))
            self.__enpassant_position = (self.board_x + 1, self.board_y + 1)

    def available_moves(self, board, previous_turn_piece):
        moves = []
        if self.color == "white":
            self.__available_moves_for_white(moves, board, previous_turn_piece)
        else:
            self.__available_moves_for_black(moves, board, previous_turn_piece)
        return moves

    def __valid_move(self, x, y, board, previous_turn_piece):
        moves = self.available_moves(board, previous_turn_piece)
        for (x_pos, y_pos) in moves:
            if x_pos == x and y_pos == y:
                return True
        return False

    def update(self, board, x, y, previous_turn_piece):
        if not self.__valid_move(x, y, board, previous_turn_piece):
            return False
        for piece in board.pieces:
            if piece.board_x == x and piece.board_y == y:
                if piece.color == self.color:
                    return False
                else:
                    board.pieces.remove(piece)
        self.board_x = x
        self.board_y = y
        self.x = self.board_x * 64
        self.y = self.board_y * 64
        if self.__enpassant_position == (x, y):
            self.__enpassant_position = None
            if self.color == "white":
                board.pieces.remove(board.get_piece_by_index(x, y + 1))
            else:
                board.pieces.remove(board.get_piece_by_index(x, y - 1))
        return True
