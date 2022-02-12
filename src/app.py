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
        self.previous_turn_piece = None
        self.turn = 0
        self.check_for_black = False
        self.check_for_white = False

    def __hover_available_moves(self):
        if(self.turn == 0 and self.white_piece is not None):
            for move in self.white_piece.available_moves(self.board, self.previous_turn_piece):
                pg.draw.circle(
                    self.screen, (210, 105, 30), ((move[0] * 64) + 32, (move[1] * 64) + 32), 10)
        elif(self.turn == 1 and self.black_piece is not None):
            for move in self.black_piece.available_moves(self.board, self.previous_turn_piece):
                pg.draw.circle(
                    self.screen, (210, 105, 30), ((move[0] * 64) + 32, (move[1] * 64) + 32), 10)

    def __mouse_button_up(self):
        pos = pg.mouse.get_pos()
        end_turn = False
        if self.turn == 0 and self.white_piece is not None:
            end_turn = self.white_piece.update(
                self.board, pos[0]//64, pos[1]//64, self.previous_turn_piece)
        elif self.turn == 1 and self.black_piece is not None:
            end_turn = self.black_piece.update(
                self.board, pos[0]//64, pos[1]//64, self.previous_turn_piece)
        if end_turn:
            self.__handle_end_turn()

    def __mouse_button_down(self):
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

    def __handle_end_turn(self):
        for piece in self.board.pieces:
            piece.update_guarded(self.board, self.previous_turn_piece)
        if self.turn:
            self.previous_turn_piece = self.black_piece
            self.black_piece = None
        else:
            self.previous_turn_piece = self.white_piece
            self.white_piece = None
        self.turn = (self.turn + 1) % 2
        self.__control_check_black()
        self.__control_check_white()

    def __control_check_black(self):
        king = self.board.get_king("black")
        for piece in self.board.pieces:
            if piece.name == "king":
                continue
            if(piece.color == "white"):
                for move in piece.available_moves(self.board, self.previous_turn_piece):
                    if(move[0] == king.board_x and move[1] == king.board_y):
                        self.check_for_black = True
                        return
        self.check_for_black = False

    def __control_check_white(self):
        king = self.board.get_king("white")
        for piece in self.board.pieces:
            if piece.name == "king":
                continue
            if(piece.color == "black"):
                for move in piece.available_moves(self.board, self.previous_turn_piece):
                    if(move[0] == king.board_x and move[1] == king.board_y):
                        self.check_for_white = True
                        return
        self.check_for_white = False

    def main(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.__mouse_button_down()
                if event.type == pg.MOUSEBUTTONUP:
                    self.__mouse_button_up()
            self.screen.blit(self.board_background,
                             self.board_background.get_rect())
            self.board.draw(self.screen)
            self.__hover_available_moves()
            pg.display.update()
