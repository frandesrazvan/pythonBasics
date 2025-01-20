import requests
import bs4

# url = requests.get("https://example.com/")
# soup = bs4.BeautifulSoup(url.text, 'lxml')

# print(soup.select('title')[0].getText()) # Example Domain

# site_paragraphs = soup.select('p')
# for i in site_paragraphs:
#     if i.getText() == 'More information...':
#         print(f'FOUND: {i.getText()}')

# res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
# soup = bs4.BeautifulSoup(res.text, 'lxml')

# for ele in soup.select('.vector-toc-text'):
#     print(ele.text)

# res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
# soup = bs4.BeautifulSoup(res.text, 'lxml')

# computer = soup.select('#mw-content-text > div.mw-content-ltr.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > span > a > img')[0]['src']
# image_link = requests.get('https:' + computer)
# f = open('my_computer_image.jpg', 'wb')
# f.write(image_link.content)
# f.close()

