#   file:           vision_example.py
#   author:         alex williams
#   description:
#       this file implements an example demonstrating screenshotting
#       alongside the transcription of text in the screenshot. it also
#       demonstrates how you can verify screenshots with a window pop-up.
#
#   note: this file is functional with:
#       opencv-python (4.4.0.44)
#       python-mss (6.1.0)
#       pillow (8.0.1)
#       pytesseract (0.3.6).

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

threshold = 190
var = 10

def createWindow(img, width, height):
    '''A simple function for showing image variables.'''
    cv2.namedWindow('window_name', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('window_name', width, height)

    cv2.imshow('window_name', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def screenshot(x, y, width, height, reduction_factor = 1, gray = True):
    '''A simple function that returns a screenshot of a rectangular area on the screen.'''
    with mss.mss() as sct:
        # The screen part to capture
        region = {'left': x, 'top': y, 'width': width, 'height': height}

        # Grab the data
        img = sct.grab(region)
        mss.tools.to_png(img.rgb, img.size, output="screenshot.png")

        if gray:
            result = cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2GRAY)
        else:
            result = cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2BGR)

        img = result[::reduction_factor, ::reduction_factor]
        return img



# Capture a screenshot at a predetermined location.
img = screenshot(x= 50, y= 210, width = 300, height = 40, gray = False)

# Display the captured image.
# Note: To dismiss the window, select it and hit Enter.
#createWindow(img, 300, 50)

# Iterate over the image and apply thresholding naively,
# e.g., if anything looks like text, turn it black. Otherwise, turn everything else white.
'''
for rows in range(0, len(img)):
    for cols in range(0, len(img[0])):
        x = img[rows][cols]
        if x[0] > threshold and x[1] > threshold and x[2] > threshold and max(x) - min(x) < var:
            img[rows][cols] = [0, 0, 0]
        else:
            img[rows][cols] = [255,255,255]
'''
# Display the thresholded image.
# Note: To dismiss the window, select it and hit Enter.
createWindow(img, 300, 50)

# Send the thresholded image through Pytesseract to extract the text.
text = pytesseract.image_to_string(img)
print("Extracted Text: ")
print(text)
