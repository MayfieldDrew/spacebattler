import pygame
from bullet import Bullet
from ybullet import yBullet

class Spaceship():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.Living = True
        self.hit = False
        return

    def setAlive(self,alive):
        self.alive = alive
        return

    def moveLeft(self, dx):
        self.x -= dx
        # check the wall
        if self.x < 0:
            self.x = 0
        return

    def moveRight(self, dx, upper_limit):
        self.x += dx
        # check the wall
        if self.x > upper_limit:
            self.x = upper_limit
        return

    def moveUp(self, dy):
        self.y -= dy
        # check the wall
        if self.y < 0:
            self.y = 0
        return

    def moveDown(self, dy, board_height):
        self.y += dy
        # check the wall
        if self.y > board_height - self.height:
            self.y = board_height - self.height
        return

    def fire(self,width,height,color):
        return Bullet(width,height,(self.x + self.width) , (self.y + (self.height /2) - (height/2)),color)
    
    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)):
                self.Living = False
                return True
        return False

    def draw(self, surface):
        if self.Living == True:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            pygame.draw.rect(surface, self.color, rect)
        return

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return

    def checkHitBaddie(self,x,y,w,h):
        if self.hitRectangle(x,y,w,h):
            self.setAlive(False)
            self.hit = True
        
