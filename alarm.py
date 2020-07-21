from sys import platform as platform_name
if platform_name == "darwin":
	import os
elif platform_name == "win32" or platform_name == "win64":
	from win10toast import ToastNotifier
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from config import *

def notify(title, text):
	if platform_name == "darwin":
                os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
	elif platform_name == "win32" or platform_name == "win64":
		toast = ToastNotifier()
		toast.show_toast("Target", "sold out")

# notify("Bestbuy", "Ring Fit Adventure is available at Bestbuy!")
def check_bestbuy(driver):
	start = time.time()
	driver.get(bestbuy_url)
	mid = time.time()
	content = driver.page_source
	end = time.time()
	with open('bestbuy.html', 'wb') as f:
		f.write(content.encode('utf-8'))
	# driver.quit()
	
	soup = BeautifulSoup(open("bestbuy.html"), features="lxml")
	
	button = soup.find("button", attrs={"class": "btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button"})
	timestamp = time.ctime(time.time())
	if button:
		if button.text == "Add to Cart":
			print("available at bestbuy at "+timestamp)
			notify("Bestbuy", bestbuy_url)
	else:
		print("sold out at bestbuy at "+timestamp)


def check_target(driver):
	driver.get(target_url)
	time.sleep(5)
	content = driver.page_source
	with open('target.html', 'wb') as f:
		f.write(content.encode('utf-8'))
	# driver.quit()

	soup = BeautifulSoup(open("target.html"), features="lxml")
	target = soup.find("div", attrs={"data-test": "orderPickupMessage"})
	if target:
		target = target.find("a")
	timestamp = time.ctime(time.time())
	if target and target.text == target_store:
		print("available at target at "+timestamp)
		notify("Target", target_url)
	else:
		print("sold out at target at "+timestamp)
	end = time.time()


options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)
while True:
	if use_bestbuy:
		check_bestbuy(driver)
	if use_target:
		check_target(driver)
	time.sleep(check_interval)
