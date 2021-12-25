import pygame
import sys

def load_image(filename):
    fullname = 'data/' + filename
    try:
        image = pygame.image.load(fullname)
    except TypeError:
        print(f'не удалось открыть изображение {filename}')
        sys.exit()
    return image

