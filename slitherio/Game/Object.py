#IMPORTING
import pygame

#SUPER CLASS OBJECT - parent class containing all functions for renderable objects
class Object:
    #constructor function
    def __init__(self, x, y, w, h, filepath):
        #private variable
        self.rect = pygame.Rect(x ,y , w, h)
        image = pygame.image.load(filepath)
        self.texturePath = filepath
        self.texture = pygame.transform.scale(image,(w,h))


    #Drawing orbs and player in sub classes   
    def draw(self, window, Camera):
        window.blit(self.texture, Camera.translate(self.rect.x, self.rect.y))