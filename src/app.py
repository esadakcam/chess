import pygame as pg
from pygame.locals import *
import os
from piece import Piece
from pieces import Pieces


class App:
    def __init__(self):
        self.pieces = Pieces()
        self.running = True
        self.screen = pg.display.set_mode((512, 512))
        self.clock = pg.time.Clock()
        self.board = pg.image.load(
            os.path.join(os.getcwd(), "assets/boards/board.png"))

    def main(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            self.screen.blit(self.board, self.board.get_rect())
            self.pieces.draw(self.screen)
            pg.display.update()
