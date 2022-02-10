import pygame


class Piece:
    def __init__(self, img, x, y, color, name):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        self.board_x = x / 64
        self.board_y = y / 64

    def available_moves(self, board):
        return []
# TODO: make abstract method

    def update(self, board, x, y):
        for piece in board.pieces:
            if piece.board_x == x and piece.board_y == y:
                return False
        self.board_x = x
        self.board_y = y
        self.x = self.board_x * 64
        self.y = self.board_y * 64
        return True

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
