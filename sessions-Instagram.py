#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@ruks3
# Coded by ruks,or,muntazir
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# Instagram : https://instagram.com/_v_go?utm_medium=copy_link
# github : https://github.com/mudiv
# ---------------------
import requests,re



class login:
	def __init__(self,username,password):
		self.username = username
		self.password =password
		self.request = requests.Session()
		pass
	def csrf(self):
		response = self.request.get('https://www.instagram.com/accounts/login/')
		c = re.findall(r"csrf_token\":\"(.*?)\"",response.text)[0]
		return c
	def session(self):
		response =self.request.post("https://www.instagram.com/accounts/login/ajax/",headers={'Host': 'www.instagram.com','content-length': '333','sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-ig-app-id': '1217981644879628','x-ig-www-claim': '0','x-requested-with': 'XMLHttpRequest','sec-ch-ua-mobile': '?1','x-instagram-ajax': '4b5f8c8eb791','viewport-width': '412','content-type': 'application/x-www-form-urlencoded','accept': '*/*','x-csrftoken':self.csrf(),'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','x-asbd-id': '198387','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua-platform': '"Android"','origin': 'https://www.instagram.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.instagram.com/'},data={'username':self.username,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{self.password}','queryParams': '{}','optIntoOneTap': 'false'}).text
		if 'authenticated":true' in response:
			print("login true \n","="*10)	
			ses =self.request.cookies["sessionid"]
			print(ses)
		else:

			print("login false")	

username = input(" username :")
password = input(" password :")			


login(username,password).session()
		