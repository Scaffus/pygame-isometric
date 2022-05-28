import pygame
from pathlib import Path
import time
from colors import Colors
from map import Map
from hud import Hud

path = Path(__file__).parent

class Game():
    pygame.init()

    def __init__(self, width, height):
        self.SIZE = self.WIDTH, self.HEIGHT = width, height
        self.RUNNING = True

        pygame.display.set_caption('Isometric Test')
        self.WIN = pygame.display.set_mode(self.SIZE)
        self.DISPLAY = pygame.Surface(self.SIZE)

        self.FPS = 60
        self.CLOCK = pygame.time.Clock()

        self.deltaTime = 0
        self.prev_time = 0
        
        self.MAP = Map(self)
        self.MAP.create()
        
        self.HUD = Hud(self)
        
    def font(self, text="Placeholder", size=24, color=Colors.BLACK, anti_alias=False):
        font = pygame.font.Font(path / 'assets/font/pixeboy.ttf', size)
        return font.render(text, anti_alias, color)

    def draw(self):
        self.DISPLAY.fill(Colors.DARK)
        
        self.MAP.draw()
        self.HUD.draw()
        
        self.WIN.blit(self.DISPLAY, (0, 0))
        pygame.display.update()
        
        self.CLOCK.tick(self.FPS)

    def event_handler(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.RUNNING = False

    def run(self):
        while self.RUNNING:

            now = time.time()
            self.deltaTime = now - self.prev_time
            self.prev_time = now
            
            self.event_handler()
            self.MAP.update()
            self.HUD.update()
            self.draw()

if __name__ == '__main__':
    game = Game(1280, 720)
    game.run()
