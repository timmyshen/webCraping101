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
    # print temp_yield


# you need to find the tag in the source code...
# the url should be http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%2012%20and%20year(NEW_DATE)%20eq%202013
# <d:NEW_DATE m:type="Edm.DateTime">2013-12-02T00:00:00</d:NEW_DATE>
# find <d:NEW_DATE m:type="Edm.DateTime"> and get things after that.

    treasuryurl = 'http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%2012%20and%20year(NEW_DATE)%20eq%202013'
    soup = make_soup(treasuryurl)
    # print soup
    # the function soup.find_all(...) may help
    tagdate = soup.find_all('d:new_date')
    date = []
    for tag in tagdate:
        date.append(tag.text)
    print date
    # tag1m = soup.find_all('d:bc_1month')
    # tag3m = soup.find_all('d:BC_3MONTH')