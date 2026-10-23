import pygame
from variables import *
import images
from random import choice

offsetx = WIDTH//2
offsety = HEIGHT//2
available_enemies = ["leafery", "smallchange"]
map_tile_ids = []
generating = False
total_weight = 0
max_weight = 0
tile_w_left = ["crossroad", "horiz", "tnoup", "tnodown", "tnoright"]
tile_w_right = ["crossroad", "horiz", "tnoup", "tnodown", "tnoleft"]
tile_w_up = ["crossroad", "vert", "tnoleft", "tnodown", "tnoright"]
tile_w_down = ["crossroad", "vert", "tnoup", "tnoleft", "tnoright"]
active_things = ["0Paycheck"]
# 0 - upgrade, 1 - greater curse, 2 - curse, 3 - temporary enemy, 4 - enemy
level = 1

def generate_map():
    global total_weight, generating
    
    map_sprs.empty()
    map_tile_ids.clear()
    total_weight = 0
    spawn_tile = Tile(0, 0, "spawn")
    map_sprs.add(spawn_tile)
    generation_queue = [spawn_tile]
    while generation_queue and total_weight < max_weight:
        current_tile = generation_queue.pop(0)
        for side in current_tile.sides:
            if total_weight >= max_weight:
                break
            new_x, new_y = current_tile.mapx, current_tile.mapy
            if side == 1:
                new_y -= 250
            elif side == 2:
                new_x += 250
            elif side == 3:
                new_y += 250
            elif side == 4:
                new_x -= 250
            already_exists = any(t.mapx == new_x and t.mapy == new_y for t in map_sprs)
            if not already_exists:
                if side == 1:
                    new_tile = Tile(new_x, new_y, choice(tile_w_down))
                elif side == 2:
                    new_tile = Tile(new_x, new_y, choice(tile_w_left))
                elif side == 3:
                    new_tile = Tile(new_x, new_y, choice(tile_w_up))
                elif side == 4:
                    new_tile = Tile(new_x, new_y, choice(tile_w_right))
                map_sprs.add(new_tile)
                generation_queue.append(new_tile)
                
    generating = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.jump_cd = 10
        self.status = 0
        self.mapx = 0
        self.mapy = 0
        self.height = 100
        self.max_jumps = 1
        self.jumps = self.max_jumps
        self.ability_cd = 30
        self.max_stamina = 600
        self.stamina = self.max_stamina
        self.max_platform = 120
        self.platform = self.max_platform
        self.speed = 3
        self.image = images.player
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.mapx+offsetx, self.mapy+offsety)
        self.mask = pygame.mask.from_surface(self.image)

    def handle_input(self, keys):
        global offsetx, offsety, generating
        if generating == False:
            if keys[pygame.K_w] and not keys[pygame.K_LEFTBRACKET] and not keys[pygame.K_RIGHTBRACKET]:
                offsety += self.speed
                self.mapy -= self.speed
            if keys[pygame.K_s] and not keys[pygame.K_LEFTBRACKET] and not keys[pygame.K_RIGHTBRACKET]:
                offsety -= self.speed
                self.mapy += self.speed
            if keys[pygame.K_a] and not keys[pygame.K_LEFTBRACKET] and not keys[pygame.K_RIGHTBRACKET]:
                offsetx += self.speed
                self.mapx -= self.speed
            if keys[pygame.K_d] and not keys[pygame.K_LEFTBRACKET] and not keys[pygame.K_RIGHTBRACKET]:
                offsetx -= self.speed
                self.mapx += self.speed
            if keys[pygame.K_SPACE]:
                if self.jump_cd <= 0:
                    if self.jumps >= 1:
                        self.jump_cd = 10
                        self.height += 30
                        self.jumps -= 1
            if keys[pygame.K_LEFTBRACKET] and not keys[pygame.K_RIGHTBRACKET]:
                if keys[pygame.K_w]:
                    if self.ability_cd <= 0:
                        offsety += self.speed * 2
                        self.mapy -= self.speed * 2
                        self.stamina -= 1
                    else: 
                        offsety += self.speed
                        self.mapy -= self.speed
                if keys[pygame.K_s]:
                    if self.ability_cd <= 0:
                        offsety -= self.speed * 2
                        self.mapy += self.speed * 2
                        self.stamina -= 1
                    else:
                        offsety -= self.speed
                        self.mapy += self.speed
                if keys[pygame.K_a]:
                    if self.ability_cd <= 0:
                        offsetx += self.speed * 2
                        self.mapx -= self.speed * 2
                        self.stamina -= 1
                    else:
                        offsetx += self.speed
                        self.mapx -= self.speed
                if keys[pygame.K_d]:
                    if self.ability_cd <= 0:
                        offsetx -= self.speed * 2
                        self.mapx += self.speed * 2
                        self.stamina -= 1
                    else:
                        offsetx -= self.speed
                        self.mapx += self.speed
                if self.stamina <= 0:
                    self.ability_cd = 150
            else:
                if self.stamina < self.max_stamina:
                    self.stamina += 0.5
            if keys[pygame.K_RIGHTBRACKET] and not keys[pygame.K_LEFTBRACKET]:
                if keys[pygame.K_w]:
                    if self.ability_cd <= 0:
                        offsety += self.speed * 2
                        self.mapy -= self.speed * 2
                        self.stamina -= 1
                        if self.platform > 0:
                            self.stamina -= 1
                            self.platform -= 1
                            self.height += 2
                    else: 
                        offsety += self.speed
                        self.mapy -= self.speed
                if keys[pygame.K_s]:
                    if self.ability_cd <= 0:
                        offsety -= self.speed * 2
                        self.mapy += self.speed * 2
                        self.stamina -= 1
                        if self.platform > 0:
                            self.stamina -= 1
                            self.platform -= 1
                            self.height += 2
                    else:
                        offsety -= self.speed
                        self.mapy += self.speed
                if keys[pygame.K_a]:
                    if self.ability_cd <= 0:
                        offsetx += self.speed * 2
                        self.mapx -= self.speed * 2
                        self.stamina -= 1
                        if self.platform > 0:
                            self.stamina -= 1
                            self.platform -= 1
                            self.height += 2
                    else:
                        offsetx += self.speed
                        self.mapx -= self.speed
                if keys[pygame.K_d]:
                    if self.ability_cd <= 0:
                        offsetx -= self.speed * 2
                        self.mapx += self.speed * 2
                        self.stamina -= 1
                        if self.platform > 0:
                            self.stamina -= 1
                            self.platform -= 1
                            self.height += 2
                    else:
                        offsetx -= self.speed
                        self.mapx += self.speed
                if self.stamina <= 0:
                    self.ability_cd = 240
            else:
                if self.stamina < self.max_stamina:
                    self.stamina += 0.5

    def update(self):
        global offsetx, offsety
        self.rect.topleft = (self.mapx+offsetx, self.mapy+offsety)
        self.jump_cd -= 1
        self.ability_cd -= 1
        if self.height <= 0:
            if self.status == 0 or self.status == 1:
                self.mapx = 0
                self.mapy = 0
                offsetx = WIDTH//2
                offsety = HEIGHT//2
                self.height = 100
            elif self.status == 2:
                self.status = 3
        self.image.set_alpha(max(0, min(255, ((self.height * 2.55)))))

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        global total_weight
        super().__init__()
        self.type = type
        self.weight = None
        self.mapx = x
        self.mapy = y
        self.weight = 0
        self.has_generated = False
        if self.type == "spawn":
            self.image = images.tiles["spawn"]
            self.sides = [1,2,3,4]
            self.weight = 0
            self.id = 0
        elif self.type == "horiz":
            self.image = images.tiles["horiz"]
            self.sides = [2,4]
            self.weight = 7
            self.id = max(map_tile_ids) + 1
        elif self.type == "vert":
            self.image = images.tiles["vert"]
            self.sides = [1,3]
            self.weight = 7
            self.id = max(map_tile_ids) + 1
        elif self.type == "crossroad":
            self.image = images.tiles["crossroad"]
            self.sides = [1,2,3,4]
            self.weight = 13
            self.id = max(map_tile_ids) + 1
        elif self.type == "tnoleft":
            self.image = images.tiles["tnoleft"]
            self.sides = [1,2,3]
            self.weight = 10
            self.id = max(map_tile_ids) + 1
        elif self.type == "tnoright":
            self.image = images.tiles["tnoright"]
            self.sides = [1,3,4]
            self.weight = 10
            self.id = max(map_tile_ids) + 1
        elif self.type == "tnoup":
            self.image = images.tiles["tnoup"]
            self.sides = [2,3,4]
            self.weight = 10
            self.id = max(map_tile_ids) + 1
        elif self.type == "tnodown":
            self.image = images.tiles["tnodown"]
            self.sides = [1,2,4]
            self.weight = 10
            self.id = max(map_tile_ids) + 1
        map_tile_ids.append(self.id)
        total_weight += self.weight
        self.rect = self.image.get_rect()
        self.firstmask = pygame.mask.from_surface(self.image)
        self.w, self.h = self.image.get_size()
        self.mask = self.firstmask.scale((self.w-2, self.h-2))
        self.rect.topleft = ((self.mapx + offsetx - 125, self.mapy + offsety - 125))

    def update(self):
        global total_weight, generating
        self.rect.topleft = ((self.mapx + offsetx - 125, self.mapy + offsety - 125))
        if generating == True and total_weight < max_weight and not self.has_generated:
            self.has_generated = True
        elif generating == True and total_weight >= max_weight:
            generating = False
        map_sprs.remove(self)
        if pygame.sprite.spritecollide(self, map_sprs, False, pygame.sprite.collide_mask):
            self.kill()
            if self.id in map_tile_ids:
                map_tile_ids.pop(map_tile_ids.index(self.id))
            total_weight -= self.weight
        map_sprs.add(self)

