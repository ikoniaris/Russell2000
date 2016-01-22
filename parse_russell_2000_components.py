from bs4 import BeautifulSoup
import csv

f = open("russell2000.html", "r")
contents = f.read()
f.close()

soup = BeautifulSoup(contents)
tbody = soup.find("tbody")
rows = tbody.find_all("tr")

with open("russell_2000_components.csv", "w") as russell_2000_out:
    writer = csv.DictWriter(russell_2000_out, ['Ticker', 'Name'])
    writer.writeheader()
    for row in rows:
        columns = row.find_all("td")
        ticker = columns[0].find("a").get_text()
        name = columns[1].find("a").get_text()
        writer.writerow({'Ticker' : ticker, 'Name' : name})

