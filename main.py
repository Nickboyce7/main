'''
Attempting to create a game using pygame. As of 6/30/2023, the leading idea for the game is to
recreate something similar to Galaga/Space Invaders. If that gets boring/hard/or something else, maybe a platformer.
God Speed

Additionally, code will probably be heavily commented to encourage understanding

DRAWING RECTANGLES: the rect argument is as such
[pixels from left side of screen, pixels from top side of screen, length of rect, height of rect]
'''

import pygame
import math as m

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True  # Initializing pygame packages, setting screen size/resolution, creating game clock
dt = 0


class Player:
    def __init__(self, x_coord, y_coord, width, height):
        self.rectangle = pygame.Rect(x_coord, y_coord, width, height)


class Enemy:
    def __init__(self, x_coord, y_coord, width, height):
        self.rectangle = pygame.Rect(x_coord, y_coord, width, height)


USER_START = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
user = Player(700, 350, 15, 15)
enemy1 = Enemy(300, 300, 30, 30)


# Creating a check border function to determine if player is in bounds of screen
def check_border(pos_x, pos_y, screen_x, screen_y):
    # For rectangles, it follows the top left corner. When moved to bottom right, rectangle disappears
    if (0 < pos_x < screen_x) and (0 < pos_y < screen_y):
        pass
    elif pos_x < 0:
        pos_x = 1
    elif pos_x > screen_x:
        pos_x = screen_x - 1
    elif pos_y < 0:
        pos_y = 1
    elif pos_y > screen_y:
        pos_y = screen_y - 1
    return pos_x, pos_y


def circle_movement(center, radius, speed, object, time):
    object.x = radius * m.cos((speed * time / 1000) % (2 * m.pi)) + center[0]
    object.y = radius * m.sin((speed * time / 1000) % (2 * m.pi)) + center[1]
    return object.x, object.y


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Only quits if X is hit in corner
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, "red", user.rectangle)

    pygame.draw.rect(screen, "blue", enemy1.rectangle)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # "K_w" is "pressing the w key"
        user.rectangle.y -= 300 * dt

    if keys[pygame.K_s]:
        user.rectangle.y += 300 * dt

    if keys[pygame.K_a]:
        user.rectangle.x -= 300 * dt

    if keys[pygame.K_d]:
        user.rectangle.x += 300 * dt

    user.rectangle.x, user.rectangle.y = check_border(user.rectangle.x, user.rectangle.y, screen_width, screen_height)
    if pygame.Rect.colliderect(user.rectangle, enemy1.rectangle):
        user.rectangle.x = 600
        user.rectangle.y = 350

    enemy1.rectangle.x, enemy1.rectangle.y = circle_movement((400,400), 100, 2, enemy1.rectangle, pygame.time.get_ticks())
  #  print(pygame.time.get_ticks())

    pygame.display.flip()  # I don't understand why you have to flip the screen??

    dt = clock.tick(60) / 1000  # limits framerate somehow

pygame.quit()
