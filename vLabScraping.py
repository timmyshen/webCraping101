__author__ = 'benqing.shen'

from bs4 import BeautifulSoup
from urllib2 import urlopen


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


if __name__ == '__main__':
    my_link = "http://vlab.stern.nyu.edu/analysis/VOL.SPX:IND-R.GARCH"

    soup = make_soup(my_link)
    prediction = soup.find("div", {"id": "sum_prediction"}).encode_contents().strip()
    print type(prediction)
    print prediction

