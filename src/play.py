import pygame
import random
import tkinter as tk
from pygame import *
from tkinter import messagebox

pygame.init()

width=800
heigth=500
window=pygame.display.set_mode((width,heigth))

sprite=pygame.image.load("images/stella2.png")
background=pygame.image.load("images/images.jpg")
mask_sprite=pygame.image.load("images/mask.png")
virus_sprite=pygame.image.load("images/virus.png")

Clock=pygame.time.Clock()

font = pygame.font.SysFont("comicsans",30,True)

class Player():
    def __init__ (self,x,y,width,heigth):
        self.x=x
        self.y=y
        self.width=width
        self.heigth=heigth
        self.vel=10
        self.isJump=False
        self.jumpLimit=10
        self.jumpcount=self.jumpLimit
        self.hitbox=pygame.Rect(self.x,self.y,self.width,self.heigth)
        self.coeff1=2
        self.coeff2=0.5

    def jump(self):
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
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.x<=width-self.vel-self.width:
                self.x+=self.vel
        
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.x>=0+self.vel:
                self.x-=self.vel

        else:
            pass

    def draw(self,win):
        self.hitbox=pygame.Rect(self.x+5,self.y+20,self.width-10,self.heigth-30)
        win.blit(pygame.transform.scale(sprite,(self.width,self.heigth)),(self.x,self.y))
        #pygame.draw.rect(win,(255,0,0),self.hitbox,1)


class FallingObject():
    def __init__(self,x,y,width,heigth):
        self.x=x
        self.y=y
        self.width=width
        self.heigth=heigth
        self.hitbox=pygame.Rect(self.x,self.y,self.width,self.heigth)

    def move(self):
        if self.y<heigth+self.heigth:
            self.y+=self.vel
        else:
            self.y=0

    def draw(self,win):
        self.hitbox=pygame.Rect(self.x+15,self.y+20,self.width-30,self.heigth-30)
        win.blit(pygame.transform.scale(self.sprite,(self.width,self.heigth)),(self.x,self.y))


class Mask(FallingObject):
    def __init__(self, x, y, width, heigth,vel,sprite):
        super().__init__(x, y, width, heigth)
        self.vel=vel
        self.sprite=sprite
    pass

class Virus(FallingObject):
    def __init__(self, x, y, width, heigth,vel,sprite):
        super().__init__(x, y, width, heigth)
        self.vel=vel
        self.sprite=sprite
    pass

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

star=Player(width//2,heigth*0.85,75,75)
masks=[]
viruses=[]

score=0
n_virus=5

vel_mask=7
vel_virus=10

run=True
while run: 
    Clock.tick(30)

    keys=pygame.key.get_pressed()
    star.move()
    star.jump()
    star.draw(window)
    
    if len(masks)<=0:
        masks.append(Mask(random.randint(0,width-75),
                            -10,
                            75,
                            75,
                            vel_mask,
                            mask_sprite))

    else:
        mask=masks[0]
        mask.move()
        mask.draw(window)
        if pygame.Rect.colliderect(mask.hitbox,star.hitbox):
            masks.remove(mask)
            score+=1
        
        if mask.y>=heigth+75:
            masks.remove(mask)

    if len(viruses)<=n_virus:
        viruses.append(Virus(random.randint(0,width-75),
                            random.randint(-300,-10),
                            35,
                            35,
                            vel_virus,
                            virus_sprite))
    else:
        for virus in viruses:
            virus.move()
            virus.draw(window)
            if pygame.Rect.colliderect(virus.hitbox,star.hitbox):
                viruses.remove(virus)
                message_box('Sei stato infettato',"Score: "+str(score))
                score=0
                viruses.clear()
                masks.clear()
                break

            if virus.y>=heigth:
                viruses.remove(virus)

    if score<=10:
        n_virus=5
    elif score>10 and score<=20:
        n_virus=6
    elif score>20 and score<=30:
        n_virus=7
    elif score>30 and score<40:
        n_virus=8
    elif score>40 and score<50:
        n_virus=9
    else:
        n_virus=10

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    text=font.render("Score: "+ str(score),1,(0,0,0))
    window.blit(text,(width-150,30))

    pygame.display.update()
    window.blit(pygame.transform.scale(background,(width,heigth)),(0,0))

pygame.quit()