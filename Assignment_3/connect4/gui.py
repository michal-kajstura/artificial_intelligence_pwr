import math
import random
import sys

import pygame
import pygame_menu as pmenu

from Assignment_3.connect4.board import Player
from Assignment_3.connect4.game import Game

BACKGROUND_COLOR = (18, 20, 26)
BOARD_COLOR = (13, 71, 161)
CIRCLES_COLORS = {
    Player.AI: (255, 87, 51),
    Player.HUMAN: (255, 214, 0),
    0: BACKGROUND_COLOR
}

pygame.font.init()
FONT = pygame.font.SysFont('Comic Sans MS', 25)
SQUARESIZE = 100
RADIUS = SQUARESIZE // 2 - 5



class GUI:
    def __init__(self, width, height):
        self.config = {
            'max_depth': 4,
            'mode': 'Human vs AI',
            'algorithm': 'Minmax',
        }
        self.screen = pygame.display.set_mode((width, height))
        self._width = width
        self._height = height
        self.first_move = Player.HUMAN
        self.config = dict()
        self.game = Game()

    def display_menu(self):
        self._draw_board()
        menu = pmenu.Menu(400, 500, 'Connect4', theme=pmenu.themes.THEME_BLUE)
        menu.add_button('Play', self.start)
        menu.add_selector(
            'Mode', [['Human vs AI'], ['AI vs AI']], onchange=self._mode_on_change)
        menu.add_selector(
            'Algorithm', [['Minmax'], ['Alpha-beta pruning']], onchange=self._algorithm_on_change)
        menu.add_selector(
            'Fist move', [['Yellow'], ['Red'], ['Random']], onchange=self._first_move_on_change)
        menu.add_button('Quit', sys.exit)
        menu.mainloop(self.screen)

    def start(self):
        pygame.init()
        game_over = False
        turn = self.first_move
        self.game = Game(**self.config)

        while not game_over:
            pygame.draw.rect(self.screen, BACKGROUND_COLOR, (0, 0, self._width, self._height))

            if turn == Player.HUMAN:
                if not self.config['mode'] == 'AI vs AI':
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()

                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            pos_x, pos_y = event.pos
                            col = math.floor(pos_x / SQUARESIZE)
                            self.game.player_move(col)
                            game_over = self.game.check_end()
                            turn = Player.AI
                else:
                    self.game.player_move(None)
                    game_over = self.game.check_end()
                    turn = Player.AI

            else:
                self.game.ai_move()
                turn = Player.HUMAN
                game_over = self.game.check_end()

            self._draw_board()

        message = FONT.render(f"Player {turn} won. Do you want to play again?", True, (255, 255, 255))
        self.screen.blit(message, (50, 50))

    def _mode_on_change(self, value, *args):
        name, index = value
        self.config['mode'] = name

    def _algorithm_on_change(self, value, *args):
        name, index = value
        self.config['algorithm'] = name

    def _first_move_on_change(self, value, *args):
        name, index = value
        if name == 'Yellow':
            self.first_move = Player.HUMAN
        elif name == 'Red':
            self.first_move = Player.AI
        else:
            self.first_move = random.choice([Player.AI, Player.HUMAN])

    def _draw_board(self):
        rows, cols = self.game._board.shape

        pygame.draw.rect(self.screen, BOARD_COLOR, (0, SQUARESIZE, self._width, self._height))
        for row in range(rows):
            for col in range(cols):
                pygame.draw.circle(
                    self.screen,
                    CIRCLES_COLORS[self.game._board[row, col]],
                    (col * SQUARESIZE + SQUARESIZE // 2, (row + 1) * SQUARESIZE + SQUARESIZE // 2),
                    RADIUS
                )
        pygame.display.update()
