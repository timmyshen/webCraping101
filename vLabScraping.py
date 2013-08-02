__author__ = 'benqing.shen'

from bs4 import BeautifulSoup
from urllib2 import urlopen


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

if __name__ == '__main__':
    # food_n_drink = ("http://www.chicagoreader.com/chicago/"
    #                 "best-of-chicago-2011-food-drink/BestOf?oid=4106228")

    my_link = "http://vlab.stern.nyu.edu/analysis/VOL.SPX:IND-R.GARCH"

    # categories = get_category_links(food_n_drink)

    soup = make_soup(my_link)
    prediction = soup.find("div", {"id": "sum_prediction"}).encode_contents().strip()
    print type(prediction)
    print prediction


    # data = []  # a list to store our dictionaries
    # for category in categories:
    #     winner = get_category_winner(category)
    #     data.append(winner)
    #     sleep(1)  # be nice
    #
    # print data