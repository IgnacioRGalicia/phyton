import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4a.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
# from bs4 import BeautifulSoup
# import requests

# url = 'http://www.google.com/'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'lxml')