class JumpUI(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.amount = 1
        self.image = images.ui["jumps"]
        self.x = WIDTH // 2 - 16
        self.y = HEIGHT - 100
        self.rect = self.image.get_rect()
    
    def update(self):
        self.amount = player.jumps
        self.image.set_alpha(200)
        self.rect.topleft = (self.x, self.y)

class Intermission(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mapx = 0
        self.mapy = 0
        self.image = images.intermission
        self.type = "start"
        self.enemychoices = ["leafery"]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global offsetx, offsety
        if player.status == 0 and self.type == "start":
            choice1.type = "none"
            choice2.type = "continue"
            choice3.type = "none"
        if player.status == 1 and self.type == "enemy":
            choice1.type = "enemy"
            choice2.type = "enemy"
            choice3.type = "enemy"
        self.rect.topleft = (self.mapx-200+offsetx, self.mapy-150+offsety)

class Choice1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mapx = -99
        self.mapy = -72
        self.open = False
        self.type = None
        self.image = images.placeholder
        self.thing = None
        self.gambled = False
        self.choicecd = 0
        self.rect = self.image.get_rect()

    def update(self, keys):
        global offsetx, offsety, generating, max_weight
        if self.type == "none":
            self.image = images.empty
        elif self.type == "enemy":
            if self.gambled == False:
                self.thing = choice(available_enemies)
                self.gambled = True
                if self.thing == "leafery":
                    self.image = images.choiceenemies["leafery"]
                elif self.thing == "smallchange":
                    self.image = images.choiceenemies["smallchangebelly"]
            else:
                pass
            if -50 <= player.mapx - self.mapx <= 20 and -50 <= player.mapy - self.mapy <= 20:
                self.open = True
                if self.thing == "leafery":
                    description.change_text("Leafery", "Hey guys! It's me, Leafery.")
                elif self.thing == "smallchange":
                    description.change_text("Pot-Bellied Small Change", "Meloch puzataa")
                if keys[pygame.K_f] and self.choicecd <= 0:
                    match self.thing:
                        case "leafery":
                            active_things.append("4Leafery")
                            self.thing = None
                            self.image = images.empty
                            self.type = "none"
                            self.choicecd = 30
                        case "smallchange":
                            active_things.append("4SmallChange")
                            self.thing = None
                            self.image = images.empty
                            self.type = "none"
                            self.choicecd = 30
                    if choice2.next == "level":
                        player.status = 2
                        generating = True
                        player.mapx = -15
                        player.mapy = -15
                        offsetx = WIDTH//2 + 15
                        offsety = HEIGHT//2 + 15
                        max_weight = level*40
                        generate_map()
                        if level % 3 == 0:
                            choice2.next = "intermissioncurse"
                        elif str(level)[len(str(level))-1] == 3 or str(level)[len(str(level))-1] == 5:
                            choice2.next = "intermissionupgrade"
                        else:
                            choice2.next = "level"
                    
            else:
                self.open = False
        else:
            pass
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.mapx-13+offsetx, self.mapy-13+offsety)
        self.choicecd -= 1

class Choice2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mapx = 1
        self.mapy = -98
        self.open = False
        self.type = None
        self.next = "intermissionenemy"
        self.thing = None
        self.gambled = False
        self.choicecd = 0
        self.image = images.placeholder
        self.rect = self.image.get_rect()

    def update(self, keys):
        global offsetx, offsety, generating, max_weight
        if self.type == "continue":
            self.image = images.cont
            if -50 <= player.mapx - self.mapx <= 20 and -50 <= player.mapy - self.mapy <= 20:
                self.open = True
                description.change_text("Continue", "Press F")
                if keys[pygame.K_f] and self.choicecd <= 0:
                    self.open = False
                    if self.next == "intermissionenemy":
                        player.status = 1
                        intermission.type = "enemy"
                        choice1.gambled = False
                        choice2.gambled = False
                        choice3.gambled = False
                        if level % 2 != 0 and str(level)[len(str(level))-1] != 3 and str(level)[len(str(level))-1] != 5 and level % 3 != 0:
                            self.next = "level"
                        self.choicecd = 30
                    elif self.next == "level":
                        player.status = 2
                        generating = True
                        player.mapx = -15
                        player.mapy = -15
                        offsetx = WIDTH//2 + 15
                        offsety = HEIGHT//2 + 15
                        max_weight = level*40
                        generate_map()
                        map_sprs.add(Tile(0,0,"spawn"))
                        if level % 2 == 0:
                            self.next = "intermissionenemy"
                        elif level % 3 == 0:
                            self.next = "intermissioncurse"
                        elif str(level)[len(str(level))-1] == 3 or str(level)[len(str(level))-1] == 5:
                            self.next = "intermissionupgrade"
                        else:
                            self.next = "level"
            else:
                self.open = False
        elif self.type == "none":
            self.image = images.empty
        elif self.type == "enemy":
            if self.gambled == False:
                self.gambled = True
                self.thing = choice(available_enemies)
                if self.thing == "leafery":
                    self.image = images.choiceenemies["leafery"]
                elif self.thing == "smallchange":
                    self.image = images.choiceenemies["smallchangebelly"]
            else:
                pass
            if -50 <= player.mapx - self.mapx <= 20 and -50 <= player.mapy - self.mapy <= 20:
                self.open = True
                if self.thing == "leafery":
                    description.change_text("Leafery", "Hey guys! It's me, Leafery.")
                elif self.thing == "smallchange":
                    description.change_text("Pot-Bellied Small Change", "Meloch puzataa")
                if keys[pygame.K_f] and self.choicecd <= 0:
                    self.open = False
                    match self.thing:
                        case "leafery":
                            active_things.append("4Leafery")
                            self.thing = None
                            self.image = images.empty
                            self.type = "none"
                            self.choicecd = 30
                        case "smallchange":
                            active_things.append("4SmallChange")
                            self.thing = None
                            self.image = images.empty
                            self.type = "none"
                            self.choicecd = 30
                    if self.next == "level":
                        player.status = 2
                        generating = True
                        player.mapx = -15
                        player.mapy = -15
                        offsetx = WIDTH//2 + 15
                        offsety = HEIGHT//2 + 15
                        max_weight = level*40
                        generate_map()
                        if level % 3 == 0:
                            self.next = "intermissioncurse"
                        elif str(level)[len(str(level))-1] == 3 or str(level)[len(str(level))-1] == 5:
                            self.next = "intermissionupgrade"
                        else:
                            self.next = "level"
            else:
                self.open = False
        else:
            pass
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.mapx-13+offsetx, self.mapy-13+offsety)
        self.choicecd -= 1

