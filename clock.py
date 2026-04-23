import pygame
import datetime

class Clock:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.cx = width // 2    # центр экрана по X
        self.cy = height // 2   # центр экрана по Y

        self.hand_img = pygame.image.load("images/mickey_hand.png").convert_alpha()


        self.hand_img = pygame.transform.scale(self.hand_img, (40, 120))

    def get_angle(self, value, total):
        return (value / total) * 360

    def draw_hand(self, angle_deg):
        rotated = pygame.transform.rotate(self.hand_img, -angle_deg)
        rect = rotated.get_rect(center=(self.cx, self.cy))
        self.screen.blit(rotated, rect)

    def draw(self):
        now = datetime.datetime.now()
        minutes = now.minute
        seconds = now.second

        # Считаем углы для каждой руки
        min_angle = self.get_angle(minutes, 60)   # правая рука = минуты
        sec_angle = self.get_angle(seconds, 60)   # левая рука = секунды

        # Рисуем обе руки
        self.draw_hand(min_angle)
        self.draw_hand(sec_angle)