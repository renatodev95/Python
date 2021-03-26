# Faça um programa que abra e reproduza o áudio de um arquivo MP3 (em Python).
import pygame
pygame.mixer.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
