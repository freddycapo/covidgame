import pygame

class FallingObject():
    def __init__(self,x,y,width,heigth,screen_heigth):
        self.x=x
        self.y=y
        self.screen_heigth=screen_heigth
        self.width=width
        self.heigth=heigth
        self.hitbox=pygame.Rect(self.x,self.y,self.width,self.heigth)

    def move(self):
        if self.y<self.screen_heigth+self.heigth:
            self.y+=self.vel
        else:
            self.y=0

    def draw(self,win):
        self.hitbox=pygame.Rect(self.x+15,self.y+20,self.width-30,self.heigth-30)
        win.blit(pygame.transform.scale(self.sprite,(self.width,self.heigth)),(self.x,self.y))