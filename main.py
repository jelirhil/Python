import pygame
pygame.mixer.init()
sound = pygame.mixer.Sound('/usr/share/sounds/freedesktop/stereo/phone-incoming-call.oga')
sound.play()