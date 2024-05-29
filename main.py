import json, time, keyboard,sys
import win32api
from ctypes import WinDLL
import numpy as np
from mss import mss
user32, shcore = (
    WinDLL("user32", use_last_error=True),
    WinDLL("shcore", use_last_error=True),
)

def exiting(): #function for exiting
    try:
        sys.exit()
    except:
        raise SystemExit


shcore.SetProcessDpiAwareness(2)
WIDTH, HEIGHT = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] #get size of the monitor
# we take image of square in the center of screen with size ZONE * ZONE
ZONE = 4 
#boundaries of our grab zone
GRAB_ZONE = (
    int(WIDTH / 2 - ZONE),
    int(HEIGHT / 2 - ZONE),
    int(WIDTH / 2 + ZONE),
    int(HEIGHT / 2 + ZONE),
)

class triggerbot:
    def __init__(self):
        print("initialization")
        self.sct = mss()
        self.triggerbot = False #mark that we holding key for activation of trigger
        self.exitProgram = False
            #opening config file
        with open('config.json') as jsonFile:
            data = json.load(jsonFile)

        try:
            self.triggerHotkey = int(data["trigger_hotkey"],16) #hotkey for activating trigger (shift)
            self.exitHotkey = int(data["exit_hotkey"],16) #hotkey for exiting trigger (f9)
            self.triggerDelay = data["trigger_delay"] 
            self.baseDelay = data["base_delay"]
            self.colorTolerance = data["color_tolerance"]
            self.threshold = data["threshold"]
            self.R, self.G, self.B = (250, 100, 250)  # purple
        except:
            exiting()
        print("bot is started")

    def searcherInO(self):
        img = np.array(self.sct.grab(GRAB_ZONE)) #getting image from grab zone


        pmap = np.array(img)
        pixels = pmap.reshape(-1, 4) 
        #converting in comfortable format of 2d array in next format:
        #we separated our RGBA canal in 4 different columns     
        colorMask = (
            (pixels[:, 0] > self.R -  self.colorTolerance) & (pixels[:, 0] < self.R +  self.colorTolerance) &
            (pixels[:, 1] > self.G -  self.colorTolerance) & (pixels[:, 1] < self.G +  self.colorTolerance) &
            (pixels[:, 2] > self.B -  self.colorTolerance) & (pixels[:, 2] < self.B +  self.colorTolerance)
        )
        matchingPixels = pixels[colorMask]
        print(pixels[0:3, 0])
        
        if self.triggerbot and len(matchingPixels) > self.threshold:
            delayPercentage = self.triggerDelay / 100.0  
            
            actualDelay = self.baseDelay + self.baseDelay * delayPercentage
            
            time.sleep(actualDelay)
            print("enemy is found")
            keyboard.press_and_release("k")

  
    def hold(self):
        while True:
            while win32api.GetAsyncKeyState(self.triggerHotkey) < 0: #check if trigger_hotkey (shift by default is holded)
                self.triggerbot = True
                #print("shift is holded")
                self.searcherInO()
            else:
                time.sleep(0.1)
            if keyboard.is_pressed("f9"):  # Check for the exit keybind
                print("trigged holde mode exit")
                self.exitProgram = True
                exiting()

    def starter(self):
        while not self.exitProgram:  # Keep running until the exit_program flag is True
            self.hold()

triggerbot().starter()
