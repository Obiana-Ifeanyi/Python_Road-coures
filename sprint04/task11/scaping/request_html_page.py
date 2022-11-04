
# USING URLLIB.RETUEST MODULE
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)

# read html_page and convert from byte() to string()
html = page.read().decode("utf-8")

# parser html
soup = BeautifulSoup(html, "html.parser")

print (soup.get_text())






# USING REQUEST MODULE
import requests
from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/dionysus"
x = requests.get(url)

page = x.text
soup = BeautifulSoup(page, "html.parser")
print (soup.get_text())

