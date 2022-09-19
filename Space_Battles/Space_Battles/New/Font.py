from turtle import width
import pygame
pygame.font.init()

class Font:
    def __init__(self):
        self.health_font = pygame.font.SysFont('comicsans',40)
        self.Gameover_font = pygame.font.SysFont('timesnewroman', 100)
        self.color = (255,255,255)
        

    def render(self, health, window, windims, score):
        health_text = self.health_font.render("Health: "+ str(health), 1, self.color)
        window.blit(health_text, (10, 10))

        score_text = self.health_font.render("Score: "+ str(score), 1, self.color)
        window.blit(score_text, (windims[0] - health_text.get_width() - 10, 10))


    def gameover(self, window, windims):      
        Gameover_text = self.Gameover_font.render("Game Over!", 1, self.color)
        window.blit(Gameover_text, (windims[0]//2 - Gameover_text.get_width()//2, windims[1]//2 - Gameover_text.get_height()//2))
