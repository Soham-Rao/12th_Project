#IMPORTING 
from Object import Object

score_increment = 5

#CLASS ORBS - class for food
class Orbs(Object):
    #CONSTRUCTOR FUNCTION
    def __init__(self, x, y, r, filepath):
        #Inheriting from object
        super().__init__(x, y, r, r, filepath)

    #UPDATING COLLISION
    def update(self,snakes): 
        for snake in snakes:
            if self.rect.colliderect(snake.rect):
                snake.score += score_increment
                return True
        return False