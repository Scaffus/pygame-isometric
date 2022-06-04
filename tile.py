import pygame
from pathlib import Path

path = Path(__file__).parent

class Tile(pygame.sprite.Sprite):
    
    def __init__(self, game, x, y, spr_tiles, type = "grass"):
        self.GAME = game
        self.x = x + self.GAME.WIDTH / 2
        self.y = y + self.GAME.HEIGHT / 3
        self.type = type
        self.spr_tiles = spr_tiles
        
        self.image = self.spr_tiles['grass']
        self.rect = self.image.get_rect()
        
        self.highlighted = False
        
    def draw(self):
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        mpos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mpos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.image.blit(self.spr_tiles['highlighted'], (0, 0))
            
            # if pygame.mouse.get_pressed()[0] == 1:
            #     self.image = self.spr_tiles['stone']
            # elif pygame.mouse.get_pressed()[2] == 1:
            #     self.image = self.spr_tiles['grass']
        
        self.GAME.MAP.map.blit(self.image, (self.x, self.y))
    