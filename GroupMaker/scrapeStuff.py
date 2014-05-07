# Chris Allulis
# What does this program do?

from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.chicagoreader.com"

def get_category_links(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(urlopen(section_url))
    print soup.find("dl","boccat")
    boccat = soup.find("dl", "boccat")
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("d d")]
    return category_links

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html,"lxml")

def get_category_winner(category_url):
    html = urlopen(category_url).read()
    soup = BeautifulSoup(html, "lxml")
    category = soup.find("h1", "headline").string
    winner = [h2.string for h2 in soup.findAll("h2", "boc1")]
    runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
    return {"category": category,
            "category_url": category_url,
            "winner": winner,
            "runners_up": runners_up}

def main():
    print get_category_links(BASE_URL)

if __name__ == "__main__":
    main()

