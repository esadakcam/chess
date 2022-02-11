from piece import Piece


class Pawn(Piece):
    def __init__(self, img, x, y, color, name):
        super().__init__(img, x, y, color, name)

    def __available_moves_for_white(self, moves, board):
        if self.board_y == 6:
            if board.get_piece_by_index(self.board_x, self.board_y - 2) is None:
                moves.append((self.board_x, self.board_y - 2))
        if board.get_piece_by_index(self.board_x, self.board_y - 1) is None:
            moves.append((self.board_x, self.board_y - 1))
        if board.get_piece_by_index(self.board_x + 1, self.board_y - 1) is not None and board.get_piece_by_index(self.board_x + 1, self.board_y - 1).color == "black":
            moves.append((self.board_x + 1, self.board_y - 1))
        if board.get_piece_by_index(self.board_x - 1, self.board_y - 1) is not None and board.get_piece_by_index(self.board_x - 1, self.board_y - 1).color == "black":
            moves.append((self.board_x - 1, self.board_y - 1))

    def __available_moves_for_black(self, moves, board):
        if self.board_y == 1:
            if board.get_piece_by_index(self.board_x, self.board_y + 2) is None:
                moves.append((self.board_x, self.board_y + 2))
        if board.get_piece_by_index(self.board_x, self.board_y + 1) is None:
            moves.append((self.board_x, self.board_y + 1))
        if board.get_piece_by_index(self.board_x + 1, self.board_y + 1) is not None and board.get_piece_by_index(self.board_x + 1, self.board_y + 1).color == "white":
            moves.append((self.board_x + 1, self.board_y + 1))
        if board.get_piece_by_index(self.board_x - 1, self.board_y + 1) is not None and board.get_piece_by_index(self.board_x - 1, self.board_y + 1).color == "white":
            moves.append((self.board_x - 1, self.board_y + 1))

    def available_moves(self, board):
        moves = []
        if self.color == "white":
            self.__available_moves_for_white(moves, board)
        else:
            self.__available_moves_for_black(moves, board)
        return moves
