'''
Attempting to create a game using pygame. As of 6/30/2023, the leading idea for the game is to
recreate something similar to Galaga/Space Invaders. If that gets boring/hard/or something else, maybe a platformer.
God Speed

Additionally, code will probably be heavily commented to encourage understanding
'''

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True  # Initializing pygame packages, setting screen size/resolution, creating game clock
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)  # Player's position starts as mid of screen

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Only quits if X is hit in corner
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)  # Set circle to screen, choose color, then size

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # "K_w" is "pressing the w key"
        if player_pos.y >= 100:  # Creating a top bound that circle can't cross, values are reversed?
            player_pos.y -= 300 * dt  # dt is the duration (somehow). The longer its held, more the position changes
        else:
            continue  # If bound is reached, it does not allow player to move y-coordinate up anymore
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()  # I don't understand why you have to flip the screen??

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000  # limits framerate somehow

pygame.quit()