class Choice3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mapx = 101
        self.mapy = -72
        self.type = None
        self.open = False
        self.image = images.placeholder
        self.thing = None
        self.gambled = False
        self.choicecd = 0
        self.rect = self.image.get_rect()

    def update(self, keys):
        global offsetx, offsety, generating, max_weight
        if self.type == "none":
            self.image = images.empty
        elif self.type == "enemy":
            if self.gambled == False:
                self.gambled = True
                self.thing = choice(available_enemies)
                if self.thing == "leafery":
                    self.image = images.choiceenemies["leafery"]
                elif self.thing == "smallchange":
                    self.image = images.choiceenemies["smallchangebelly"]
            else:
                pass
            if -50 <= player.mapx - self.mapx <= 20 and -50 <= player.mapy - self.mapy <= 20:
                self.open = True
                if self.thing == "leafery":
                    description.change_text("Leafery", "Hey guys! It's me, Leafery.")
                elif self.thing == "smallchange":
                    description.change_text("Pot-Bellied Small Change", "Meloch puzataa")
                if keys[pygame.K_f] and self.choicecd <= 0:
                    match self.thing:
                        case "leafery":
                            active_things.append("4Leafery")
                            self.thing = None
                            self.image = images.empty
                            self.type = "none"
                            self.choicecd = 30
                        case "smallchange":
                            active_things.append("4SmallChange")
                            self.thing = None
                            self.image = images.empty
                            self.type = "none"
                            self.choicecd = 30
                    if choice2.next == "level":
                        player.status = 2
                        generating = True
                        player.mapx = -15
                        player.mapy = -15
                        offsetx = WIDTH//2 + 15
                        offsety = HEIGHT//2 + 15
                        max_weight = level*40
                        generate_map()
                        if level % 3 == 0:
                            choice2.next = "intermissioncurse"
                        elif str(level)[len(str(level))-1] == 3 or str(level)[len(str(level))-1] == 5:
                            choice2.next = "intermissionupgrade"
                        else:
                            choice2.next = "level"
            else:
                self.open = False
        else:
            pass
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.mapx-13+offsetx, self.mapy-13+offsety)
        self.choicecd -= 1

