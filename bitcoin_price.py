"""Checks the current Bitcoin price using requests and the Coindesk API"""
import requests

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

time = r.json()['time']['updateduk']
price = r.json()['bpi']['USD']['rate']

print("The value of one Bitcoin" "\nPrice: " + price + " USD" + "\nTime: " + time)
print("\nPowered by CoinDesk API")
