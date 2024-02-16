import pygame
pygame.init()
screen_width = 800
screen_height = 600
white = (255, 255, 255)
screen = pygame.display.set_mode((screen_width, screen_height))
run= True
player= pygame.image.load('player.png')
player= pygame.transform.smoothscale(player, (150, 150))
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(white)
    screen.blit(player, (500,300))
    pygame.display.update()
pygame.quit()
