#nithash rajendram
import os
import random
import pygame

WIDTH, HEIGHT = 600, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
#BORDER = pygame.Rect(0, 0,600, 600)
pygame.display.set_caption("Snake Game")
FPS = 60
VELOCITY = 5

BACK_GROUND = pygame.image.load(os.path.join('Assets', 'background.jpg'))
PLAYER_Image = pygame.image.load(os.path.join('Assets', 'jet.png'))
PLAYER = pygame.transform.scale(PLAYER_Image, (60,60))


def draw_window(playerbox):
    WINDOW.fill((133, 128, 127))
    WINDOW.blit(BACK_GROUND, (0, 0))
    #pygame.draw.rect(WINDOW,(0,0,0), BORDER)
    WINDOW.blit(PLAYER, (playerbox.x, playerbox.y))
    pygame.display.update()

def player_movement(keys_pressed, playerbox):
    if keys_pressed[pygame.K_LEFT] and playerbox.x >=0:  # left
        playerbox.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT]and playerbox.x <=540:  # right
        playerbox.x += VELOCITY
    if keys_pressed[pygame.K_UP] and playerbox.y >=5:  # up
        playerbox.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and playerbox.y <= 325:  # down
        playerbox.y += VELOCITY

def main():

    playerbox = pygame.Rect(100, 200, 60, 60)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, playerbox)
        draw_window(playerbox)

    pygame.quit()

if __name__ == "__main__":
    main()
