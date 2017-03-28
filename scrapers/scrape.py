import csv
import requests
from BeautifulSoup import BeautifulSoup

years = ['2015-2016', '2014-2015', '2013-2014', '2012-2013', '2011-2012', '2010-2011']
url = "https://columbian.gwu.edu/2015-2016"
print url
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text.encode('utf-8'))
    list_of_rows.append(list_of_cells)

outfile = open("grants1.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Department", "Faculty", "Sponsor", "Title"])
writer.writerows(list_of_rows)