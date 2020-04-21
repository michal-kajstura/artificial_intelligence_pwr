import math
import sys

import pygame

from Assignment_3.connect4.board import Board, Player

BACKGROUND_COLOR = (18, 20, 26)
BOARD_COLOR = (13, 71, 161)
CIRCLES_COLORS = {
    Player.PLAYER1: (255, 87, 51),
    Player.PLAYER2: (255, 214, 0),
    0: BACKGROUND_COLOR
}

_COLOR = (0, 0, 255)
COLUMN_COUNT = 7
ROW_COUNT = 6
SQUARESIZE = 100
pygame.font.init()
FONT = pygame.font.SysFont('Comic Sans MS', 70)
TEXT_COLOR = (255, 255, 255)
RADIUS = SQUARESIZE // 2 - 5

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

screen = pygame.display.set_mode((width, height))

board = Board(ROW_COUNT, COLUMN_COUNT)
game_over = False

def draw_board(board, screen):
    rows, cols = board.shape

    pygame.draw.rect(screen, BOARD_COLOR, (0, SQUARESIZE, width, height))
    for row in range(rows):
        for col in range(cols):
            pygame.draw.circle(
                screen,
                CIRCLES_COLORS[board[row, col]],
                (col * SQUARESIZE + SQUARESIZE // 2, (row + 1) * SQUARESIZE + SQUARESIZE // 2),
                RADIUS
            )
    pygame.display.update()

def drop_circle(board, col, player):
    rows, cols = board.shape
    for row in reversed(range(rows)):
        if board[row, col] == 0:
            board.set_field(row, col, player)
            return True

    return False


pygame.init()
turn = Player.PLAYER1

pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, width, height))
draw_board(board, screen)

while not game_over:
    pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, width, height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = event.pos
            col = math.floor(pos_x / SQUARESIZE)

            drop_circle(board, col, turn)

            if board.check_board_state(turn):
                text_surface = FONT.render(f'{turn} won!', False, TEXT_COLOR)
                screen.blit(text_surface, (SQUARESIZE // 2, 10))

            draw_board(board, screen)

            turn = Player.PLAYER1 if turn == Player.PLAYER2 else Player.PLAYER2


