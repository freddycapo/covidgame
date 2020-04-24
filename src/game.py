import pygame
import random
import tkinter as tk
from pygame import *
from tkinter import messagebox
from Player import Player
from FallingObject import FallingObject

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


class Mask(FallingObject):
    def __init__(self, x, y, width, heigth,screen_heigth,vel,sprite):
        super().__init__(x, y, width, heigth,screen_heigth)
        self.vel=vel
        self.sprite=sprite
    pass

class Virus(FallingObject):
    def __init__(self, x, y, width, heigth,screen_heigth,vel,sprite):
        super().__init__(x, y, width, heigth,screen_heigth)
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

star=Player(width//2,heigth*0.85,75,75,width,heigth,sprite)
masks=[]
viruses=[]

score=0
n_virus=5

vel_mask=7
vel_virus=10

run=True
while run: 
    Clock.tick(30)

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