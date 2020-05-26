from enum import IntEnum


class Player(IntEnum):
    AI = 1
    HUMAN = 2
    EMPTY = 0

def change_player(player):
    return Player.HUMAN if player == Player.AI else Player.AI
