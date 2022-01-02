import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Fucking Game")

LIGHT_BLUE = 204, 255, 255
BLACK = 0, 0, 0
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 3, HEIGHT)
FPS = 60
VEL = 5
BULLETS_VEL = 7
MAX_BULLETS = 5 
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 60, 50

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(yellow, red): # display
    WIN.fill(LIGHT_BLUE) # base screen color
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) # draw surface 
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_key_binds(keys_pressed, yellow): # yellow key binds
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x + 10: # right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 10: # down
        yellow.y += VEL

def red_key_binds(keys_pressed, red): # red key binds
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: # down
        red.y += VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red): # bullets control
    for bullets in yellow_bullets:
        bullets.x += BULLETS_VEL
        if yellow.colliderect(bullets):
            yellow_bullets.remove(bullets)
            
def main():
    # position of spaceships
    yellow = pygame.Rect(100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(750, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    yellow_bullets = []
    red_bullets = []

    # game running
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    # bullets 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullets = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 - 2, 10, 5) 
                    yellow_bullets.append(bullets)
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullets = pygame.Rect(red.x, red.y + red.height/2 - 2, 10, 5)
                    red_bullets.append(bullets)

        keys_pressed = pygame.key.get_pressed()
        yellow_key_binds(keys_pressed, yellow)
        red_key_binds(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(yellow, red)

    pygame.quit()

if __name__ == "__main__":
    main()



