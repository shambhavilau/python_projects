import random
import sys  # use sys.exit to exit the program
import pygame
from pygame.locals import *

# Global Variables
FPS = 32
SCREEN_WIDTH = 350   # 289 , 511
SCREEN_HEIGHT = 511
# creating a display surface for the game
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GROUND_Y = SCREEN_HEIGHT * 0.92
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/unicorn2.1.png'
BACKGROUND = 'gallery/sprites/bg.png'
BARRIER = 'gallery/sprites/pipe.png'



def welcome_screen():
    """ Shows some images on screen """
    player_x = int(SCREEN_WIDTH/5)
    player_y = int((SCREEN_HEIGHT - GAME_SPRITES['player'].get_height())/2)
    message_x = int((SCREEN_WIDTH - GAME_SPRITES['message'].get_width())/2)
    message_y = int(SCREEN_HEIGHT * 0.13)
    base_x = 0

    while True:
        counter = 3
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                counter -= 1
                if counter > 0:
                    GAME_SOUNDS['countdown'].play()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (player_x, player_y))
                # SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'], (base_x, GROUND_Y))
                pygame.display.update()
                FPS_CLOCK.tick(FPS)


def main_game():
    score = 0
    player_x = int(SCREEN_WIDTH/5)
    player_y = int(SCREEN_WIDTH/2)
    base_x = 0
    # Create 2 pipes for blitting on screen
    newBarrier1 = getRandomBarrier()
    newBarrier2 = getRandomBarrier()

    # list for upper and lower barriers
    upper_barriers = [
        {'x': SCREEN_WIDTH + 200, 'y': newBarrier1[0]['y']},
        {'x': SCREEN_WIDTH + 200 + (SCREEN_WIDTH/2), 'y': newBarrier2[0]['y']},
    ]
    lower_barriers = [
        {'x': SCREEN_WIDTH + 200, 'y': newBarrier1[1]['y']},
        {'x': SCREEN_WIDTH + 200 + (SCREEN_WIDTH / 2), 'y': newBarrier2[1]['y']},
    ]
    barrier_velocity_x = -4  # vel with which barrier will move
    player_velocity_y = -9
    player_max_velocity_y = 10
    player_min_velocity_y = -8
    player_acceleration_y = 1

    player_fly_velocity = -8  # velocity while flying
    player_fly = False  # it is true only when unicorn is flying

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if player_y > 0:
                    player_velocity_y = player_fly_velocity
                    player_fly = True
                    GAME_SOUNDS['fly'].play()

        crash_test = is_collide(player_x, player_y, upper_barriers, lower_barriers)  # returns true if player crashes
        if crash_test:
            return

        # check for score
        player_mid_pos = player_x + GAME_SPRITES['player'].get_width()/2
        for b in upper_barriers:
            barrier_mid_pos = b['x'] + GAME_SPRITES['barrier'][0].get_width()/2
            if barrier_mid_pos <= player_mid_pos < barrier_mid_pos + 4:
                score += 1
                print("Score ", score)
                GAME_SOUNDS['point'].play()

        if player_velocity_y < player_max_velocity_y and not player_fly:
            player_velocity_y += player_acceleration_y

        if player_fly:
            player_fly = False
        player_height = GAME_SPRITES['player'].get_height()
        player_y = player_y + min(player_velocity_y, GROUND_Y - player_y - player_height)

        # move barriers to the left
        for upper_barrier, lower_barrier in zip(upper_barriers, lower_barriers):
            upper_barrier['x'] += barrier_velocity_x
            lower_barrier['x'] += barrier_velocity_x

        # add a new pipe when the first pipe is about to cross left part of screen
        if 0 < upper_barriers[0]['x'] < 5:
            new_barrier = getRandomBarrier()
            upper_barriers.append(new_barrier[0])
            lower_barriers.append(new_barrier[1])

        # remove barrier if it goes out of screen
        if upper_barriers[0]['x'] < -GAME_SPRITES['barrier'][0].get_width():
            upper_barriers.pop(0)
            lower_barriers.pop(0)

        # blit sprites on screen
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upper_barrier, lower_barrier in zip(upper_barriers, lower_barriers):
            SCREEN.blit(GAME_SPRITES['barrier'][0], (upper_barrier['x'], upper_barrier['y']))
            SCREEN.blit(GAME_SPRITES['barrier'][1], (lower_barrier['x'], lower_barrier['y']))

        SCREEN.blit(GAME_SPRITES['base'], (base_x, GROUND_Y))
        SCREEN.blit(GAME_SPRITES['player'], (player_x, player_y))
        my_digits = [int(x) for x in list(str(score))]
        width = 0
        for digit in my_digits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        x_offset = (SCREEN_WIDTH - width)/2

        for digit in my_digits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (x_offset, SCREEN_HEIGHT * 0.12))
            x_offset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def is_collide(player_x, player_y, upper_barriers, lower_barriers):
    if player_y > GROUND_Y - 60 or player_y < 0:
        GAME_SOUNDS['hit'].play()
        return True
    # check for collision with upper or lower barriers
    for b in upper_barriers:
        barrier_height = GAME_SPRITES['barrier'][0].get_height()
        if player_y < barrier_height + b['y'] and abs(player_x - b['x']) < GAME_SPRITES['barrier'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    for b in lower_barriers:
        player_height = GAME_SPRITES['player'].get_height()
        if player_y + player_height > b['y'] and abs(player_x - b['x']) < GAME_SPRITES['barrier'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    return False


def getRandomBarrier():
    """ Generate positions of two barrier (straight and inverted) """
    barrier_height = GAME_SPRITES['barrier'][0].get_height()
    offset = SCREEN_HEIGHT / 3
    y2 = offset + random.randrange(0, int(SCREEN_HEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset))
    barrier_x = SCREEN_WIDTH + 10
    y1 = barrier_height - y2 + offset
    barrier = [
        {'x': barrier_x, 'y': -y1},  # for upper barrier
        {'x': barrier_x, 'y': y2}    # for lower barrier
    ]
    return barrier


if __name__ == '__main__':
    # game starts here
    # initialize all pygame modules
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    pygame.display.set_caption('Heads Up Unicorn 🦄')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha()
        # .convert_alpha() used for displaying image faster in the game window
    )

    GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base1.1.png').convert_alpha()
    GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['barrier'] = (pygame.transform.rotate(pygame.image.load(BARRIER).convert_alpha(), 180),
                               pygame.image.load(BARRIER).convert_alpha())

    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/score.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['fly'] = pygame.mixer.Sound('gallery/audio/wing.wav')
    GAME_SOUNDS['countdown'] = pygame.mixer.Sound('gallery/audio/countdown.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcome_screen()
        main_game()
