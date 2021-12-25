import pygame

from game import make_world, load_level, terminate, move_mario
from start_screen import start_screen

SIZE = WIDTH, HEIGHT = 500, 500
FILENAME_LEVEL = 'level_1.map'
pygame.init()
screen = pygame.display.set_mode(SIZE)
start_screen(screen, SIZE)
level = load_level(FILENAME_LEVEL)
level, level_size_x, level_size_y = load_level(FILENAME_LEVEL)
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player, pos_player_x, pos_player_y = make_world(level, level_size_x, level_size_y, all_sprites, player_group,
                                                tiles_group)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pos_player_x, pos_player_y = move_mario(level, level_size_x, level_size_y,
                                                        'up', pos_player_x, pos_player_y)
            if event.key == pygame.K_DOWN:
                pos_player_x, pos_player_y = move_mario(level, level_size_x,
                                                        level_size_y, 'down', pos_player_x, pos_player_y)
            if event.key == pygame.K_LEFT:
                pos_player_x, pos_player_y = move_mario(level, level_size_x,
                                                        level_size_y, 'left', pos_player_x, pos_player_y)
            if event.key == pygame.K_RIGHT:
                pos_player_x, pos_player_y = move_mario(level, level_size_x,
                                                        level_size_y, 'right', pos_player_x, pos_player_y)
    player.update(pos_player_x, pos_player_y)

    all_sprites.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()

pygame.quit()
