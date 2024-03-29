import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KENDO")

WHITE = (255, 255, 255)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90) # resize and rotate the img

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP =  pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)   


def draw_window(red, yellow):
    WIN.fill(WHITE) # for white screen
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) # for yellow image to appear on top of white bg
    WIN.blit(RED_SPACESHIP,(red.x, red.y))
    pygame.display.update()


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:             
                run = False

        keys_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a]: # LEFT
            yellow.x -=VEL
        if key_pressed[pygame.K_d]: # RIGHT
            yellow.x +=VEL    
        if key_pressed[pygame.K_w]: # UP
            yellow.y -=VEL
        if key_pressed[pygame.K_s]: # DOWN
            red.y +=VEL
        if key_pressed[pygame.K_LEFT]: #LEFT
            red.x -=VEL
        if key_pressed[pygame.K_RIGHT]: # RIGHT
            red.x +=VEL    
        if key_pressed[pygame.K_UP]: # UP
            red.y -=VEL
        if key_pressed[pygame.K_DOWN]: # DOWN
            red.y +=VEL  

        draw_window(red, yellow)        
        
    pygame.quit()


