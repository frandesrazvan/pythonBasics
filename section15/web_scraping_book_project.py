# GOAL: Get the title of every book with a 2 star rating
import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

total_pages = 50
two_star_title = []
for i in range(1, total_pages + 1):
    req = requests.get(base_url.format(i))
    soup = bs4.BeautifulSoup(req.text, 'lxml')

    books = soup.select('.product_pod')

    for book in books:
        # if len(book.select('.star-rating.Two')) != 0:
        if 'star-rating Two' in str(book):
            two_star_title.append(book.select('a')[1]['title'])
        
print(two_star_title)

