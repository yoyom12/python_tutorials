import pygame
x = pygame.init()

# creating Windows
gameWindow = pygame.display.set_mode((1200,600))
pygame.display.set_caption("my first gam")

# game specific variabl
quit_game = False
game_ovr = False

clock = pygame.time.Clock()


# creating a game loop
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("you prss right ky")
            if event.key == pygame.K_LEFT:
                print("you prss lft ky")
            if event.key == pygame.K_UP:
                print("you prss up ky")

                clock.tick(60)

pygame.quit()
quit()


