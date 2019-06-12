#!/usr/bin/python3


import requests 
import json 

# inspired by https://github.com/mrpappas/live-bitcoin-price 

def get_btc(currency):
	r = requests.get('https://blockchain.info/ticker')
	if r.status_code != 200: 
		return [] 
	else:
		jr = r.json()

	value = jr[currency]['last']
	symbol = jr[currency]['symbol']
	text = "the current bitcoin price for {0} is {1}{2}".format(currency, symbol, value)
	return text

currencies = ['GBP','USD']

for currency in currencies:
	print(get_btc(currency))

