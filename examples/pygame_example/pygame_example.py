import pygame as pg

# Initializing the audio lib
pg.mixer.init()

# Loading the audio file
pg.mixer.music.load('examples/pygame_example/connor.mp3')

# Play the audio
pg.mixer.music.play()

# Keep the script running while the audio plays
while pg.mixer.music.get_busy(): 
    pg.time.Clock().tick(3) # Verifying 3 times per second if the audio is still playing, so to not use cpu unnecessarily
