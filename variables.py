import pygame

FPS = 60
WIDTH = 800
HEIGHT = 600
pygame.init()
ui_font = pygame.font.Font("font/AccanthisadfstdRegular.otf", 16)
gih_count_font = pygame.font.Font("font/AccanthisadfstdRegular.otf", 24)

background_colors = {
    "1": (50, 0, 120),
    "5": [
        (20, 100, 80),
        (100, 100, 20),
        (40, 100, 20)
    ],
    "10": [
        (45, 180, 0),
        (100, 0, 180)
    ],
    "20": [
        (180, 0, 130),
        (180, 115, 0)
    ],
    "30": (20, 0, 200),
    "40": (200, 200, 200)
}
