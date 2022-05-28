from tkinter.tix import Y_REGION
import pygame
from colors import Colors
from pathlib import Path

path = Path(__file__).parent

class Hud:
    
    def __init__(self, game):
        self.GAME = game

        self.HUD = pygame.Surface(self.GAME.SIZE).convert_alpha()
        self.HUD.fill([0, 0, 0, 0])

        self.FPS = pygame.Surface((0, 0))
        self.MPOS = pygame.Surface((0, 0))
        self.HOVER = pygame.Surface((0, 0))
        
    def draw(self):
        self.HUD.fill([0, 0, 0, 0])
        
        self.HUD.blit(self.FPS, (0, 0))
        self.HUD.blit(self.MPOS, (0, 20))
        self.HUD.blit(self.HOVER, (0, 40))
        
        self.GAME.DISPLAY.blit(self.HUD, (0, 0))
        
    def update(self):
        self.FPS = self.GAME.font(f"{self.GAME.CLOCK.get_fps()}", 24, Colors.WHITE)