from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage

#for now the program will use a default search value of "Construction" to look for jobs

#create empty lists for project info
projects = []
publication_dates = []
locations = []
closing_dates = []
organizations = []
sol_number = []
description = []

#set data to spoof the user agent
url = "https://www.bidnetdirect.com/public/solicitations/open?keywords=Construction"
req = urllib.request.Request(
    url,
    data = None,
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
    )

#find the number of pages available to search
current_page = urllib.request.urlopen(req)
html = current_page.read().decode("utf-8", errors = 'ignore')
soup = bs(html, 'html.parser')
print(soup)