class Description(pygame.sprite.Sprite):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.image = images.description
        self.image.set_alpha(200)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,HEIGHT-100)

    def change_text(self, name, description):
        self.name = name
        self.description = description

    def update(self):
        pass

class Reroll(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mapx = 140
        self.mapy = 0
        self.image = images.reroll
        self.cd = 0
        self.open = False
        self.rect = self.image.get_rect()

    def update(self, keys):
        global offsetx, offsety
        self.rect.topleft = (self.mapx-13+offsetx, self.mapy-13+offsety)
        self.cd -= 1
        if -50 <= player.mapx - self.mapx <= 20 and -50 <= player.mapy - self.mapy <= 20:
            self.open = True
            description.change_text("Reroll", "Self explanatory")
            if keys[pygame.K_f] and self.cd <= 0:
                choice1.gambled = False
                choice2.gambled = False
                choice3.gambled = False
                self.cd = 30
        else:
            self.open = False

class ThingList(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = images.thinglist
        self.image.set_alpha(150)
        self.on = True
        self.row = 0
        self.mkd = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 10)

    def update(self, keys):
        active_things.sort()
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 10)
        if self.on == True:
            self.image.set_alpha(150)
            self.addeverything()
        else:
            self.image.set_alpha(0)
        if keys[pygame.K_m] and self.mkd <= 0:
            if self.on == False:
                self.addeverything()
                self.mkd = 10
                self.on = True
            else:
                thing_sprs.empty()
                self.on = False
                self.mkd = 10
        self.mkd -= 1

    def addeverything(self):
        global thing_sprs
        thing_sprs.empty()
        unique_counts = {}
        for item in active_things:
            unique_counts[item] = unique_counts.get(item, 0) + 1
        sorted_unique_items = sorted(list(unique_counts.keys()))
        items_per_row = 12
        spacing_x = 45
        spacing_y = 45
        start_x = self.rect.x + 25  
        start_y = self.rect.y + 20  
        for i, item_key in enumerate(sorted_unique_items):
            row_idx = i // items_per_row
            col_idx = i % items_per_row
            calc_x = start_x + (col_idx * spacing_x)
            calc_y = start_y + (row_idx * spacing_y)
            thing_sprs.add(Thing(item_key, calc_x, calc_y, unique_counts[item_key]))

