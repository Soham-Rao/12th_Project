#importing
import pygame
import os

#class font - class for rendering text on screen
class Font:
    #contructor function
    def __init__(self):
        #private variables
        self.color = (255,255,0) #Yellow
        self.size = 70
        self.font = pygame.font.Font(os.path.join("textures","Minecraft.ttf"), self.size)

    #function to create font to be rendered and blit it 
    def renderFont(self, window, score):
        text = self.font.render("Score: " + str(score), True, self.color)
        window.blit(text,(0,0))