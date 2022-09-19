#IMPORTING

import pygame
import random
import os
import csv
from Player import Player
from Orbs import Orbs
from Camera import Camera
from AI import AI
from Font import Font
from Slither_Highscore import Highscore

#DEFINING VARIABLES

FPS = 60
NUM_ORBS = 150
NUM_AI = 7

PLAYER_START_W = 50
PLAYER_START_H = 50

PLAYER_START_X = 0
PLAYER_START_Y = 0

PLAYER_TEXTURE = "textures\\body_red.png"

#MAINGAME CLASS

class MainGame_Slither:
    #CONSTRUCTOR FUNCTION
    def __init__(self):
        pygame.init()


        self.WinDims = (1000,700)
        self.window = pygame.display.set_mode(self.WinDims)
        pygame.display.set_caption("Slither.io  ")
        self.WinColor_grey = (75,75,75)
        self.quit = False
        self.clock = pygame.time.Clock()

        self.textures = [os.path.join("textures","blue_orb.png"), os.path.join("textures","green_orb.png"), os.path.join("textures","orange_orb.png"), 
        os.path.join("textures","purple_orb.png"), os.path.join("textures","yellow_orb.png"), os.path.join("textures","red_orb.png")]
        
        self.Camera  = Camera(PLAYER_START_X, PLAYER_START_Y, (PLAYER_START_W,PLAYER_START_H), self.WinDims)
        self.player = Player(PLAYER_START_X, PLAYER_START_Y, PLAYER_START_W, PLAYER_START_H, random.choice(self.textures), self.WinDims)
        self.orbs = []
        self.snakes = []

        self.fontRenderer = Font()
        self.highscore = Highscore()





    #INITIATING WORLD AND CALLING PLAY AND SPAWNING ORBS
    def init(self):
                
        for i in range(NUM_ORBS):
            randx = random.randint(-self.WinDims[0] * 3, self.WinDims[0] * 3)
            randy = random.randint(-self.WinDims[1] * 3, self.WinDims[1] * 3)
            randr = random.randint(10,PLAYER_START_W)
            randtexture = random.choice(self.textures)

            newOrbs = Orbs(randx, randy, randr, randtexture)
            self.orbs.append(newOrbs)

           

        
        #Creating PLAYER and AI in snake list

        self.snakes.append(self.player)

        for i in range(NUM_AI):
            randx = random.randint(-self.WinDims[0] * 3, self.WinDims[0] * 3)
            randy = random.randint(-self.WinDims[1] * 3, self.WinDims[1] * 3)
            
            randTexture = random.choice(self.textures)

            newAI = AI(randx,randy,PLAYER_START_W,PLAYER_START_H,randTexture)
            self.snakes.append(newAI)

        #Playing game
        self.play()         


    #CALLING UPDATE AND RENDER
    def play(self):
        while self.quit == False:
            self.update()
            self.render()


    #EVENTS AND CLOCK 
    def update(self):
        self.clock.tick(FPS)
        
        #Window events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #SCORES IN CSV
                '''
                f = open("slither_highscore.csv", "w", newline = "")
                csw = csv.writer(f)
                L = ['Username', 'Score']
                csw.writerow(L)
                f.close()
                '''
                self.highscore.create_csv(self.player.score)
                self.quit = True
        

        #Orb events
        for orb in self.orbs:
            if orb.update(self.snakes):
                self.orbs.remove(orb)

        if len(self.orbs) <= 100:
            for i in range(NUM_ORBS):
                randx = random.randint(-self.WinDims[0] * 3, self.WinDims[0] * 3)
                randy = random.randint(-self.WinDims[1] * 3, self.WinDims[1] * 3)
                randr = random.randint(10,PLAYER_START_W)
                randtexture = random.choice(self.textures)

                newOrbs = Orbs(randx, randy, randr, randtexture)
                self.orbs.append(newOrbs)


        #snakes events(player and AI)
        for snake in self.snakes:
            if snake.update(self.orbs, self.snakes) == True: #combat
                #spawning orbs for head
                startx = snake.rect.x
                starty = snake.rect.y
                size = PLAYER_START_W
                texture = random.choice(self.textures)

                newOrbs = Orbs(startx, starty, size, texture)
                self.orbs.append(newOrbs)

                
                #spawning orbs for body
                for segment in snake.segments:
                    startx = segment.rect.x
                    starty = segment.rect.y
                    size = PLAYER_START_W
                    texture = random.choice(self.textures)

                    newOrbs = Orbs(startx, starty, size, texture)
                    self.orbs.append(newOrbs)


                #removing snake
                snake.segments.clear() #removing body part
                self.snakes.remove(snake) #removing head

        if len(self.snakes) <= 3:
            for i in range(NUM_AI):
                randx = random.randint(-self.WinDims[0] * 1.5, self.WinDims[0] * 1.5)
                randy = random.randint(-self.WinDims[1] * 1.5, self.WinDims[1] * 1.5)
                
                randTexture = random.choice(self.textures)

                newAI = AI(randx,randy,PLAYER_START_W,PLAYER_START_H,randTexture)
                self.snakes.append(newAI)


        
        
        #Camera events
        self.Camera.update(self.player.rect.x, self.player.rect.y)

        

        

    #FILLING AND DWARING WINDOW
    def render(self):
        #Filling color 
        self.window.fill(self.WinColor_grey)
        
        #drawing orbs
        for orb in self.orbs:
            orb.draw(self.window, self.Camera)

        #drawing snakes
        for snake in self.snakes:
            snake.draw(self.window, self.Camera)

        #drawing score
        self.fontRenderer.renderFont(self.window, self.player.score)


    #UPDATING WINDOW
        pygame.display.update()






