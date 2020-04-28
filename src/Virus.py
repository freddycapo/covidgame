from FallingObject import FallingObject

class Virus(FallingObject):
    def __init__(self, x, y, width, heigth,screen_heigth,vel,sprite):
        super().__init__(x, y, width, heigth,screen_heigth)
        self.vel=vel
        self.sprite=sprite
    