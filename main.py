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
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tamendoca")

# Sprites and groups
moving_sprites = pygame.sprite.Group()
amendoca = Amendoca(100, 100)
moving_sprites.add (amendoca)

FPS = 60

def main():
    """This ensure the game runs and closes"""
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit

        """This make the drawings appears"""
        WINDOW.fill((0, 0, 0))
        moving_sprites.draw(WINDOW)
        pygame.display.flip()

if __name__ == "__main__":
    main()