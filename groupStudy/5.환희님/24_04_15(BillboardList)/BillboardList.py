from bs4 import BeautifulSoup as bs
from urllib.parse import quote
from urllib.request import urlopen
import json

url = 'https://www.billboard.com/charts/hot-100/'
html = urlopen(url)
soup = bs(html, 'html.parser')

data = []
lists = soup.find_all('div',{'class':'o-chart-results-list-row-container'})
for row in lists:
    song_title = row.find('h3').text.strip()
    artist_name = row.find('h3').find_next().text.strip()
    song_info = {
        'title': song_title,
        'artist': artist_name
    }
    # print(song_info)
    data.append(song_info)

with open('Ex01.json', 'w') as f:
    json.dump(data, f, indent=4)

print(data)
