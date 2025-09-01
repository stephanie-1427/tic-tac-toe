from random import choice

player = None
players = ['X', 'O']
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def pick_player():
    global player
    player = choice(players)

__all__ = ["player", "players", "board", "pick_player"]