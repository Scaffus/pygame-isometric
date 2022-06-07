import pygame
from pathlib import Path
import os

path = Path(__file__).parent

tiles_path = path / 'assets/textures/'

def load_sprites():
    # sprites = {}
    # for file in os.listdir(tiles_path):
    #     sprites[file] = pygame.image.load(tiles_path + file).convert()
        
    return { file.replace('.png', ''):pygame.transform.scale2x(pygame.image.load(tiles_path / file).convert()) for file in os.listdir(tiles_path)}

