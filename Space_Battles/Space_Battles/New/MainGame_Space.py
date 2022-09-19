import pygame
import os
import random
import csv
from Player import Player
from AI import AI
from Font import Font
from Space_Highscore import Highscore

FPS = 60

PLAYER_HEIGHT = 75
PLAYER_WIDTH = 100
PLAYER_X = 100 
PLAYER_Y = 330
AI_X = 900
AI_Y = 330

MAX_BULLETS = 5

Player_hit = pygame.USEREVENT + 1
enemy_hit = pygame.USEREVENT + 2

class MainGame_Space:
    def __init__(self):
        self.WinDims = (1000, 700)
        self.window = pygame.display.set_mode(self.WinDims) 
        pygame.display.set_caption("Space Battles")
        self.Winbgm = pygame.transform.scale(pygame.image.load(os.path.join("Assets","space.png")),(self.WinDims))

        self.quit = False
        self.clock = pygame.time.Clock()
        self.border = pygame.Rect((self.WinDims[0]//2)-5, 0, 10, self.WinDims[1])
        self.colors = [(0,59,89),(144,238,144),(255,0,0),(255,255,0),(255,255,255),(0,0,0),(0,0,255)] #CYAN, GREEN, RED, YELLOW, WHITE, BLACK

        self.player_textures = [os.path.join("Assets","Blue_Spaceship.png")]
        self.enemy_textures = [os.path.join("Assets","Red_Spaceship.png")]
        self.player = Player(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, random.choice(self.player_textures), 90)
        self.enemy = AI(AI_X, AI_Y, PLAYER_WIDTH, PLAYER_HEIGHT, random.choice(self.enemy_textures), 270)
        self.spaceships = []
        self.spaceships.append(self.player)
        self.spaceships.append(self.enemy)
        self.player_bullets = []
        self.enemy_bullets = []

        self.player_health = 10
        self.score = 0

        self.fontrenderer = Font()
        self.Highscore = Highscore()

    def play(self):
        while self.quit == False:
            self.update()
            self.render()

    def update(self):
        self.clock.tick(FPS)

        #window events 
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                #SCORES IN CSV
                '''
                f = open("space_highscore.csv", "w", newline = "")
                csw = csv.writer(f)
                L = ['Username', 'Score']
                csw.writerow(L)
                f.close()
                '''
                self.Highscore.create_csv(self.score)
                self.quit = True

            if event.type == enemy_hit:
                self.enemy.health -= 1
                

            #bullet keys
            self.player.bullets(self.player_bullets, events)
            
            self.enemy.bullets(self.enemy_bullets)
            
        
        #Movements
        keypressed = pygame.key.get_pressed()
        self.player.movements(keypressed,self.border, self.WinDims)
        self.player.move_bullet(self.player_bullets)
        
        
        if self.player_health > 0:
            self.enemy.movements(self.border, self.WinDims)
            self.enemy.move_bullet(self.enemy_bullets)
        elif self.player_health <= 0:
            pygame.time.delay(2000)
            '''
            f = open("space_highscore.csv", "w", newline = "")
            csw = csv.writer(f)
            L = ['Username', 'Score']
            csw.writerow(L)
            f.close()
            '''
            self.Highscore.create_csv(self.score)
            self.quit = True
        
            pygame.quit()
            


        #Bullets
        for bullet in self.player_bullets:
            if self.enemy.rect.colliderect(bullet):
                self.score += 1
                self.player_bullets.remove(bullet)
            elif bullet.x > self.WinDims[0]:
                self.player_bullets.remove(bullet)

        for bullet in self.enemy_bullets:
            if self.player.rect.colliderect(bullet):
                self.player_health -= 1
                self.enemy_bullets.remove(bullet)
            elif bullet.x < 0:
                self.enemy_bullets.remove(bullet)

        #Damage
        for bullet in self.player_bullets:
            if self.enemy.rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(enemy_hit))   
                self.player_bullets.remove(bullet)

        for bullet in self.enemy_bullets:
            if self.player.rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(Player_hit))
                self.enemy_bullets.remove(bullet)
                



    def render(self):
        self.window.blit(self.Winbgm, (0,0))
        
        pygame.draw.rect(self.window, self.colors[0], self.border)

        for spaceship in self.spaceships:
            spaceship.draw(self.window)

        for bullet in self.player_bullets:
            pygame.draw.rect(self.window, self.colors[6], bullet)

        for bullet in self.enemy_bullets:
            pygame.draw.rect(self.window, self.colors[2], bullet)


        self.fontrenderer.render(self.player_health, self.window, self.WinDims, self.score)
        
        if self.player_health <= 0:
            self.fontrenderer.gameover(self.window, self.WinDims)

        pygame.display.update()



