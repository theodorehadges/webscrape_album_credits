#import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://www.allmusic.com/album/the-college-dropout-mw0000326741/credits'

hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(my_url,headers=hdr)
page = urlopen(req)
the_soup = soup(page)
the_soup.prettify()

data_file = open("kanye_the-college-dropout.txt", "w")

for tr in the_soup.find_all('tr'):
    stack = []
    for td in tr.findAll('td'):
        stack.append(td.text.replace('\n', '').replace('\t', '').strip())

    data_file.write(", ".join(stack) + '\n')

