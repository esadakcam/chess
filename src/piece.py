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

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def _set_pos(self, x, y):
        self.board_x = x
        self.board_y = y
        self.x = self.board_x * 64
        self.y = self.board_y * 64

    def _valid_move(self, x, y, board, previous_turn_piece):
        moves = self.available_moves(board, previous_turn_piece)
        for (x_pos, y_pos) in moves:
            if x_pos == x and y_pos == y:
                return True
        return False

    @abstractmethod
    def available_moves(self, board, previous_turn_piece):
        pass

    def update(self, board, x, y, previous_turn_piece):
        if not self._valid_move(x, y, board, previous_turn_piece):
            return False
        if board.get_piece_by_index(x, y) is not None:
            board.pieces.remove(board.get_piece_by_index(x, y))
        self._set_pos(x, y)
        return True
