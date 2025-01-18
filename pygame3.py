import pygame


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)


player = pygame.Rect(300, 250, 50, 50)
enemy = pygame.Rect(500, 200, 50, 50)  


player_speed = 5


running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed


    player.x = max(0, min(player.x, screen_width - player.width))
    player.y = max(0, min(player.y, screen_height - player.height))


    screen.fill(white)


    pygame.draw.rect(screen, red, player)
    pygame.draw.rect(screen, blue, enemy)


    pygame.display.flip()


pygame.quit()