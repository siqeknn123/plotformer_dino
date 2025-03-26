from settings import *


class MapObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, heigth, image):
        super().__init__()
        self.width = width
        self.heigth = heigth
        self.image = pygame.transform.scale(image, (width, heigth))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, images):
        super().__init__()
        self.width = width
        self.height = height
        self.images = images
        self.anim_count = 0
        self.image = pygame.transform.scale(self.images[self.anim_count], (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, x, y, width, height, speed, images):
        super().__init__(x, y, width, height, speed, images)
        self.action = "idle"
        self.animations = {
            "idle": list(range(4)),
            "right": list(range(4, 10)),
            "left": list(range(10, 17))
        }
        self.is_jump = False
        self.jump_count = 28
        self.fall = 0
        self.gravity = 2.2
        self.on_ground = False

    def update(self, platforms):
        frames = self.animations[self.action]
        self.anim_count += 1
        if self.anim_count >= len(frames) - 1:
            self.anim_count = 0
        self.image = pygame.transform.scale(self.images[frames[self.anim_count]], (self.width, self.height))

        self.fall += self.gravity
        self.rect.y += self.fall
        hit_platforms = pygame.sprite.spritecollide(self, platforms, False)
        if hit_platforms:
            for platform in hit_platforms:
                if self.fall > 0 and self.rect.bottom > platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.fall = 0
                    self.on_ground = True
        else:
            self.on_ground = False

        keys_pressed = pygame.key.get_pressed()        
        if keys_pressed[pygame.K_a]:
            self.action = "left"
            self.rect.x -= self.speed
        elif keys_pressed[pygame.K_d]:
            self.action = "right"
            self.rect.x += self.speed
        else:
            self.action = "idle"
        
        if not self.is_jump:
            if keys_pressed[pygame.K_SPACE]:
                if self.on_ground:
                    self.is_jump = True
                    self.fall -= self.jump_count
        else:
            self.is_jump = not self.on_ground

            
        

        
