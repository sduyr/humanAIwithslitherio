#   file:           pynput_example.py
#   author:         alex williams
#   description:
#       this file implements an example demonstrating mouse control.
#       this implementation is based on an example provided by the
#       Pynput documentation found at: https://pynput.readthedocs.io
#
#   note: this file is functional with Pynput version 1.7.3

from pynput.mouse import Button, Controller
import time

def click(mouse):
    '''A simple function that clicks and releases the left-mouse button.'''
    # Note: This assumes that the window has focus. You may need to perform an initial
    # click inside the app window before performing the *actual* click you want to perform.
    mouse.press(Button.left)
    mouse.release(Button.left)

def dbl_click(mouse):
    '''A simple function that double-clicks with the left-mouse buttons.'''
    # Double click; this is different from pressing and releasing
    # twice on macOS
    mouse.click(Button.left, 2)

# Define a mouse controller.
mouse = Controller()

# Assuming that the Amazon browser window is open, we can begin.

# 1. Set the mouse position to the "Best Sellers" location.
mouse.position = (80, 230)
print('Now we have moved it to {0}'.format(mouse.position))

# Sleep to give preparation time for the mouse to move.
time.sleep(0.5)
click(mouse)
time.sleep(2)

# 2. Set the mouse position to the "Reload" list item location.
mouse.position = (150, 300)
time.sleep(0.5)
click(mouse)
time.sleep(2)

# 3. Set the mouse position to the "$25.00" location.
mouse.position = (10, 300)
time.sleep(0.5)
click(mouse)
time.sleep(2)

# 4. Scroll down a bit vertically to see the Add to Cart button.
mouse.scroll(0, 5)

# 5. Set the mouse position to the "$25.00" location.
mouse.position = (250, 300)
time.sleep(0.5)
click(mouse)
print('Added to Cart!')


# Note: Alternatives to mouse movements could be made relatively in 2D space, e.g.
# mouse.move(5, -5)
