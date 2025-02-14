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
    pygame.image.load('images/w_left/l4.png'),
    pygame.image.load('images/w_left/l5.png'),
    pygame.image.load('images/w_left/l6.png'),
    pygame.image.load('images/w_left/l7.png')

]
wolf_anim_count = 0
bg_x = 0

wolf_speed = 5
wolf_x = 100
wolf_y = 326

is_jump = False
jump_count = 7

running = True
while running:
    clock.tick(15)
    screen.blit(bg, (bg_x,0))
    #screen.blit(bg, (bg_x + 900, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        screen.blit(walk_left[wolf_anim_count], (wolf_x, wolf_y))
    else:
        screen.blit(walk_right[wolf_anim_count], (wolf_x, wolf_y))

    if keys[pygame.K_a] and wolf_x > 10:
        wolf_x -= wolf_speed
    elif keys[pygame.K_d] and wolf_x < 700:
        wolf_x += wolf_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                wolf_y -= (jump_count ** 2) / 2
            else:
                wolf_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7

    if wolf_anim_count == 6:
        wolf_anim_count = 0
    else:
        wolf_anim_count += 1

    #bg_x -= 2
    #if bg_x == - 900:
        #bg_x == 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

