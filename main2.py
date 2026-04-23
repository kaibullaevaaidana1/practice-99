import pygame
import sys
from player import MusicPlayer

WIDTH = 600
HEIGHT = 250

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")

    font_big = pygame.font.SysFont(None, 32)
    font_small = pygame.font.SysFont(None, 22)

    player = MusicPlayer("music")

    clock = pygame.time.Clock()

    controls = "P = Play    S = Stop    N = Next    B = Back    Q = Quit"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.prev_track()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        screen.fill((20, 20, 20))

        info_text = font_big.render(player.get_info(), True, (255, 255, 255))
        screen.blit(info_text, (20, 90))

        hint_text = font_small.render(controls, True, (120, 120, 120))
        screen.blit(hint_text, (20, 180))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()