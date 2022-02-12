import pygame
from abc import abstractmethod


class Piece:
    def __init__(self, img, x, y, color, name):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        self.board_x = x / 64
        self.board_y = y / 64
        self.previous_position = (self.board_x, self.board_y)
        self.guarded = True

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def _set_pos(self, x, y):
        self.previous_position = (self.board_x, self.board_y)
        self.board_x = x
        self.board_y = y
        self.x = self.board_x * 64
        self.y = self.board_y * 64

    def valid_move(self, x, y, board, previous_turn_piece):
        check_flag = board.check_for_white if self.color == "white" else board.check_for_black
        moves = self.available_moves(board, previous_turn_piece)
        if not check_flag:
            if (x, y) in moves:
                return True
            return False
        # TODO : BUGLU burdan sonrası
        if (x, y) not in moves:
            return False
        previous_pos = (self.board_x, self.board_y)
        self.board_x, self.board_y = x, y
        king = board.get_king(self.color)
        for piece in board.pieces:
            if piece.color == self.color or piece.name == "king":
                continue
            if (king.board_x, king.board_y) in piece.available_moves(board, previous_turn_piece):
                self.board_x, self.board_y = previous_pos
                return False
        self.board_x, self.board_y = previous_pos
        return True

    @abstractmethod
    def available_moves(self, board, previous_turn_piece):
        pass

    def update(self, board, x, y, previous_turn_piece):
        if not self.valid_move(x, y, board, previous_turn_piece):
            return False
        if board.get_piece_by_index(x, y) is not None:
            board.pieces.remove(board.get_piece_by_index(x, y))
        self._set_pos(x, y)
        return True

    def update_guarded(self, board, previous_turn_piece):
        previous_color = self.color
        self.color = "black" if self.color == "white" else "white"

        for piece in board.pieces:
            if piece.color == self.color:
                continue
            if (self.board_x, self.board_y) in piece.available_moves(board, previous_turn_piece):
                self.color = previous_color
                self.guarded = True
                return
        self.color = previous_color
        self.guarded = False
