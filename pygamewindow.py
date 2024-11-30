import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500,500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game Screen")

background_image = pygame.transform.scale(
    pygame.image.load("background.jpg").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

image_rand = pygame.transform.scale(
    pygame.image.load("penguin.jpeg").convert_alpha(),(200,200))
image_rect = image_rand.get_rect(center=(SCREEN_WIDTH //2, SCREEN_HEIGHT //2 -30))