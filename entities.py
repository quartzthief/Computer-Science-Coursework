from pygame.sprite import Group
from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(groups)

        #graphics sorting out the animations 
        self.frame_index, self.frames = 0, frames

        #sprite setup
        self.image = self.frames['down'][self.frame_index]
        self.rect = self.image.get_frect(center = pos)


class Player(Entity):
    def __init__(self, pos, frames, groups):
        super().__init__(pos,frames,groups)
        self.direction = vector()
#allow plauyer to move all directions along x and y
    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector()
        if keys[pygame.K_UP]:
            input_vector.y -= 1
        if keys[pygame.K_DOWN]:
            input_vector.y += 1
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        if keys[pygame.K_RIGHT]:
            input_vector.x += 1
        self.direction =  input_vector

#multiplication on this is character speed
    def move(self,dt):
        self.rect.center += self.direction * 300 * dt

    def update(self,dt):
        self.input()
        self.move(dt)