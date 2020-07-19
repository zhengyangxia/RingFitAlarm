import os
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from config import *

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

# notify("Bestbuy", "Ring Fit Adventure is available at Bestbuy!")
def check_bestbuy(apikey):
	
	url = "https://api.bestbuy.com/v1/products(sku="+bestbuy_sku+")?apiKey="+bestbuy_api+"&sort=onlineAvailability.asc&show=onlineAvailability&format=json"
	r = requests.get(url)
	r_json = r.json()
	timestamp = time.ctime(time.time())
	if r_json['products'][0]['onlineAvailability']:
		print "available at bestbuy at "+timestamp
		notify("Bestbuy", bestbuy_url)
	else:
		print "sold out at bestbuy at "+timestamp


def check_target(options):	
	driver = webdriver.Chrome(chrome_options=options)
	driver.get(target_url)
	time.sleep(5)
	content = driver.page_source
	with open('target.html', 'w') as f:
		f.write(content.encode('utf-8'))
	driver.quit()

	soup = BeautifulSoup(open("target.html"), features="lxml")
	target = soup.find("div", attrs={"data-test": "orderPickupMessage"})
	if target:
		target = target.find("a")
	timestamp = time.ctime(time.time())
	if target and target.text == target_store:
		print "available at target at "+timestamp
		notify("Target", target_url)
	else:
		print "sold out at target at "+timestamp


options = webdriver.ChromeOptions()
options.add_argument("headless")
while True:
	if use_bestbuy:
		check_bestbuy(apikey)
	if use_target:
		check_target(options)
	time.sleep(check_interval)