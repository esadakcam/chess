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

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
