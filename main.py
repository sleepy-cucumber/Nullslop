import sys
import pygame
from classes import *
from variables import *
import images

bg_color = (50, 0, 120)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nullslop")
pygame.display.set_icon(images.icon)
clock = pygame.time.Clock()


status = 0  # 0 - start, 1 - intermission, 2 - level
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    player.handle_input(keys)
    status = player.status

    if status == 0 or status == 1:
        floor_collision = pygame.sprite.spritecollide(player, intermission_spr, False, pygame.sprite.collide_mask)
    elif status == 2:
        floor_collision = pygame.sprite.spritecollide(player, map_sprs, False, pygame.sprite.collide_mask)
    else:
        running = False

    if not floor_collision:
        player.height -= 2
    else:
        if 80 <= player.height <= 104:
            player.height = 100
            player.jumps = player.max_jumps
            player.platform = player.max_platform
        else:
            player.height -= 2
    screen.fill(bg_color)
    text_jumps = ui_font.render("x" + str(jumpui.amount), False, (255,255,255))
    text_height = ui_font.render("h:"+str(player.height), False, (255,255,255))
    text_stamina = ui_font.render("stm:"+str(player.stamina)+"/"+str(player.max_stamina), False, (255,255,255))
    text_platform = ui_font.render("ptf:"+str(player.platform)+"/"+str(player.max_platform), False, (255,255,255))
    text_abilitycd = ui_font.render("cd:"+str(player.ability_cd), False, (255,255,255))
    text_gifts = gih_count_font.render(str(player.gifts_collected)+"/"+str(player.total_gifts), False, (255,255,255))
    if choice1.open or choice2.open or choice3.open or reroll.open:
        text_name = gih_count_font.render(description.name, True, (255,255,255))
        text_desc = ui_font.render(description.description, True, (255,255,255))
    else:
        text_name = gih_count_font.render(" error", True, (255,255,255))
        text_desc = ui_font.render(" okay", True, (255,255,255))
    if status == 0:
        intermission_spr.draw(screen)
        intermission_spr.update()
        player_sprite.draw(screen)
        player_sprite.update()
        ui_sprites.draw(screen)
        ui_sprites.update()
        choice_sprites.draw(screen)
        choice1.update(keys)
        choice2.update(keys)
        choice3.update(keys)
        screen.blit(text_jumps, (jumpui.x, jumpui.y + 32))
        screen.blit(text_height, (WIDTH//2, HEIGHT//2+25))
        screen.blit(text_stamina, (WIDTH//2, HEIGHT//2-16))
        screen.blit(text_platform, (WIDTH//2, HEIGHT//2-33))
        if choice1.open or choice2.open or choice3.open:
            description_sprite.draw(screen)
            description_sprite.update()
            screen.blit(text_name, (10, HEIGHT-90))
            screen.blit(text_desc, (10, HEIGHT-60))
        thinglist_spr.draw(screen)
        thinglist_spr.update(keys)
        thing_sprs.draw(screen)
        thing_sprs.update()
        for spr in thing_sprs.sprites():
            if spr.count > 1 and spr.image != images.empty:
                count_text = ui_font.render(f"{spr.count}", True, (255, 255, 255))
                text_x = spr.rect.right - count_text.get_width()
                text_y = spr.rect.bottom - count_text.get_height() + 3 
                screen.blit(count_text, (text_x, text_y))
        if player.ability_cd > 0:
            screen.blit(text_abilitycd, (WIDTH//2+25, HEIGHT//2))
    if status == 1:
        intermission_spr.draw(screen)
        intermission_spr.update()
        player_sprite.draw(screen)
        player_sprite.update()
        ui_sprites.draw(screen)
        ui_sprites.update()
        choice_sprites.draw(screen)
        choice1.update(keys)
        choice2.update(keys)
        choice3.update(keys)
        reroll_spr.draw(screen)
        reroll_spr.update(keys)
        screen.blit(text_jumps, (jumpui.x, jumpui.y + 32))
        screen.blit(text_height, (WIDTH//2, HEIGHT//2+25))
        screen.blit(text_stamina, (WIDTH//2, HEIGHT//2-16))
        screen.blit(text_platform, (WIDTH//2, HEIGHT//2-33))
        if choice1.open or choice2.open or choice3.open or reroll.open:
            description_sprite.draw(screen)
            description_sprite.update()
            screen.blit(text_name, (10, HEIGHT-90))
            screen.blit(text_desc, (10, HEIGHT-60))
        thinglist_spr.draw(screen)
        thinglist_spr.update(keys)
        thing_sprs.draw(screen)
        thing_sprs.update()
        for spr in thing_sprs.sprites():
            if spr.count > 1 and spr.image != images.empty:
                count_text = ui_font.render(f"{spr.count}", True, (255, 255, 255))
                text_x = spr.rect.right - count_text.get_width() + 10
                text_y = spr.rect.bottom - count_text.get_height() + 10
                screen.blit(count_text, (text_x, text_y))
        if player.ability_cd > 0:
            screen.blit(text_abilitycd, (WIDTH//2+25, HEIGHT//2))
    if status == 2:
        for tile in map_sprs:
            if -250 <= tile.rect.x <= WIDTH + 250 and -250 <= tile.rect.y <= HEIGHT + 250:
                screen.blit(tile.image, tile.rect)
        map_sprs.update()
        for gift in gift_sprs:
            if -50 <= gift.rect.x <= WIDTH + 50 and -50 <= gift.rect.y <= HEIGHT + 50:
                screen.blit(gift.image, gift.rect)
        gift_sprs.update()
        player_sprite.draw(screen)
        player_sprite.update()
        ui_sprites.draw(screen)
        ui_sprites.update()
        screen.blit(text_jumps, (jumpui.x, jumpui.y + 32))
        screen.blit(text_height, (WIDTH//2, HEIGHT//2+25))
        screen.blit(text_stamina, (WIDTH//2, HEIGHT//2-16))
        screen.blit(text_platform, (WIDTH//2, HEIGHT//2-33))
        screen.blit(text_gifts, (WIDTH//2 - 50, HEIGHT - 30))
        thinglist_spr.draw(screen)
        thinglist_spr.update(keys)
        thing_sprs.draw(screen)
        thing_sprs.update()
        for spr in thing_sprs.sprites():
            if spr.count > 1 and spr.image != images.empty:
                count_text = ui_font.render(f"{spr.count}", True, (255, 255, 255))
                text_x = spr.rect.right - count_text.get_width() + 10
                text_y = spr.rect.bottom - count_text.get_height() + 10
                screen.blit(count_text, (text_x, text_y))
        if player.ability_cd > 0:
            screen.blit(text_abilitycd, (WIDTH//2+25, HEIGHT//2))
        
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()