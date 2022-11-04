
# USING REQUEST MODULE
import requests
from bs4 import BeautifulSoup


url = "https://www.flexjobs.com/search?search=&search=developer"

# 'download data/infomation
x = requests.get(url)

page = x.content

# parsing the html page
# the "html.parser" can be used but more effecient parser 'lxml' is used for this script
soup = BeautifulSoup(page, 'lxml')


#find_job_result = soup.find('h2', class_="d-inline-block").text
#print (find_job_result)



jobs = soup.find_all('li', class_="m-0 row job") #.text
#role = jobs.find_all('a', class_="job-title job-link")

print (jobs)



