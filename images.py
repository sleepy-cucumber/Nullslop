import pygame
from variables import *

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load("sprites/icon.png")
pygame.display.set_icon(icon)
tiles = {
    "spawn": pygame.image.load("sprites/tiles/spawn.png").convert_alpha(),
    "crossroad": pygame.image.load("sprites/tiles/crossroad.png").convert_alpha(),
    "horiz": pygame.image.load("sprites/tiles/horiz.png").convert_alpha(),
    "vert": pygame.image.load("sprites/tiles/vert.png").convert_alpha(),
    "tnoleft": pygame.image.load("sprites/tiles/tnoleft.png").convert_alpha(),
    "tnoright": pygame.image.load("sprites/tiles/tnoright.png").convert_alpha(),
    "tnoup": pygame.image.load("sprites/tiles/tnoup.png").convert_alpha(),
    "tnodown": pygame.image.load("sprites/tiles/tnodown.png").convert_alpha(),
    "lur": pygame.image.load("sprites/tiles/lur.png").convert_alpha(),
    "ldr": pygame.image.load("sprites/tiles/ldr.png").convert_alpha(),
    "ldl": pygame.image.load("sprites/tiles/ldl.png").convert_alpha(),
    "lul": pygame.image.load("sprites/tiles/lul.png").convert_alpha(),
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
beacon = pygame.image.load("sprites/beacon.png")
