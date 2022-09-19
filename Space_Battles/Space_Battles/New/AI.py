import pygame
import random
from Spaceships import Spaceships

class AI(Spaceships):
    def __init__(self, x, y, w ,h, filepath, rotate):
        super().__init__(x, y, w ,h, filepath, rotate)
        self.prevtime = 0
        self.time = 0
        self.max_bul = 10
        self.bul_vel = 7

    def movements(self, border, windims):
        dir = ['R','L','U','D']

        self.time = pygame.time.get_ticks()
        
        if self.time - self.prevtime >= 70:
            self.prevtime = self.time

            randx = random.randint(0, 40)
            randy = random.randint(0, 40)
            direction = random.choice(dir)
            if direction == 'L' and self.rect.x - randx > (border.x + border.width + 10): # left
                for i in range(randx):
                    self.rect.x -= 1
            if direction == 'R' and self.rect.x + randx + self.rect.width < windims[0]: # right
                for i in range(randx):
                    self.rect.x += 1
            if direction == 'U' and self.rect.y - randy > 0: # up
                for i in range(randy):
                    self.rect.y -= 1
            if direction == 'D' and self.rect.y + randy + self.rect.height < windims[1]-25:  # down
                for i in range(randy):
                    self.rect.y += 1

    def bullets(self, List):
        self.time = pygame.time.get_ticks()

        if len(List) <= self.max_bul and self.time - self.prevtime >= 80:
            self.prevtime = self.time

            bullet = pygame.Rect((self.rect.x), (self.rect.y + self.rect.height//2 -2), (20), (4))
            List.append(bullet)

    def move_bullet(self, List):           
        for bullet in List:
                bullet.x -= self.bul_vel