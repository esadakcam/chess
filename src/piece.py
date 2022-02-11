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

    @abstractmethod
    def available_moves(self, board):
        pass

    @abstractmethod
    def update(self, board, x, y):
        pass
