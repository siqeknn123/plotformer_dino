import pygame
from objects import *
from levels import *

pygame.init()

level1_objects, key, chest = draw_level(level1)

player = Player(50, 600, 40, 50, 20, player_images)
level1_objects.add(player)

game = True
while game:
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    window.blit(bg, (0, 0))

    for obj in level1_objects:
        window.blit(obj.image, camera.apply(obj))
    camera.update(player)

    player.update(platforms)

    if pygame.sprite.spritecollide(player, coins, True):
        coins_count += 1

    window.blit(pygame.transform.scale(coin_img, (40, 40)), (15, 15))
    coins_count_txt = font1.render(f':{coins_count}', True, (255, 255, 255))
    window.blit(coins_count_txt, (60, 15))

    if pygame.sprite.collide_rect(player, key):
        window.blit(get_key_txt, (500, 15))
        if keys_pressed[pygame.K_f]:
            is_key = True
            key.rect.x = -300
    if pygame.sprite.collide_rect(player, chest) and not is_key:
        window.blit(find_key_txt, (480, 15))
    if pygame.sprite.collide_rect(player, chest) and is_key:
        window.blit(open_chest_txt,(480, 15))
        if keys_pressed[pygame.K_f]:
            is_key = False
            coins_count += 20
            chest.rect.x = -301

    pygame.display.update()
    clock.tick(FPS)



