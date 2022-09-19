import pygame
import os


class Font:
    def __init__(self):
        self.color = (255,255,0) #Yellow
        self.size = 70
        self.font = pygame.font.Font(os.path.join("textures","Minecraft.ttf"), self.size)

    def renderFont(self, window, score):
        text = self.font.render("Score: " + str(score), True, self.color)
        window.blit(text,(0,0))

