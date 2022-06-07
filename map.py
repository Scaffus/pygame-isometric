import pygame
from tile import Tile
from colors import Colors

class Map:
    
    def __init__(self, game, width, height):
        self.GAME = game
        self.width = width
        self.height = height
        self.tile_size = 32 * 2
        self.tiles = []
        self.map = pygame.Surface(self.GAME.SIZE)

    def create(self):
        for x in range(self.width):
            for y in range(self.height):
                self.tiles.append(
                    Tile(self.GAME,
                         x * .5 * self.tile_size + y * -.5 * self.tile_size,
                         x * .25 * self.tile_size + y * .25 * self.tile_size,
                         self.GAME.SPRITES)
                )
                
    def draw(self):
        self.map.fill(Colors.DARK)
        
        for tile in self.tiles:
            tile.draw()
            
        self.GAME.DISPLAY.blit(self.map, (0, 0))