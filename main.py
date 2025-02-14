import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('FPGame')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/background.jpg')

walk_right = [
    pygame.image.load('images/w_right/r1.png'),
    pygame.image.load('images/w_right/r2.png'),
    pygame.image.load('images/w_right/r3.png'),
    pygame.image.load('images/w_right/r4.png'),
    pygame.image.load('images/w_right/r5.png'),
    pygame.image.load('images/w_right/r6.png'),
    pygame.image.load('images/w_right/r7.png')
]
walk_left = [
    pygame.image.load('images/w_left/l1.png'),
    pygame.image.load('images/w_left/l2.png'),
    pygame.image.load('images/w_left/l3.png'),
    pygame.image.load('images/w_left/l5.png'),
    pygame.image.load('images/w_left/l6.png'),
    pygame.image.load('images/w_left/l7.png')
]

wolf_anim_count = 0
bg_x = 0

running = True
while running:
    clock.tick(10)
    screen.blit(bg, (bg_x,0))
    screen.blit(bg, (bg_x + 900, 0))
    screen.blit(walk_right[wolf_anim_count], (300, 325))

    if wolf_anim_count == 6:
        wolf_anim_count = 0
    else:
        wolf_anim_count += 1

    bg_x -= 2
    if bg_x == - 900:
        bg_x == 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

