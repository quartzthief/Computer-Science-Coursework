from typing import Any
from settings import *
 
class Sprite(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        #floatingpoint rectangel used to give more precise positionioing of sprite rectangles
        self.rect = self.image.get_frect(topleft = pos)

class AnimatedSprite(Sprite):
    def __init__(self,pos,frames,groups):
        self.frame_index, self.frames = 0, frames
        super().__init__(pos, frames[self.frame_index],groups)
    
    def animate(self,dt):
        #a animation speed imported from settings 
        self.frame_index += ANIMATION_SPEED * dt
        #self frame index would eb a float as dt x 4 would not be an integer so needs into to work as intended also modulus of amount of frame index exceeds frames it starts from the beggingin
        self.image = self.frames[int(self.frame_index) % len(self.frames)]

    def update(self,dt):
        self.animate(dt)