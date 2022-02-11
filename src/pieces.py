from piece import Piece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
import os


class Pieces:
    def __init__(self):
        self.pieces = []
        self.__fill_piece_list()

    def __fill_piece_list(self):
        for i in range(8):
            self.pieces.append(
                Pawn(os.path.join(os.getcwd(), "assets/pieces/w_pawn.png"), i * 64, 384, "white", "pawn"))
            self.pieces.append(
                Pawn(os.path.join(os.getcwd(), "assets/pieces/b_pawn.png"), i * 64, 64, "black", "pawn"))
        for i in range(2):
            self.pieces.append(Rook(os.path.join(
                os.getcwd(), "assets/pieces/w_rook.png"), i * 448, 448, "white", "rook"))
            self.pieces.append(Rook(os.path.join(
                os.getcwd(), "assets/pieces/b_rook.png"), i * 448, 0, "black", "rook"))
            self.pieces.append(Knight(os.path.join(os.getcwd(
            ), "assets/pieces/w_knight.png"), (i * 320) + 64, 448, "white", "knight"))
            self.pieces.append(Knight(os.path.join(os.getcwd(
            ), "assets/pieces/b_knight.png"), (i * 320) + 64, 0, "black", "knight"))
            self.pieces.append(Bishop(os.path.join(os.getcwd(
            ), "assets/pieces/w_bishop.png"), (i * 192) + 128, 448, "white", "bishop", i))
            self.pieces.append(Bishop(os.path.join(os.getcwd(
            ), "assets/pieces/b_bishop.png"), (i * 192) + 128, 0, "black", "bishop", i))
        self.pieces.append(Queen(os.path.join(
            os.getcwd(), "assets/pieces/w_queen.png"), 192, 448, "white", "queen"))
        self.pieces.append(Queen(os.path.join(
            os.getcwd(), "assets/pieces/b_queen.png"), 192, 0, "black", "queen"))
        self.pieces.append(King(os.path.join(
            os.getcwd(), "assets/pieces/w_king.png"), 256, 448, "white", "king"))
        self.pieces.append(King(os.path.join(
            os.getcwd(), "assets/pieces/b_king.png"), 256, 0, "black", "king"))

    def get_piece_by_index(self, x, y):
        for piece in self.pieces:
            if piece.board_x == x and piece.board_y == y:
                return piece
        return None

    def draw(self, screen):
        for piece in self.pieces:
            piece.draw(screen)
