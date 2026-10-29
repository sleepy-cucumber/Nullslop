import pygame
from variables import *

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load("sprites/icon.png")
pygame.display.set_icon(icon)
tiles = {
    "spawn": pygame.image.load("sprites/tiles/spawn.png"),
    "crossroad": pygame.image.load("sprites/tiles/crossroad.png"),
    "horiz": pygame.image.load("sprites/tiles/horiz.png"),
    "vert": pygame.image.load("sprites/tiles/vert.png"),
    "tnoleft": pygame.image.load("sprites/tiles/tnoleft.png"),
    "tnoright": pygame.image.load("sprites/tiles/tnoright.png"),
    "tnoup": pygame.image.load("sprites/tiles/tnoup.png"),
    "tnodown": pygame.image.load("sprites/tiles/tnodown.png"),
    "lur": pygame.image.load("sprites/tiles/lur.png"),
    "ldr": pygame.image.load("sprites/tiles/ldr.png"),
    "ldl": pygame.image.load("sprites/tiles/ldl.png"),
    "lul": pygame.image.load("sprites/tiles/lul.png"),
}
ui = {
    "jumps": pygame.image.load("sprites/ui/jumps.png").convert_alpha()
}
enemies = {
    "leafery": pygame.image.load("sprites/enemies/LeaferyEnemy.png"),
    "smallchangebelly": pygame.image.load("sprites/enemies/SmallStomachy.png")
}
choiceenemies = {
    "leafery": pygame.image.load("sprites/choice/enemies/LeaferyChoice.png"),
    "smallchangebelly": pygame.image.load("sprites/choice/enemies/SmallChangePotBelliedChoice.png")
}
choiceupgrades = {
    "paycheck": pygame.image.load("sprites/choice/upgrades/Paycheck.png")
}
gifts = {
    "gift": pygame.image.load("sprites/gifts/gift.png"),
    "goldengift": pygame.image.load("sprites/gifts/goldengift.png"),
    "mine": pygame.image.load("sprites/gifts/tripmine.png")
}
intermission = pygame.image.load("sprites/intermission.png")
player = pygame.image.load("sprites/player.png").convert_alpha()
cont = pygame.image.load("sprites/choice/continue.png")
reroll = pygame.image.load("sprites/choice/reroll.png")
placeholder = pygame.image.load("sprites/choice/placeholder.png")
empty = pygame.image.load("sprites/choice/empty.png")
description = pygame.image.load("sprites/description.png").convert_alpha()
thinglist = pygame.image.load("sprites/activethings.png").convert_alpha()
