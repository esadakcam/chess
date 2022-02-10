import pygame as pg
from pygame.locals import *
import os
from piece import Piece
from pieces import Pieces


class App:

    def __init__(self):
        self.board = Pieces()
        self.running = True
        self.screen = pg.display.set_mode((512, 512))
        self.clock = pg.time.Clock()
        self.board_background = pg.image.load(
            os.path.join(os.getcwd(), "assets/boards/board.png"))
        self.black_piece = None
        self.white_piece = None
        self.turn = 0

    def main(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    piece = self.board.get_piece_by_index(
                        pos[0]//64, pos[1]//64)
                    if piece and ((piece.color == "white" and self.turn == 1) or (piece.color == "black" and self.turn == 0)):
                        piece = None
                    if piece is not None:
                        if self.turn == 0:
                            self.white_piece = piece
                        else:
                            self.black_piece = piece
                    print(piece.available_moves(self.board))
                if event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    end_turn = False
                    if self.turn == 0 and self.white_piece is not None:
                        end_turn = self.white_piece.update(
                            self.board, pos[0]//64, pos[1]//64)
                    elif self.turn == 1 and self.black_piece is not None:
                        end_turn = self.black_piece.update(
                            self.board, pos[0]//64, pos[1]//64)
                    if end_turn:
                        if self.turn:
                            self.black_piece = None
                        else:
                            self.white_piece = None
                        self.turn = (self.turn + 1) % 2

            self.screen.blit(self.board_background,
                             self.board_background.get_rect())
            self.board.draw(self.screen)
            if(self.turn == 0 and self.white_piece is not None):
                for move in self.white_piece.available_moves(self.board):
                    pg.draw.circle(
                        self.screen, (0, 0, 0), ((move[0] * 64) + 32, (move[1] * 64) + 32), 15)
            pg.display.update()
