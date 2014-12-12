from bs4 import BeautifulSoup
import requests
import os
import sys

try:
    os.mkdir('joblist')
except WindowsError:
    pass
    
##Getting Url##    
url = "http://joblist.bdjobs.com/jobsearch.asp?fcatId=8&icatId="
responce = requests.get(url)
content = responce.text.encode("utf8", "ignore")
soup = BeautifulSoup(content)

def get_content(next_url):
    print next_url
    resp = requests.get(next_url)
    content = resp.text.encode("utf8", "ignore")
    return content
    
job_link = []
job_title = soup.findAll("div", {"class" : "job_title_text"})
for name in job_title:
    #print name.find('a').string
    job_link.append('http://joblist.bdjobs.com/'+name.a['href'])
    #print job_link
    
while len(job_link) > 0:
    print len(job_link)
    next_url = job_link.pop(0)
    #print next_url
    content = get_content(next_url)
    #job_link = get_links(content)
    
