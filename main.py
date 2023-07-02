'''
Attempting to create a game using pygame. As of 6/30/2023, the leading idea for the game is to
recreate something similar to Galaga/Space Invaders. If that gets boring/hard/or something else, maybe a platformer.
God Speed

Additionally, code will probably be heavily commented to encourage understanding
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
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def get_position(self):
        return self.position

    def get_size(self):
        return self.size


class Enemy:
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def get_position(self):
        return self.position

    def get_size(self):
        return self.size


USER_START = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
user = Player(USER_START, 20)
enemy1 = Enemy((300, 300), 15)


# Creating a check border function to determine if player is in bounds of screen
def check_border(pos_x, pos_y, screen_x, screen_y):
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


def check_collision(object_one, object_two):

    res = tuple(map(lambda i, j: i - j, object_two.get_position(), object_one.get_position()))

    if m.sqrt(res[0]**2 + res[1]**2) < (object_one.get_size() + object_two.get_size()):
        print("hit")
        object_one.position = pygame.Vector2(600, 300)
    else:
        pass

    return object_one.position, object_two.position


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Only quits if X is hit in corner
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #  pygame.draw.circle(screen, "red", player_pos, 20)  # Set circle to screen, choose color, then size
    pygame.draw.circle(screen, "red", user.position, user.size)

    pygame.draw.circle(screen, "blue", enemy1.position, enemy1.size)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # "K_w" is "pressing the w key"
        user.position.y -= 300 * dt  # dt is the duration (somehow). The longer its held, more the position changes

    if keys[pygame.K_s]:
        user.position.y += 300 * dt

    if keys[pygame.K_a]:
        user.position.x -= 300 * dt

    if keys[pygame.K_d]:
        user.position.x += 300 * dt

    user.position.x, user.position.y = check_border(user.position.x, user.position.y, screen_width, screen_height)
    user.position, enemy1.position = check_collision(user, enemy1)
    # print(player_pos.x, player_pos.y)

    # flip() the display to put your work on screen
    pygame.display.flip()  # I don't understand why you have to flip the screen??

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000  # limits framerate somehow

pygame.quit()