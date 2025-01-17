import re
import requests
import bs4

# TASK: Use requests library and BeautifulSoup to connect to https://quotes.toscrape.com/ and get the HTML text from the homepage

url = 'https://quotes.toscrape.com/'

req = requests.get(url)
soup = bs4.BeautifulSoup(req.text, 'lxml')

print(soup)

# TASK: Get the names of all authors on the first page

authors = soup.select('.author')

for author in authors:
    print(author.text)

# TASK: Inspect the site and use BeautifulSoup to extract the top ten tags from the requests text shown on the top right from the home page(e.g Love, Inspirational, Live, etc...)

top_tags = soup.select('.tag-item')

for tag_name in top_tags:
    print(tag_name.select('a')[0].text)

# TASK: Notice how there is more than one page, and subsequent pages look like this https://quotes.toscrape.com/page/2/. 
# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website.

url2 = 'https://quotes.toscrape.com/page/{}/'

unique_authors = set()
page_existent = True
page = 1

while page_existent:
    req2 = requests.get(url2.format(page))
    soup2 = bs4.BeautifulSoup(req2.text, 'lxml')

    if 'No quotes found!' in req2.text:
        print('Last page found')
        break

    authors = soup.select('.author')

    for author in authors:
        unique_authors.add(author.text)

    page += 1

print(unique_authors)