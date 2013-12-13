__author__ = 'Benqing'

from urllib2 import urlopen

from bs4 import BeautifulSoup


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


if __name__ == '__main__':
    full_link = '''
                http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield
                '''
    treasury_url = 'http://www.treasury.gov'
    treasury_resource_center = '/resource-center'
    treasury_data_chart_center = '/data-chart-center'
    rest_page = '/interest-rates/Pages/TextView.aspx'
    data_yield = "?data=yield"

    link = treasury_url + treasury_resource_center + treasury_data_chart_center + rest_page + data_yield

    soup = make_soup(link)

    temp_yield = soup.find("").encode_contents().strip()
    # print type(temp_yield)
    print temp_yield

