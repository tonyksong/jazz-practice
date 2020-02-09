import requests
from bs4 import BeautifulSoup
import random

URL = 'https://www.learnjazzstandards.com/blog/50-jazz-standards-you-need-to-know/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

items = soup.findAll("li")

standards = []
for i in items:
    convert_to_string = str(i)
    if convert_to_string.startswith("<li><s"):
        standard_url = convert_to_string.split('<')
        standard_name = standard_url[3].split('>')
        standards.append(standard_name[1])

keys = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']

tempo = list(range(60, 201, 2))

print('Tune:', random.choice(standards))
print('Key:', random.choice(keys))
print('Tempo:', random.choice(tempo))
