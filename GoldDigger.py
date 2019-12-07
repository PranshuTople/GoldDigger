import numpy as np
import time
import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
from PIL import ImageGrab
import cv2
import pytesseract

driver_path = "G:/Robo-Freaks/Projects/DYlogin/chromedriver.exe"
url = 'https://paytm.com/digitalgold'

amount = 1			# Amount to Invest
BuyThresh = 3900 	# Will buy if less than this
SellThresh = 4000 	# Will sell if more than this

def buyGold():
	global amount
	global url

	pyautogui.click(x=190,y=493,button="left")
	pyautogui.press(['backspace', 'backspace', 'backspace'])
	pyautogui.typewrite(str(amount))  
	pyautogui.click(x=194,y=609,button="left")
	time.sleep(5)
	pyautogui.click(x=226,y=710,button="left")
	pyautogui.click(x=436,y=19,button="left")
	time.sleep(10)
	pyautogui.click(x=966,y=424,button="left")
	time.sleep(10)
	browser.get(url)
	browser.set_window_position(0, 0)
	browser.set_window_size(400, 768)
	time.sleep(2)


def sellGold():
	pass

browser = webdriver.Chrome(driver_path)
browser.get(url)
pyautogui.click(x=343,y=360,button="left")
time.sleep(10)
browser.set_window_position(0, 0)
browser.set_window_size(400, 768)


browser2 = webdriver.Chrome(driver_path)
browser2.get(url)
pyautogui.click(x=343,y=360,button="left")
time.sleep(10)
browser2.set_window_position(500, 0)
browser2.set_window_size(400, 768)
pyautogui.click(x=729,y=399,button="left")


while (1):
	buyRAWimage = ImageGrab.grab(bbox=(108,345,175,368))
	sellRAWimage = ImageGrab.grab(bbox=(603,345,677,368))
	buyimage = np.array(buyRAWimage.getdata(),dtype='uint8').reshape((buyRAWimage.size[1],buyRAWimage.size[0],3))
	sellimage = np.array(sellRAWimage.getdata(),dtype='uint8').reshape((sellRAWimage.size[1],sellRAWimage.size[0],3))
	cv2.imshow('buyRate', buyimage)
	cv2.imshow('sellRate', sellimage)

	buyPrice = pytesseract.image_to_string(buyimage, lang='eng')
	buyPrice = buyPrice[0:(len(buyPrice)-2)]
	buyPrice = float(buyPrice)
	print(buyPrice)

	sellPrice = pytesseract.image_to_string(sellimage, lang='eng')
	sellPrice = sellPrice[0:(len(sellPrice)-2)]
	sellPrice = float(sellPrice)

	if (buyPrice<=BuyThresh):
		buyGold()
		time.sleep(10)

	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break

