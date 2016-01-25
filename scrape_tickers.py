import re

from HTMLParser import HTMLParser
from requests import get

URL = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=%s&owner=exclude&action=getcompany&Find=Search'

# HTML2TextParser
# Usage:
# parser.feed(contents)
# text = parser.get_text()

class HTML2TextParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.text = []
    def handle_data(self, data):
        self.text.append(data)
        return data
    def get_text(self):
        return ' '.join(self.text)

def scrape_ticker_for_cik(ticker):
    url = URL % ticker
    response = get(url)
    parser = HTML2TextParser()
    parser.feed(response.text)
    text = parser.get_text()

    match = re.search(r'CIK\s*#:\s*(\d+)', text)
    if match:
        cik = match.group(1)
        return cik
    else:
        return None

print(scrape_ticker_for_cik('AAVL'))
print(scrape_ticker_for_cik('ATRA'))


