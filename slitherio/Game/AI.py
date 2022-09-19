from Snake import Snake

class AI(Snake):
    #CONSTRUCTOR FUNCTION
    def __init__(self, x, y, w, h, filepath):
        #Inheriting from object
        super().__init__(x, y, w, h, filepath)
        #Private variables
        self.speed = 7


    def update(self, orbs, snakes):
        self.calc_direction(orbs)
        return super().update(snakes) #returning true/false for combat

    def calc_direction(self, orbs):
        
        if len(orbs) == 0: #after all eaten
            return
        
        closestOrb = orbs[0]
        closestDistance = 999999999
        
        #random definition for calculation
        for orb in orbs:
            direction = [orb.rect.x - self.rect.x, orb.rect.y - self.rect.y]
            distance = ((direction[0]**2)+(direction[1]**2))**(1/2)

            #redinition and calculation of vectors
            if distance < closestDistance:
                closestOrb = orb
                closestDistance = distance

        #parent class moves and appends vector
        direction = [closestOrb.rect.x - self.rect.x, closestOrb.rect.y - self.rect.y]
        length = ((direction[0]**2)+(direction[1]**2))**(1/2)
        
        if length == 0: #preventing zerodivision error
            return

        direction[0] /= length
        direction[1] /= length

        self.direction = direction