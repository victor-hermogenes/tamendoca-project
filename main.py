import pygame,sys

class Amendoca(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
WIDTH, HEIGHT = 400, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tamendoca")

# Sprites and groups
moving_sprites = pygame.sprite.Group()
amendoca = Amendoca(100, 100)
moving_sprites.add (amendoca)

FPS = 60

def main():
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit


