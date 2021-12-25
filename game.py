import pygame

import sys

from sprites import Tile, Player

FILENAME_LEVEL = 'level_1.map'


def terminate():
    pygame.quit()
    sys.exit()


def load_level(filename):
    fullname = 'data/' + filename
    with open(fullname, 'r') as mapfile:
        data = mapfile.readlines()
    data = [elem.strip() for elem in data]
    size_x = max([len(elem) for elem in data])
    data = [elem.ljust(size_x, '.') for elem in data]
    size_y = len(data)
    return data, size_x, size_y


def make_world(level, level_size_x, level_size_y, all_sprites, player_group, tiles_group):
    player = None
    position_player_x, position_player_y = None, None
    for y in range(level_size_y):
        for x in range(level_size_x):
            if level[y][x] == '#':
                Tile(x, y, 'box', tiles_group, all_sprites)
            elif level[y][x] == '.':
                Tile(x, y, 'grass', tiles_group, all_sprites)
            elif level[y][x] == '@':
                Tile(x, y, 'grass', tiles_group, all_sprites)
                player = Player(x, y, 'player', player_group, all_sprites)
                position_player_x = x
                position_player_y = y
    return player, position_player_x, position_player_y


def move_mario(level, level_size_x, level_size_y, direction, pos_player_x, pos_player_y):
    if direction == 'up':
        if pos_player_y > 0 and level[pos_player_y - 1][pos_player_x] != '#':
            pos_player_y -= 1
        return pos_player_x, pos_player_y
    elif direction == 'down':
        if pos_player_y < level_size_y - 1 and level[pos_player_y + 1][pos_player_x] != '#':
            pos_player_y += 1
        return pos_player_x, pos_player_y
    elif direction == 'right':
        if pos_player_x < level_size_x - 1 and level[pos_player_y][pos_player_x + 1] != '#':
            pos_player_x += 1
        return pos_player_x, pos_player_y
    elif direction == 'left':
        if pos_player_x > 0 and level[pos_player_y][pos_player_x - 1] != '#':
            pos_player_x -= 1
    return pos_player_x, pos_player_y
