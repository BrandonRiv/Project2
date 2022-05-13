'''
https://www.youtube.com/watch?v=4hdK9Gey76E
'''
import time
import threading

# Install pip pynput
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="t")

clicking = False
mouse = Controller()


'''
Clicker needs a time.sleep or else it will not register every click
'''
def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.0001)


'''
Function to toggle on and off the clicking
'''
def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

