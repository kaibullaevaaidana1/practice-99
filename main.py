import pygame
import sys
from clock import Clock

WIDTH = 500
HEIGHT = 500
FPS = 1  # обновляем 1 раз в секунду

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey's Clock")
    clock_obj = Clock(screen, WIDTH, HEIGHT)
    tick = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 255))

        clock_obj.draw()
        pygame.display.flip()
        tick.tick(FPS)
if __name__ == "__main__":
    main()