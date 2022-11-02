import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time


no_of_driver = int(input("Enter number of drivers: "))
url = input("Enter Url : ")
time_to_refersh = int(input(" Enter refersh rate in sec: "))
driver = []

for i in range(no_of_driver):
     driver.append(webdriver.Chrome(executable_path="chromedriver"))
     driver[i].get(url)

while True:
      time.sleep(time_to_refersh)
      for i in range(no_of_driver):
          driver[i].refresh()