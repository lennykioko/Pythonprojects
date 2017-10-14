import urllib.request
import json
import webbrowser

def fullContactCollect(email):
	#obtain your API ket from the full contact website once you create your fullcontact account
	api_key = "xxxxxxxxx"
	email = email
	fullUrl = 'https://api.fullcontact.com/v2/person.json?apiKey=' + api_key +'&email=' + email
	with urllib.request.urlopen(fullUrl) as url:
		jsonData = json.load(url)
	print(jsonData)
	print('\n\n')
	photos = jsonData['photos']

	for item in photos:
		photo_url = item['url']
		print(photo_url)
	x = 0
	while x < 5:
		webbrowser.open(photo_url)
		x += 1
#enter the target's email below
fullContactCollect('accountname@example.com')