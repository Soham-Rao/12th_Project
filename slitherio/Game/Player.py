#IMPORTING
import pygame
from Snake import Snake

#CLASS PLAYER - class for properties of the player
class Player(Snake):
    #CONSTRUCTOR FUNCTION
    def __init__(self, x, y, w, h, filepath, WinDims):
        #Inheriting from object
        super().__init__(x, y, w, h, filepath)
        #private variables
        self.WinDims = WinDims
        


    #MOVEMENT
    def update(self, orbs, snakes):
        #moving player
        self.calc_direction()
        self.boost()

        #moving and drawing in parent class snake         
        return super().update(snakes) #returning true/false for combat
            

    #check direction to move in - mouse
    def calc_direction(self):

        #Movement with mouse
        mousePos = pygame.mouse.get_pos()
        worldPos = (((mousePos[0] - self.WinDims[0]/2) + self.rect.x) , ((mousePos[1] - self.WinDims[1]/2) + self.rect.y))    #correctly returning mouse position
        
        self.direction = [worldPos[0] - self.rect.x, worldPos[1] - self.rect.y]
        
        vectLength = ((self.direction[0]**2)+(self.direction[1]**2))**(1/2) #normalizing vector
        
        if vectLength == 0:
            return

        self.direction =  [self.direction[0] / vectLength, self.direction[1] / vectLength] 
        
    #boost function on mouse click
    def boost(self):
            #Boosting player
            mousePress = pygame.mouse.get_pressed()
            if mousePress[0] == True:
                self.speed = 12
            elif mousePress[0] == False:
                self.speed = 8
                