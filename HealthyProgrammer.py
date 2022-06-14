from ast import If
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':

    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    eyessecs = 30*60
    exsecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time now to stop the alarm press 'q'")
            musiconloop("water.mp3","q")
            init_water = time()
            log_now("Water Drank Done at")
        if time() - init_eyes > eyessecs:
            print("Eyes Excercise time now to stop the alarm press 'q'")
            musiconloop("Eyes.mp3","q")
            init_eyes = time()
            log_now("Eyes Relaxed Done at")
        if time() - init_exercise > exsecs:
            print("Physical Activity time now to stop the alarm press 'q'")
            musiconloop("Physical.mp3","q")
            init_exercise = time()
            log_now("Physical Activity Done at")
            break

