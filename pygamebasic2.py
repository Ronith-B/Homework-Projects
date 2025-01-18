import pygame


pygame.init()


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game Screen")

screen.fill((255, 255, 255))  


rectangle_color = (255, 0, 0)  
rectangle_width = 100
rectangle_height = 50
rectangle_x = (screen_width - rectangle_width) // 2
rectangle_y = (screen_height - rectangle_height) // 2
pygame.draw.rect(screen, rectangle_color, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))


font = pygame.font.Font(None, 36)
text = font.render("Hello, World!", True, (0, 0, 0))  
text_rect = text.get_rect()
text_rect.center = (screen_width // 2, screen_height // 2 + 50)
screen.blit(text, text_rect)


pygame.display.flip()



pygame.quit()