#!/usr/bin/python3
#_*_ coding: utf8 _*_

import string
import random
import requests
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#Si hay problemas asociados a TLS/SSL para el requests, habilitar con verify=False
from fake_useragent import UserAgent

def main():
	for x in range(3):
		try:
			cookie_l = "".join(random.choice(string.ascii_uppercase) for i in range(24))
			fake_ua = UserAgent()
			params = {
			"parameter_1":""
			}
			headers = {"Host":"",
			"User-Agent":fake_ua.random,
			"Accept":"",
			"Accept-Language":"",
			"Accept-Encoding":"",
			"Referer": "",
			"Cookie":"ASPSESSIONIDALGO="+cookie_l,
			"Upgrade-Insecure-Requests": "1",
			"Connection":"close",}
			r = requests.post(url=url,headers=headers,params=params)
			if r.status_code == 500:
				print("Not valid cookie!")
			else:
				print("Posible valid cookie found: "+cookie_l+" Server response: "+str(r.status_code))
		except:
			print("Error :(")
	else:
		print("\nEnd of loop!")
if __name__ == '__main__':
	url = ""
	try:
		main()
	except KeyboardInterrupt:
		print("\nStopping...")
		exit()