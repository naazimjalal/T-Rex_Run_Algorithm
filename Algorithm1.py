# Libraries below this
import pyautogui
from PIL import Image, ImageGrab
import time
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def read(audio):
    engine.say(audio)
    engine.runAndWait()

# functions below
# this function below will hit the key i want i.e - up and down arrow key

def hit(key):
    pyautogui.keyDown(key)

# function that checks if box collides with the dinosaur
def collision(data):
    for i in range(290, 400):
        for j in range(650, 670):
            if data[i, j] < 100:
                return True
    return False
    
def duck(data):
    for k in range(290, 400):
        for l in range(560, 600):
            if data[k, l] < 100:
                return True
    return False

if __name__ == "__main__":
    hit('up')
    read("this algorithm was created by Naazim")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if collision(data):
            hit('up')
        elif duck(data):
            hit('down')
    