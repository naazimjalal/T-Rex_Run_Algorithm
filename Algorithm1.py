# Libraries below this
import pyautogui
import webbrowser
from PIL import Image, ImageGrab
import time
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def read(audio):
    engine.say(audio)
    engine.runAndWait()
# functions below
def creds():
    read("This Algorithm was created by Naazim, on twenty first of september, twenty twenty")
    time.sleep(1)
    read("Starting")
    time.sleep(2)
    read("Algorithm is activating in 5, 4, 3, 2, 1")

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
    # first grab an image of the window and convert to grayscale for faster results
    '''creds()'''
    hit('up')
    read("this algorithm was created by Naazim")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if collision(data):
            hit('up')
        elif duck(data):
            hit('down')
    