import os
import pygame

asset_dict = {}
ASSETS_FOLDER = 'assets'

for folder_name, subfolders, filenames in os.walk(ASSETS_FOLDER):
    for filename in filenames:
        if filename.endswith('.png'):
            asset_name = os.path.splitext(filename)[0]
            asset_path = os.path.join(folder_name, filename)
            asset_image = pygame.image.load(asset_path)
            asset_dict[asset_path[len("assets/"):]] = asset_image

def get_asset(asset_path):
    return asset_dict[asset_path]
