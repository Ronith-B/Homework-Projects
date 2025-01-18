import pygame


pygame.init()


screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game Screen")


background_color = (58, 58, 58)
screen.fill(background_color)


image = pygame.image.load("your_image.png")  
image_width, image_height = image.get_size()
image_x = (screen_width - image_width) // 2
image_y = (screen_height - image_height) // 2
screen.blit(image, (image_x, image_y))


pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()