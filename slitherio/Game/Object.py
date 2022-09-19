#IMPORTING
import pygame

#SUPER CLASS OBJECT

class Object:
    def __init__(self, x, y, w, h, filepath):
        self.rect = pygame.Rect(x ,y , w, h)
        image = pygame.image.load(filepath)
        self.texturePath = filepath
        self.texture = pygame.transform.scale(image,(w,h))


    #Drawing orbs and player in sub classes   
    def draw(self, window, Camera):
        window.blit(self.texture, Camera.translate(self.rect.x, self.rect.y))













