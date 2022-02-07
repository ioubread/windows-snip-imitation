import pyautogui as pyg
import time
from tkinter import *
from PIL import Image, ImageTk, ImageOps
from pathlib import Path
import os
import win32api 
import threading

homeDir = Path.home()
desktopDir = homeDir / "Desktop"
os.chdir(desktopDir)

adjustment = -2
resolutions = (1920, 1080)
unixtimestamp = round(time.time())
screenshotName = str(unixtimestamp) + ".png"
screenshotNameCropped = str(unixtimestamp) + "_cropped.png"

myScreenshot = pyg.screenshot()
myScreenshot.save(screenshotName)

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = Tk()
        self.root.attributes('-fullscreen',True) 

        test = ImageTk.PhotoImage(image1)

        self.canvas = Canvas(self.root, width=1920, height=1080, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)

        self.x = self.y = 0

        self.rect = None
        self.start_x = None
        self.start_y = None

        self.canvas.create_image(0, 0, anchor="nw", image=test)

        self.root.mainloop()

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, fill="black", stipple="gray50")

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)

        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)


image1 = Image.open(screenshotName)
image1 = image1.resize(resolutions, Image.ANTIALIAS)

app = App()

state_left = win32api.GetKeyState(0x01)
state_right = win32api.GetKeyState(0x02)

coordinates = []

while len(coordinates) < 2:

    a = win32api.GetKeyState(0x01) 
    b = win32api.GetKeyState(0x02) 
    

    if a != state_left:  
        state_left = a 
        if a < 0: 
            coordinates.append(pyg.position())

        else: 
            coordinates.append(pyg.position())
            app.root.quit()
            break

    if b != state_right:
        state_right = b 
        if b < 0: 
            print('Right Button Pressed') 
        else: 
            print('Right Button Released') 

    time.sleep(0.001)

firstClick, secondClick = coordinates

coordXs = sorted([firstClick.x, secondClick.x])
coordYs = sorted([firstClick.y, secondClick.y])

coordLeft = coordXs[0]
coordTop = coordYs[0]
coordRight = coordXs[1]
coordBottom = coordYs[1]

os.remove(screenshotName)
image2 = image1.crop((coordLeft, coordTop, coordRight, coordBottom))
image2.save(screenshotNameCropped)
