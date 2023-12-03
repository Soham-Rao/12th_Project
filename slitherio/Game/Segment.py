#importing
import pygame
from Object import Object

#class segemnts - class for the body parts of the snakes
class Segment(Object):
    #constructor function
    def __init__(self, x, y, w, h, filepath,speed):
        #Inheriting from Object
        super().__init__(x, y, w, h, filepath)
        #Private variables
        self.speed = speed

    #updating movement for body parts to follow head
    def update(self, targetPos, segments):
        self.boost()
    

        direction = [targetPos[0] - self.rect.x, targetPos[1] - self.rect.y]
        length = ((direction[0]**2)+(direction[1]**2))**(1/2)
        
        if length < self.rect.w/1.8:
            return
        
        direction[0] /= length
        direction[1] /= length

        self.rect.x += direction[0] * self.speed
        self.rect.y += direction[1] * self.speed

    #boost speed for body on mouse click
    def boost(self):
            #Boosting player
            mousePress = pygame.mouse.get_pressed()
            if mousePress[0] == True:
                self.speed = 13
            elif mousePress[0] == False:
                self.speed = 7

    def price(self, segments):
        pass