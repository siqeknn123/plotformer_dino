import pygame

pygame.init()

W, H = 1280, 700
FPS = 20

coins_count = 0
is_key = False


window = pygame.display.set_mode((W, H))
pygame.display.set_caption('Platformer dino')
pygame.display.set_icon(pygame.image.load('assets/images/player/stand_1.png'))
clock = pygame.time.Clock()

platforms = pygame.sprite.Group()

coins = pygame.sprite.Group()

bg = pygame.transform.scale(pygame.image.load('assets/background/level1.png'), (W, H))

platform_image = pygame.image.load('assets/background/platform.png')

player_images = [
    pygame.image.load("assets/images/player/stand_1.png"),
    pygame.image.load("assets/images/player/stand_2.png"),
    pygame.image.load("assets/images/player/stand_3.png"),
    pygame.image.load("assets/images/player/stand_4.png"),
    pygame.image.load("assets/images/player/move_right_1.png"),
    pygame.image.load("assets/images/player/move_right_2.png"),
    pygame.image.load("assets/images/player/move_right_3.png"),
    pygame.image.load("assets/images/player/move_right_4.png"),
    pygame.image.load("assets/images/player/move_right_5.png"),
    pygame.image.load("assets/images/player/move_right_6.png"),
    pygame.image.load("assets/images/player/move_left_1.png"),
    pygame.image.load("assets/images/player/move_left_2.png"),
    pygame.image.load("assets/images/player/move_left_3.png"),
    pygame.image.load("assets/images/player/move_left_4.png"),
    pygame.image.load("assets/images/player/move_left_5.png"),
    pygame.image.load("assets/images/player/move_left_6.png")
]

coin_img = pygame.image.load("assets/images/coin/coin.png")
key_img = pygame.image.load("assets/images/key/key.png")
chest_img = pygame.image.load("assets/images/chest/chest.png")
portal_img = pygame.image.load("assets/images/portal/portal.png")

'''ШРИФТИ'''
pygame.font.init()
font1 = pygame.font.Font(None, 60)
'''ТЕКСТИ'''
find_key_txt = font1.render("Знайди ключ!", True, (255, 255, 255))
open_chest_txt = font1.render("Натисни F щоб відкрити!", True, (255, 255, 255))
get_key_txt = font1.render("Натисни F щоб підібрати ключ!", True, (255, 255, 255))