class Thing(pygame.sprite.Sprite):
    def __init__(self, thing, x, y, count):
        super().__init__()
        self.thing = thing
        self.x = x
        self.y = y
        self.image = images.empty
        self.count = count
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.update()

    def update(self):
        match self.thing:
            case "0Paycheck":
                self.image = images.choiceupgrades["paycheck"]
            case "4Leafery":
                self.image = images.choiceenemies["leafery"]
            case "4SmallChange":
                self.image = images.choiceenemies["smallchangebelly"]
            case _:
                self.image = images.empty
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        
        

player = Player()
intermission = Intermission()
jumpui = JumpUI()
choice1 = Choice1()
choice2 = Choice2()
choice3 = Choice3()
reroll = Reroll()
description = Description("Woah", "Ja-placeholder!")
thinglist = ThingList()
thing = Thing(None, 0, 0, 1)

map_sprs = pygame.sprite.Group()
intermission_spr = pygame.sprite.Group(intermission)
player_sprite = pygame.sprite.Group(player)
ui_sprites = pygame.sprite.Group(jumpui)
description_sprite = pygame.sprite.Group(description)
choice_sprites = pygame.sprite.Group(choice1, choice2, choice3)
reroll_spr = pygame.sprite.Group(reroll)
thinglist_spr = pygame.sprite.Group(thinglist)
thing_sprs = pygame.sprite.Group()
