#file: wm.py
#author: Senjuti Dutta
#The class’s constructor should use the Chrome webdriver to open the Slither.io interface in a Chrome browser window sized at 600 x 600 in which the game is played.
#The class implements a “takeScreenshot” function that facilitates screenshots.
#The function should include parameters for a starting set of x and y coordinates alongside the width and height of the screenshot.
#The function should support thresholding. The function should return the image screenshot.
#The class implements an “extractText” function that extracts text from images using Pytesseract.
#The function should take an image as a parameter and return the extracted text.


from selenium import webdriver
import time
import numpy as np
import cv2
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

import mss
import mss.tools
from PIL import Image
import PIL.ImageOps

threshold = 50
var = 37


class WindowManager():
    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver")
        self.driver.get('http://slither.io')
        self.driver.set_window_size(width = 600, height = 600)
        #self.takeScreenshot(x = 50, y = 500, width = 400, height = 50, gray = False)
        #self.driver.save_screenshot("img.png")
        #image = Image.open("img.png")
        #image.show()




    def takeScreenshot(self,x, y, width, height, reduction_factor = 1, gray = True):
        '''A simple function that returns a screenshot of a rectangular area on the screen.'''
        with mss.mss() as sct:
            # The screen part to capture
            #mon = sct.monitors
            #print(mon)
            region = {'left': x, 'top': y, 'width': width, 'height': height}


            # Grab the data
            img = sct.grab(region)
            mss.tools.to_png(img.rgb, img.size, output="screenshot.png")

            if gray:
                result = cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2GRAY)
            else:
                result = cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2BGR)

            img = result[::reduction_factor, ::reduction_factor]
            #return img



            for rows in range(0, len(img)):
                for cols in range(0, len(img[0])):
                    a = img[rows][cols]
                    if a[0] > threshold and a[1] > threshold and a[2] > threshold and max(a) - min(a) < var:
                        img[rows][cols] = [0, 0, 0]
                    else:
                        img[rows][cols] = [255,255,255]
            #img = cv2.imread("screenshot.png")


            #cv2.namedWindow('window_name', cv2.WINDOW_NORMAL)
            #cv2.resizeWindow('window_name', 300, 50)
            #cv2.imshow('window_name', img)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()

            #img.show()
            return img



    #img = takeScreenshot(x= 50, y= 210, width = 300, height = 40, gray = False)

    def extractText(self,img):
        extracted_text = pytesseract.image_to_string(img)
        print(extracted_text)
        return extracted_text
# kept it for testing
if __name__ == '__main__':

    abc = WindowManager()
    image = abc.takeScreenshot(x = 50, y = 500, width = 400, height = 50, gray = False)
    text = abc.extractText(image)
