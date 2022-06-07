from tkinter.tix import Y_REGION
import pygame
from colors import Colors
from pathlib import Path

path = Path(__file__).parent

class Hud:
    
    def __init__(self, game):
        self.GAME = game

        self.HUD_S = pygame.Surface(self.GAME.SIZE).convert_alpha()
        self.HUD_S.fill([0, 0, 0, 0])

        self.FPS = pygame.Surface((0, 0))
        self.MPOS = pygame.Surface((0, 0))
        self.HOVER = pygame.Surface((0, 0))

        self.HOTBAR = Hotbar(5 + 1, self.GAME)
        self.HOTBAR.create()
        
    def draw(self):
        self.HUD_S.fill([0, 0, 0, 0])
        
        self.HUD_S.blit(self.FPS, (0, 0))
        self.HUD_S.blit(self.MPOS, (0, 20))
        self.HUD_S.blit(self.HOVER, (0, 40))
        self.HOTBAR.draw()
        
        self.GAME.DISPLAY.blit(self.HUD_S, (0, 0))
        
    def update(self):
        self.FPS = self.GAME.font(f"{self.GAME.CLOCK.get_fps()}", 24, Colors.WHITE)


class Hotbar:
    def __init__(self, count, game):
        self.GAME = game
        self.count = count

        self.HOTBAR_S = pygame.Surface(self.GAME.SIZE).convert_alpha()
        self.HOTBAR_S.fill([0, 0, 0, 0])

        self.slot_s = self.GAME.SPRITES['inv_slot']
        self.slot_size_x, self.slot_size_y = self.slot_s.get_size()

        self.x = self.GAME.WIDTH / 2 - self.count * self.slot_size_x / 2
        self.y = self.GAME.HEIGHT / 1.15

        self.selected_slot_s = self.GAME.SPRITES['inv_slot_selected']
        self.selected_slot = 1
    
    def create(self):
        for i in range(1, self.count):
            self.HOTBAR_S.blit(self.slot_s, (i * self.slot_size_x, 0))

    def draw(self):

        self.update()
        self.GAME.HUD.HUD_S.blit(self.HOTBAR_S, (self.x, self.y))

    def update(self):
        self.HOTBAR_S.blit(self.selected_slot_s, ((self.selected_slot + 1) * self.slot_size_x, 0))