import pygame

POP_SOUND = "res/pop.wav"
HIT_SOUND = "res/hit.wav"
pygame.mixer.init()


def play_sound_pop():
    pop = pygame.mixer.Sound(POP_SOUND)
    pop.play()


def play_sound_hit():
    hit = pygame.mixer.Sound(HIT_SOUND)
    hit.play()
