import pygame
from variables import *

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load("sprites/icon.png")
pygame.display.set_icon(icon)
tiles = {
    "spawn": pygame.image.load("sprites/tiles/spawn.png").convert_alpha(),
    "crossroad": {
        "normal": pygame.image.load("sprites/tiles/crossroad/crossroad.png").convert_alpha(),
        "cracked": pygame.image.load("sprites/tiles/crossroad/crossroadcracked.png").convert_alpha(),
        "break": pygame.image.load("sprites/tiles/crossroad/crossroadbreak.png").convert_alpha()
    },
    "horiz": {
        "normal": pygame.image.load("sprites/tiles/horiz/horiz.png").convert_alpha(),
        "cracked": pygame.image.load("sprites/tiles/horiz/horizcracked.png").convert_alpha(),
        "break": pygame.image.load("sprites/tiles/horiz/horizbreak.png").convert_alpha()
    },
    "vert": {
        "normal": pygame.image.load("sprites/tiles/vert/vert.png").convert_alpha(),
        "cracked": pygame.image.load("sprites/tiles/vert/vertcracked.png").convert_alpha(),
        "break": pygame.image.load("sprites/tiles/vert/vertbreak.png").convert_alpha()
    },
    "tnoleft": {
        "normal": pygame.image.load("sprites/tiles/tnoleft/tnoleft.png").convert_alpha(),
        "cracked": pygame.image.load("sprites/tiles/tnoleft/tnoleftcracked.png").convert_alpha(),
        "break": pygame.image.load("sprites/tiles/tnoleft/tnoleftbreak.png").convert_alpha()
    },
    "tnoright": {
        "normal": pygame.image.load("sprites/tiles/tnoright/tnoright.png").convert_alpha(),
        "cracked": pygame.image.load("sprites/tiles/tnoright/tnorightcracked.png").convert_alpha(),
        "break": pygame.image.load("sprites/tiles/tnoright/tnorightbreak.png").convert_alpha()
    },
    "tnoup": {
        "normal": pygame.image.load("sprites/tiles/tnoup/tnoup.png").convert_alpha(),
        "cracked": pygame.image.load("sprites/tiles/tnoup/tnoupcracked.png").convert_alpha(),
        "break": pygame.image.load("sprites/tiles/tnoup/tnoupbreak.png").convert_alpha()
    },
    "tnodown": {
        "normal": pygame.image.load("sprites/tiles/tnodown/tnodown.png").convert_alpha(),
        "cracked": pygame.image.load("sprites/tiles/tnodown/tnodowncracked.png").convert_alpha(),
        "break": pygame.image.load("sprites/tiles/tnodown/tnodownbreak.png").convert_alpha()
    },
    "lur": {
        "normal": pygame.image.load("sprites/tiles/lur/lur.png").convert_alpha(),
        "cracked": pygame.image.load("sprites/tiles/lur/lurcracked.png").convert_alpha(),
        "break": pygame.image.load("sprites/tiles/lur/lurbreak.png").convert_alpha()
    },
    "ldr": {
        "normal": pygame.image.load("sprites/tiles/ldr/ldr.png").convert_alpha(),
        "cracked": pygame.image.load("sprites/tiles/ldr/ldrcracked.png").convert_alpha(),
        "break": pygame.image.load("sprites/tiles/ldr/ldrbreak.png").convert_alpha()
    },
    "ldl": {
        "normal": pygame.image.load("sprites/tiles/ldl/ldl.png").convert_alpha(),
        "cracked": pygame.image.load("sprites/tiles/ldl/ldlcracked.png").convert_alpha(),
        "break": pygame.image.load("sprites/tiles/ldl/ldlbreak.png").convert_alpha()
    },
    "lul": {
        "normal": pygame.image.load("sprites/tiles/lul/lul.png").convert_alpha(),
        "cracked": pygame.image.load("sprites/tiles/lul/lulcracked.png").convert_alpha(),
        "break": pygame.image.load("sprites/tiles/lul/lulbreak.png").convert_alpha()
    }
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
