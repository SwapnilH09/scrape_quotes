from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable

# get url - parsing the wiki page for Web scraping
page = requests.get("http://quotes.toscrape.com/")

# display status code
#print(page.status_code)

page = page.text
#print(page)

# create soup
soup = BeautifulSoup(page, 'html.parser')

# find all quotes
quotes = soup.find_all('div', class_='quote')

#print(quotes)

myTable = PrettyTable(["Author", "quote", "tags"])

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tags = quote.find_all('a', class_='tag')
    tag = []
    for t in tags:
        tag.append(t.text)
    myTable.add_row([author, text, tag])

print(myTable)

table_txt = myTable.get_string()

#with open("quotes.txt", "w", encoding="utf-8") as f:
#    f.write(table_txt)



