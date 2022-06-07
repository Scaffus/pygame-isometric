from imp import PKG_DIRECTORY
import pygame
from pathlib import Path
from colors import Colors

path = Path(__file__).parent

class Player(pygame.sprite.Sprite):
    def __init__(self, name, color, x, y, game):
        self.GAME = game

        self.name = name
        self.color = color
        self.image = self.GAME.SPRITES['elephant']
        self.rect = pygame.image.get_rect()

        self.x = x
        self.y = y

        self.vel_x = 0
        self.vel_y = 0

    def draw(self):
        self.GAME.DISPLAY.blit(self.image, (self.x, self.y))

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        