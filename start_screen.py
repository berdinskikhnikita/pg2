import pygame

from game import terminate
from work_image import load_image

BACKGROUND_FILENAME = 'fon.jpg'
SIZE = WIDTH, HEIGHT = 600, 500


def start_screen(screen, size_screen):
    fon = pygame.transform.scale(load_image(BACKGROUND_FILENAME), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.transform.scale(screen, size_screen)
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
            pygame.display.flip()


if __name__ == "__main__":
    screen = None
    start_screen(screen)
