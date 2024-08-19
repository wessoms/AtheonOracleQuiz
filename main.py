import random
import time
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.mixer.init()

def path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

sound_files = [
    path('audio/1.wav'),
    path('audio/2.wav'),
    path('audio/3.wav'),
    path('audio/4.wav'),
    path('audio/5.wav'),
    path('audio/6.wav'),
]

def tune():
    for oracle in sound_files:
        sound = pygame.mixer.Sound(oracle)
        sound.play()
        time.sleep(sound.get_length()-1)
    time.sleep(.5)

def play_sounds():
    sounds = random.sample(sound_files, 3)
    for sound_file in sounds: 
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
        time.sleep(sound.get_length()-.5)
    return sounds

def retry(soundlist):
    for sound_file in soundlist:
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
        time.sleep(sound.get_length()-.5)

def quiz():
    print('Playing')
    correct_sounds = play_sounds()

    user_guess = input('Guessed Oracles: ').split()

    while(user_guess == ['r'] or user_guess == ['q'] or user_guess == ['t']):
        if(user_guess == ['q']):
            print('Quitting.\n')
            quit()
        elif(user_guess == ['r']):
            print(" | Replaying...")
            retry(correct_sounds)
            user_guess = input('Guessed Oracles: ').split()
        else:
            print(" | Tuning...")
            tune()
            user_guess = input('Guessed Oracles: ').split()


    correct_indices = [sound_files.index(sound) +1 for sound in correct_sounds]
    user_guess_indices = [int(guess) for guess in user_guess]

    if user_guess_indices == correct_indices:
        print('Correct!\nPress ENTER to continue')
    else:
        print(f'Incorrect. Actual Answer: {correct_indices[0]} {correct_indices[1]} {correct_indices[2]}\nPress ENTER to continue')

    check = input()
    if(check == 'q'):
        print('Quitting.\n')
        quit()

if __name__ == "__main__":
    print('Welcome to the Atheon Oracle Quizzer\nPress ENTER to get started or T to tune\n\n')
    while True:
        quiz()
pygame.quit()