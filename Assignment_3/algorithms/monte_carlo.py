import random

import numpy as np

from Assignment_3.connect4.board import Board
from Assignment_3.connect4.player import Player, change_player


class MCTS:
    def __init__(self, max_iter, factor):
        self._max_iter = max_iter
        self._factor = factor
        self._board = None

    def __call__(self, board):
        self._board = board
        root = Node()
        for _ in range(self._max_iter):
            self._tree_traversal(root)
        # TODO AVG
        best_move = np.argmax([child.num_simulations for child in root.children])
        return best_move

    def _tree_traversal(self, current_node):

        # If is leaf
        if len(current_node.children) == 0:

            # If there are no simulations in this node
            if current_node.num_simulations == 0:
                self._rollout(current_node)
            else:
                current_node.children = self._node_expansion(current_node)
                current_node = random.choice(current_node.children)

                move = self._board.drop_coin(current_node.action, current_node.turn)
                if self._board.check_board_state(*move):
                    current_node.value = 1 if current_node.turn == Player.AI else 0
                else:
                    self._rollout(current_node)
                self._board.unset_field(*move)

            self._backpropagate(current_node)
        else:
            children = current_node.children
            child_with_highest_ucb1 = max(children, key=lambda n: ucb1(n, self._factor))

            move = self._board.drop_coin(child_with_highest_ucb1.action, child_with_highest_ucb1.turn)
            self._tree_traversal(child_with_highest_ucb1)
            self._board.unset_field(*move)

    def _node_expansion(self, node):
        valid_moves = self._board.get_available_moves()
        return [Node(action, node, change_player(node.turn)) for action in valid_moves]

    def _rollout(self, node):
        node.num_simulations += 1

        moves = []
        turn = change_player(node.turn)
        while True:
            valid_moves = self._board.get_available_moves()
            if len(valid_moves) == 0:
                node.value = 0
                break

            move = random.choice(valid_moves)
            moves.append(self._board.drop_coin(move, turn))

            if self._board.check_board_state(*moves[-1]):
                node.value = 1 if turn == Player.AI else -1
                break

            turn = Player.HUMAN if turn == Player.AI else Player.AI


        for move in reversed(moves):
            self._board.unset_field(*move)

    def _backpropagate(self, node):
        while node is not None:
            node.value = sum(child.value for child in node.children) if node.children else node.value
            node.num_simulations += 1
            node = node.parent


class Node:
    def __init__(self, action=None, parent=None, turn=None):
        self.parent = parent
        self.children = []
        self.action = action
        self.num_simulations = 0
        self.value = 0
        self.turn = turn

    @property
    def average_value(self):
        if self.num_simulations == 0:
            return 0

        return self.value / self.num_simulations

    def __str__(self):
        return f'{self.value} / {self.num_simulations}. {round(self.average_value, 2)}'


def ucb1(node, c):
    if node.num_simulations == 0:
        return np.inf

    return node.value / node.num_simulations \
           + c * np.sqrt(np.log(node.parent.num_simulations) / node.num_simulations)




# board = Board()
# board._board = np.array([
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 2, 0, 0, 0, 0],
#     [0, 1, 1, 2, 0, 0, 0],
#     [0, 1, 1, 2, 2, 0, 0],
# ])
#
# mcts = MCTS(1000, 2)
# col = mcts(board)
# print(col)
