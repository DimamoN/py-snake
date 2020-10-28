import pygame

POP_SOUND = "res/pop.wav"
pygame.mixer.init()


def play_sound_pop():
    pop_sound = pygame.mixer.Sound(POP_SOUND)
    pop_sound.play()

