import pygame,sys

class Amendoca_Idle(pygame.sprite.Sprite):
    pass


class Amendoca_Bath(pygame.sprite.Sprite):
    pass


class Amendoca_Sleep(pygame.sprite.Sprite):
    pass


class Amendoca_Hunt(pygame.sprite.Sprite):
    pass


class Amendoca_Run(pygame.sprite.Sprite):
    pass


class Amendoca_Playful(pygame.sprite.Sprite):
    pass


class Amendoca_Nervous(pygame.sprite.Sprite):
    pass

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tamendoca")

# Sprites and groups
moving_sprites = pygame.sprite.Group()

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