#IMPORTING
from Object import Object
from Segment import Segment


MAX_CHECK_DISTANCE = 500 #Distance to check for combat to avoid overload


#PARENT CLASS SNAKE - parent class for common properties of both player and enemy snakes
class Snake(Object):
    #CONSTRUCTOR FUNCTION
    def __init__(self, x, y, w, h, filepath):
        #Inheriting from object
        super().__init__(x, y, w, h, filepath)
        #private variables
        self.speed = 7
        self.prevScore = 0
        self.score = 0
        self.segments = []
        self.direction = [] 


    #MOVEMENT
    def update(self, snakes):
        
        #moving player
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        
        
        #calling adding and updating segment functions
        self.addSegment()
        self.updateSegments()

        #Checking for combat
        for snake in snakes:
            direction = [snake.rect.x - self.rect.x, snake.rect.y - self.rect.y]
            distance = ((direction[0]**2)+(direction[1]**2)) ** (1/2)
            
            if distance > MAX_CHECK_DISTANCE or distance == 0:
                continue
            
            for segment in snake.segments:
                if self.rect.colliderect(segment.rect):
                    return True

        return False



    #Drawing length
    def draw(self, window, Camera):
        window.blit(self.texture, Camera.translate(self.rect.x, self.rect.y))
            
        for segment in self.segments:
            window.blit(segment.texture, Camera.translate(segment.rect.x, segment.rect.y))
    
    
    #Score and length
    def addSegment(self):
        
        if self.score - self.prevScore >= 20:
            self.prevScore = self.score
            

            startX = self.direction[0] * -1 * self.rect.w / 1.5
            startY = self.direction[1] * -1 * self.rect.h / 1.5      

            if len(self.segments) == 0:
                startX += self.rect.x
                startY += self.rect.y
            else:
                startX += self.segments[-1].rect.x
                startY += self.segments[-1].rect.y


            newSegment = Segment(startX, startY, self.rect.w, self.rect.h, self.texturePath,self.speed)
            self.segments.append(newSegment)
            


    #Target position for segments
    def updateSegments(self):
        for i in range(len(self.segments)):
            if i == 0:
                self.segments[i].update((self.rect.x, self.rect.y), self.segments)
            else:
                self.segments[i].update((self.segments[i-1].rect.x, self.segments[i-1].rect.y), self.segments)

    
            
    

                
