from collections import defaultdict
from time import time

import pandas as pd

from Assignment_3.algorithms.heuristics import heuristic
from Assignment_3.algorithms.minmax import MiniMax
from Assignment_3.algorithms.monte_carlo import MCTS
from Assignment_3.connect4.game import Game
from Assignment_3.connect4.player import Player, change_player

def run_experiment(first_player, second_player):
    game = Game(mode='AI vs AI')
    game._algorithm = first_player
    game._second_algo = second_player
    first_player_time = 0
    second_player_time = 0
    moves = 0

    turn = Player.AI
    while not game.check_end():
        moves += 1

        if turn == Player.AI:
            start = time()
            game.ai_move()
            first_player_time += (time() - start)
        else:
            start = time()
            game.player_move(None)
            second_player_time += (time() - start)

        turn = change_player(turn)

    winner = change_player(turn)
    print(winner)
    return {
        'first_player_time': first_player_time,
        'second_player_time': second_player_time,
        'moves': moves,
        'winner': winner - 1,
    }


experiments = []

minmax_args = [
    ({'alpha_beta': False, 'max_depth': 2},  {'alpha_beta': False, 'max_depth': 3}),
    ({'alpha_beta': True, 'max_depth': 2},  {'alpha_beta': True, 'max_depth': 2}),
    ({'alpha_beta': False, 'max_depth': 2},  {'alpha_beta': True, 'max_depth': 2}),

    ({'alpha_beta': False, 'max_depth': 3}, {'alpha_beta': False, 'max_depth': 3}),
    ({'alpha_beta': True, 'max_depth': 3}, {'alpha_beta': True, 'max_depth': 3}),
    ({'alpha_beta': False, 'max_depth': 3}, {'alpha_beta': True, 'max_depth': 3}),

    ({'alpha_beta': False, 'max_depth': 4}, {'alpha_beta': False, 'max_depth': 4}),
    ({'alpha_beta': True, 'max_depth': 4}, {'alpha_beta': True, 'max_depth': 4}),
    ({'alpha_beta': False, 'max_depth': 4}, {'alpha_beta': True, 'max_depth': 4}),
    ({'alpha_beta': False, 'max_depth': 4}, {'alpha_beta': False, 'max_depth': 2}),
    ({'alpha_beta': True, 'max_depth': 4}, {'alpha_beta': True, 'max_depth': 2}),
    ({'alpha_beta': False, 'max_depth': 4}, {'alpha_beta': True, 'max_depth': 2}),
]
minmax_experiments = [
    (MiniMax(Player.AI, Player.HUMAN, heuristic, **args1), MiniMax(Player.HUMAN, Player.AI, heuristic, **args2))
     for args1, args2 in minmax_args
]
experiments.extend(minmax_experiments)

# experiments.append((MCTS(1000, 2), MiniMax(Player.HUMAN, Player.AI, heuristic)))
# experiments.append((MCTS(1000, 2), MCTS(1000, 2)))
# experiments.append((MCTS(5000, 2), MCTS(5000, 2)))
# experiments.append((MCTS(1000, 1), MCTS(1000, 1)))
# experiments.append((MCTS(5000, 1), MCTS(5000, 1)))

results = []
for first, second in experiments:
    result_aggregations = defaultdict(float)

    for i in range(4):
        result = run_experiment(first, second)
        for k, v in result.items():
            result_aggregations[k] += v
    for k, v in result_aggregations.items():
        result_aggregations[k] = v / 4

    result_aggregations = {**{'first_alpha_beta': first._alpha_beta,
    'second_alpha_beta': second._alpha_beta,
    'max_depth': first._max_depth}, ** result_aggregations}
    results.append(result_aggregations)


df = pd.DataFrame(results).round(2)
df.to_csv('result.csv')
df.to_latex('result.tex')
