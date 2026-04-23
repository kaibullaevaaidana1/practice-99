import pygame
import sys
from ball import Ball

WIDTH = 600
HEIGHT = 400

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball")
    clock = pygame.time.Clock()

    ball = Ball(WIDTH // 2, HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                step = ball.step

                if event.key == pygame.K_UP:
                    ball.move(0, -step, WIDTH, HEIGHT)  

                elif event.key == pygame.K_DOWN:
                    ball.move(0, step, WIDTH, HEIGHT)    

                elif event.key == pygame.K_LEFT:
                    ball.move(-step, 0, WIDTH, HEIGHT)   
                elif event.key == pygame.K_RIGHT:
                    ball.move(step, 0, WIDTH, HEIGHT)    


        screen.fill((255, 255, 255))
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()