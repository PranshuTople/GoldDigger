import numpy as np
import pyscreenshot as ImageGrab
import cv2
#import pytesseract
import tkinter
from selenium import webdriver
from pynput.mouse import Listener
num = 0
fromx = 0
fromy = 0
tox = 10
toy = 10

def on_click(x,y, button, pressed):
	global num, fromx, fromy, tox, toy
	num = num +1
	if (num % 2) == 0:
		tox = x
		toy = y
	else:
		fromx = x
		fromy = y
	#print("{} {} {} {}".format(fromx,fromy,tox,toy))



while (1):
	
	image = ImageGrab.grab(bbox=(fromx,fromy,tox,toy))
	imagenp = np.array(image.getdata(),dtype='uint8').reshape((image.size[1],image.size[0],3))
	cv2.imshow('window', imagenp)
	with Listener(on_click=on_click) as listener:
		listener.join()
"""
window = tkinter.Tk()

window.title("GoldDigger")

label = tkinter.Label (window, text = "Hello World").pack()

window.mainloop()
"""
"""
driver = webdriver.Firefox()

driver.get('https://paytm.com/digitalgold')
driver.save_screenshot("screenshot.png")

#driver.close()
"""
