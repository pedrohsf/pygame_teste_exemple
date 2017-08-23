#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()

font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)
pontuacao_font = pygame.font.SysFont(font_name,25)
pontos = 0



pygame.mixer.pre_init(44100,32,2,4096)

explosion_sound = pygame.mixer.Sound('images/boom.wav')
explosion_player = False

screen = pygame.display.set_mode((956, 560), 0, 32)


background = pygame.image.load('images/bg_big.png').convert()


ship = {
    'surface' : pygame.image.load('images/ship.png').convert_alpha(),
    'position' : [randrange(956), randrange(560)],
    'speed' : {
        'x' : 0,
        'y' : 0
    }
}

exploded_ship = {
    'surface' : pygame.image.load('images/ship_exploded.png').convert_alpha(),
    'position' : [],
    'speed' : {
        'x' : 0,
        'y' : 0
    },
    'rect' : Rect(0,0,48,48)
}

collision_animation_counter = 0

pygame.display.set_caption('Asteroids')
clock = pygame.time.Clock()

def remove_used_asteroids():
    for asteroid in asteroids:
        if asteroid['position'][1] > 560:
            asteroids.remove(asteroid)

def create_asteroid():
    return{
        'surface' : pygame.image.load('images/asteroid.png').convert_alpha(),
        'position' : [randrange(892), -64],
        'speed' : randrange(10)
    }

def move_asteroids():
    for asteroid in asteroids:
        asteroid['position'][1] += asteroid['speed']

ticks_to_asteroid = 90
ticks_to_points = 30
asteroids = []

def get_rect(obj):
    return Rect(obj['position'][0],
                obj['position'][1],
                obj['surface'].get_width(),
                obj['surface'].get_height())

def ship_collided():
    ship_rect = get_rect(ship)
    for asteroid in asteroids:
        if ship_rect.colliderect(get_rect(asteroid)):
            return True
    return False

collided = False

while True:


    if not ticks_to_asteroid:
        if int(pontos/10) < 80 :
            ticks_to_asteroid = 90 - (int(pontos/10))
        else:
            ticks_to_asteroid = 10

        asteroids.append(create_asteroid())
    else:
        ticks_to_asteroid -= 1

    if not ticks_to_points:
        if not collided:
            ticks_to_points = 30
            pontos += 50
    else:
        ticks_to_points -= 1

    ship['speed'] = {
        'x': 0,
        'y': 0
    }

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
        ship['speed']['y'] = -5
    elif pressed_keys[K_DOWN]:
        ship['speed']['y'] = 5
    if pressed_keys[K_LEFT]:
        ship['speed']['x'] = -5
    elif pressed_keys[K_RIGHT]:
        ship['speed']['x'] = 5

    screen.blit(background, (0, 0))

    move_asteroids()

    for asteroid in asteroids:
        screen.blit(asteroid['surface'], asteroid['position'])

    if not collided:
        collided = ship_collided()
        if ship['position'][0] < 908 and ship['position'][0] > 0 :
            ship['position'][0] += ship['speed']['x']
        else:
            if ship['speed']['x'] > 0 and ship['position'][0] <= 0 :
                ship['position'][0] += ship['speed']['x']
            elif ship['speed']['x'] < 0 and ship['position'][0] >= 908:
                ship['position'][0] += ship['speed']['x']


        if ship['position'][1] < 560 and ship['position'][1] > 0:
            ship['position'][1] += ship['speed']['y']

        screen.blit(ship['surface'], ship['position'])
    else:
        if not explosion_player:
            explosion_player = True
            explosion_sound.play()

            ship['position'][0] += ship['speed']['x']
            ship['position'][1] += ship['speed']['y']

            screen.blit(ship['surface'], ship['position'])
        elif collision_animation_counter == 3:
            text = game_font.render('GAME OVER',1, (255,0,0))
            screen.blit(text,(355,250))
        else:
            exploded_ship['rect'].x = collision_animation_counter * 48
            exploded_ship['position'] = ship['position']
            screen.blit(exploded_ship['surface'],exploded_ship['position'],exploded_ship['rect'])
            collision_animation_counter += 1



    pontuacao_text = pontuacao_font.render('Pontos :' + ' ' + str(pontos), 1, (255, 0, 0))

    screen.blit(pontuacao_text, (30, 530))


    pygame.display.update()

    time_passed = clock.tick(30)