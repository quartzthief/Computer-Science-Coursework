from settings import *
from pytmx.util_pygame import load_pygame
#streamlines pathfinding in files
from os.path import join
#getting sprites
from sprites import Sprite, AnimatedSprite
from entities import Player
from groups import AllSprites
#animations
from support import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('game name')
        self.clock = pygame.time.Clock()
        #groups
        self.all_sprites = AllSprites()

        self.import_assets()
        self.setup(self.tmx_maps['world'], 'house')

    def import_assets(self):
        #create dictionarys of asset groups
        self.tmx_maps = {
            'world': load_pygame(join('data','maps','world.tmx')),
            'hospital': load_pygame(join('data','maps','hospital.tmx'))
            }
        self.overworld_frames = {
            'water': import_folder('graphics','tilesets','water'),
            'coast': coast_importer(24,12,'graphics', 'tilesets','coast'),
            'characters': all_character_import('graphics','characters')
        }
        print(self.overworld_frames['characters'])



    def setup(self, tmx_map, player_start_pos):
        #terrain
        for layer in ['Terrain', 'Terrain Top']:
            for x,y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE , y * TILE_SIZE) ,surf, self.all_sprites)

        #objects
        for obj in tmx_map.get_layer_by_name('Objects'):
            Sprite((obj.x, obj.y), obj.image, self.all_sprites)

        
        #entitities
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player' and obj.properties['pos'] == player_start_pos:
                self.player = Player(
                    pos = (obj.x, obj.y), 
                    frames = self.overworld_frames['characters']['player'],
                    groups = self.all_sprites)

        #water and animation of said water
        for obj in tmx_map.get_layer_by_name('Water'):
            for x in range(int(obj.x),int(obj.x + obj.width),TILE_SIZE):
                for y in range(int(obj.y),int(obj.y + obj.height),TILE_SIZE):
                  AnimatedSprite((x,y), self.overworld_frames['water'], self.all_sprites)
        
        #coast
        for obj in tmx_map.get_layer_by_name('Coast'):
            terrain = obj.properties['terrain']
            side = obj.properties['side']
            AnimatedSprite((obj.x,obj.y), self.overworld_frames['coast'][terrain][side], self.all_sprites)
    

    def run(self):
        while True:
            # frame rate
            dt = self.clock.tick() / 1000
            #event loop
            for event in pygame.event.get():
                #exit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #game logic
            #looks at all the spriets in the program and calls the update method
            self.all_sprites.update(dt)

            # fills in gaps in map so it doesnt pait ontop
            self.display_surface.fill('black')
            #draws sprites
            self.all_sprites.draw(self.player.rect.center)

            #displays everything in run loop
            pygame.display.update()


#checking if in main file
if __name__ == '__main__':
    game = Game()
    game.run()