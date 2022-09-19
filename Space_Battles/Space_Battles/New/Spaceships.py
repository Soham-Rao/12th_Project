import pygame
import os

class Spaceships:
    def __init__(self, x, y, w ,h, filepath, rotate):
        self.rect = pygame.Rect(x, y, w, h)
        self.texture = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(filepath),(w,h)),rotate)
        self.texturePath = filepath
        self.health = 10

    def draw(self, window):
        window.blit(self.texture, (self.rect.x, self.rect.y))

