#importing
import pygame
import os

#parent class spaceships - parent class with common properties of both player and enemy spaceships 
class Spaceships:
    #constructor function
    def __init__(self, x, y, w ,h, filepath, rotate):
        #private variables
        self.rect = pygame.Rect(x, y, w, h)
        self.texture = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(filepath),(w,h)),rotate)
        self.texturePath = filepath
        self.health = 10

    #rendering objects onto screen
    def draw(self, window):
        window.blit(self.texture, (self.rect.x, self.rect.y))