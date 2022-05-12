#file: agent.py
#author: Senjuti Dutta
# Description: The class should implement a start() method that opens the Slither.io interface in a Chrome browser window sized at 600 x 600 in which the game is played.
#The method iteratively plays the game until it has played the number of games that was specified in the constructor.
#The method should maintain an awareness of game state (i.e., which screen is currently active usin Sellenium and Pytesseract) and
#facilitate ' start' screen , 'game'screen and 'restart'screen.
#This class supports autonomous and suggestion mode for game screen
#In the game screen it uses click and mouse controller from pyinput to use the mouse in autonomous mode and also use mouse for suggestive mode with audio suggestions and also records final length in a csv file named after the date and time at which the log_name method is executed



import decisionmaker as dm
import wm
import time
from pynput.mouse import Button, Controller
import sys
import datetime
import csv
import pyttsx3 as tts
from pynput import keyboard
from numpy import random
import cv2



class SlitherAgent():
    def __init__(self, mode = '', no_of_games = 0):
        '''The constructor requires an agent mode  which sets the agent mode i.e autonomous or suggestion
        sets the number of games to be played'''
        self.mode = mode
        self.no_of_games = no_of_games
        self.decision = dm.DecisionMaker((320, 410))
        self.window = wm.WindowManager()
        self.mouse = Controller()
        self.keyboard = keyboard.Controller()
        self.game_counter = 0
        self.directions = {
            'N': (0,1),
            'NW': (-1,1),
            'W': (-1,0),
            'SW': (-1,-1),
            'S': (0,-1),
            'SE': (1,-1),
            'E': (1,0),
            'NE': (1,1)
        }

        self.voice_commands = {
         'N': "North",
         'NW': "North West",
         'W': "West",
         'SW': "South West",
         'S': "South",
         'SE': "South East",
         'E': "East",
         'NE': "North East",
        }
        self.time = time.time()
        self.log_length = []
        self.voice = tts.init()
        #self.my_mouse = ma.MouseActions()

    def start(self):



        img = self.window.takeScreenshot(x = 20, y = 200, width = 600, height = 400, gray = False)
        text = self.window.extractText(img)
        #time.sleep(2)
        #print(dir(text))

        # -----state determination ------

        if 'Play Again' in text:
            state = 'Restart Screen'

        elif 'Play'in text:
            state = 'Start Screen'

        else:
            state = 'Game Screen'
        #print(state)

       # ----decision -----

        if state == 'Start Screen':
            print(state)
            self.mouse.position = (320, 450)
            time.sleep(0.5)
            #self.click()
            self.keyboard.type('All hail, Byron Williams')
            time.sleep(1.5)
            self.mouse.position = (320, 510)
            time.sleep(0.5)
            self.click()
            time.sleep(1.2)
            self.start()
        elif state == 'Restart Screen':
            print(state)
            self.game_counter += 1
            text1 = text.split("\n")
            #print(text1)
            for i in text1:
                if i.find("Your final length was") != -1 :
                    text1 = i
                    break;
            #print(text1)
            self.log_length.append([self.game_counter,text1])
            #self.log_game(["Your final length was",text1])
            if self.game_counter >= self.no_of_games:
                print(self.log_length)
                self.log_game(self.log_length)
                return


            #print(text)

            #log_game(text)
            self.mouse.position = (320, 510)
            time.sleep(0.5)
            self.click()
            time.sleep(1.2)
            self.start()

        else:
            print(state)
            current_time = time.time()
            lapse_time = current_time - self.time
            print(lapse_time)
            if lapse_time >= 2:
                #cv2.namedWindow('window_name', cv2.WINDOW_NORMAL)
                #cv2.resizeWindow('window_name', 600, 400)

                #cv2.imshow('window_name', img)
                #cv2.imwrite(str(datetime.datetime.now())+"circle.png",img)
                #cv2.waitKey(0)
                #cv2.destroyAllWindows()
                direction_name = self.decision.generate_decision(img)
                self.time = time.time()

                if self.mode == 'autonomous':
                # taking center position
                    self.mouse.position = (320, 410)
                    # to scale up multiplied with 200 for better movement
                    print(direction_name)
                    self.mouse.move(self.directions[direction_name][0]*200,-1*self.directions[direction_name][1]*200)
                elif self.mode == 'suggestive':
                    print(direction_name)
                    temp = ["Move to ","Move towards ","Go to ","Go towards ","Go "]
                    self.voice.say(temp[random.randint(4)] + self.voice_commands[direction_name])
                    self.voice.runAndWait()
                else:
                    print("You have not entered any mode.\nDefault user playing without any AI assistance!")
                    return

            self.start()





    def click(self):
    #A simple function that clicks and releases the left-mouse button.
    # Note: This assumes that the window has focus. You may need to perform an initial
    # click inside the app window before performing the *actual* click you want to perform.
        self.mouse.press(Button.left)
        self.mouse.release(Button.left)

    def log_game(self, text):
        csvname = str(datetime.datetime.now()) + "_" + str(self.mode)
        with open(csvname+"_run.csv","w") as csvFile:
            Fileout = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            for t in text:
                Fileout.writerow(t)
# Put it for test
if __name__ == '__main__':
    input = sys.argv
    #print(input)
    slither = SlitherAgent(mode = input[1], no_of_games = int(input[2]))
    slither.start()
