import pygame

from work_image import load_image

TILE_IMAGES = {
    'box': load_image('box.png'),
    'grass': load_image('grass.png'),
    'player': load_image('mar.png')
}
TILE_WIDTH = TILE_HEIGHT = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tile_type, *groups):
        super().__init__(*groups)
        self.image = TILE_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(pos_x * TILE_WIDTH, pos_y * TILE_HEIGHT)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tile_type, *groups):
        super().__init__(*groups)
        self.image = TILE_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(pos_x * TILE_WIDTH + 15, pos_y * TILE_HEIGHT + 5)

    def update(self, new_pos_x, new_pos_y):
        self.rect = self.image.get_rect().move(new_pos_x * TILE_WIDTH + 5, new_pos_y * TILE_HEIGHT + 5)
