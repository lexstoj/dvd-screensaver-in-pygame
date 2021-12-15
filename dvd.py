import pygame
import random

pygame.init()

width = 1000

length = 750
x = random.randrange(0, 1000)
y = random.randrange(0, 750)
vx, vy = 3, 2
title = "dvd screensaver lul"
window = pygame.display.set_mode([width, length])
pygame.display.set_caption(title)

clock = pygame.time.Clock()
refresh_rate = 75

black = (0, 0, 0)

logo = pygame.image.load('men.png').convert_alpha()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    x += vx
    y += vy

    if x <= 0 or x >= 925:
        vx *= -1
    if y <= 0 or y >= 675:
        vy *= -1 
            

    window.fill(black)
    window.blit(logo, [x,y])

    pygame.display.flip()
    clock.tick(refresh_rate)

pygame.quit()
