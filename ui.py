import tkinter
from selenium import webdriver

"""
window = tkinter.Tk()

window.title("GoldDigger")

label = tkinter.Label (window, text = "Hello World").pack()

window.mainloop()
"""

#options = webdriver.Firefox()
#options.binary_location = "/usr/bin/geckodriver"
driver = webdriver.Firefox()

driver.get('https://paytm.com/digitalgold')
driver.save_screenshot("screenshot.png")

#driver.close()

