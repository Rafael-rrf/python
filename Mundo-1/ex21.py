import pygame

pygame.init()
pygame.mixer.music.load("teste.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass