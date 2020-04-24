import pygame

class Player():
    def __init__ (self,x,y,width,heigth,screen_width,screen_heigth,sprite):
        self.x=x
        self.y=y
        self.width=width
        self.heigth=heigth
        self.screen_width=screen_width
        self.screen_heigth=screen_heigth
        self.sprite=sprite
        self.vel=10
        self.isJump=False
        self.jumpLimit=10
        self.jumpcount=self.jumpLimit
        self.hitbox=pygame.Rect(self.x,self.y,self.width,self.heigth)
        self.coeff1=2
        self.coeff2=0.5

    def jump(self):
        keys=pygame.key.get_pressed()
        if not(self.isJump):
            if keys[pygame.K_SPACE]:
                self.isJump=True
                self.walkcount=0

        else:
            if self.jumpcount>= -(self.jumpLimit):
                neg=1
                if self.jumpcount<0:
                    neg= -1
                self.y -= self.jumpcount ** self.coeff1 *self.coeff2 *neg
                self.jumpcount -=1
            
            else:
                self.isJump=False
                self.jumpcount=self.jumpLimit

    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.x<=self.screen_width-self.vel-self.width:
                self.x+=self.vel
        
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.x>=0+self.vel:
                self.x-=self.vel

        else:
            pass

    def draw(self,win):
        self.hitbox=pygame.Rect(self.x+5,self.y+20,self.width-10,self.heigth-30)
        win.blit(pygame.transform.scale(self.sprite,(self.width,self.heigth)),(self.x,self.y))
        #pygame.draw.rect(win,(255,0,0),self.hitbox,1)