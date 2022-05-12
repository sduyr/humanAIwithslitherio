#   author:         alex williams
#   description:
#       this file implements a selenium example that opens a Chrome browser window
#       and navigates to Amazon's primary webpage.
#
#   note: this file is functional with Selenium version 3.141.0

from selenium import webdriver
import time

# This function opens a new browser window, positions and sizes it as desired. Open the site afterwards.
def open_window(width, height, x_pos = 0, y_pos = 0, url = 'http://www.amazon.com'):

    # Open the browser
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=chrome_options)
    #driver = webdriver.Chrome()

    # Sets the size of the window
    driver.set_window_size(width, height)

    # Repositions the window
    driver.set_window_position(x_pos, y_pos)

    # Navigate to Amazon
    driver.get(url)

    return driver

# Open the Window
driver = open_window(500,500)

# Start a never-ending loop to ensure our window doesn't close immediately
while True:
    print('.')
    time.sleep(3)
