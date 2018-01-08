#! python3
"""Opens several Google search results"""

import sys
import webbrowser
import requests
import bs4

print("Googling.....")

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
links = soup.select('.r a')
tabs = min(5, len(links))


for i in range(tabs):
    webbrowser.open('http://google.com' + links[i].get('href'))
