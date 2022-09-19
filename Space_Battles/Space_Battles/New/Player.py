import pygame
from Spaceships import Spaceships


class Player(Spaceships):
    def __init__(self, x, y, w ,h, filepath, rotate):
        super().__init__(x, y, w ,h, filepath, rotate)
        self.velocity = 5
        self.max_bul = 10
        self.bul_vel = 7
        #self.score = 0
        
    def movements(self, key_pressed, border, WinDims):
        if key_pressed[pygame.K_a] and self.rect.x - self.velocity > 0: # left
            self.rect.x -= self.velocity
        if key_pressed[pygame.K_d] and self.rect.x + self.velocity + self.rect.width < border.x: # right
            self.rect.x += self.velocity
        if key_pressed[pygame.K_w] and self.rect.y - self.velocity > 0: # up
            self.rect.y -= self.velocity
        if key_pressed[pygame.K_s] and self.rect.y + self.velocity + self.rect.height < WinDims[1]-25:  # down
            self.rect.y += self.velocity

    def bullets(self, List, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(List) <= self.max_bul:
                    bullet = pygame.Rect((self.rect.x + self.rect.width - 5), (self.rect.y + self.rect.height//2 -2), (20), (4))
                    List.append(bullet)

    def move_bullet(self, List):           
        for bullet in List:
                bullet.x += self.bul_vel
