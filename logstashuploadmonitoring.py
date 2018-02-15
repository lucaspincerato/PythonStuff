import requests
import time

while 1==1:
	resp = requests.get("http://localhost:9200/cars/_count?pretty")
	print(resp.text)
	time.sleep(3)
