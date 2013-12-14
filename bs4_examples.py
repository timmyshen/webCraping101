# coding=utf-8
__author__ = 'Benqing'


def info():
    return 'http://www.crummy.com/software/BeautifulSoup/bs4/doc/'


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup


def navigate_data_structure(soup_in):
    if type(soup_in) != BeautifulSoup:
        raise TypeError
    print soup_in.title
    print soup_in.title.name
    print soup_in.title.string
    print soup_in.title.parent.name

    # my own
    print soup_in.head
    print soup_in.head.string
    print soup_in.head.parent.name
    # -----------------------------

    # Question: find the first one?
    # How can I find the i-th one?
    print soup_in.p
    print soup_in.p['class']

    print soup_in.a
    # find_all returns a list
    print soup_in.find_all('a')

    print soup_in.find(id="link3")
    # .string gives the content
    print soup_in.find(id="link3").string


def extract_all_a_tags(soup_in):
    for link in soup_in.find_all('a'):
        print(link.get('href'))


def extract_all_text(soup_in):
    print(soup_in.get_text())

# How to use beautiful soup

# soup = BeautifulSoup(open("index.html"))
# soup = BeautifulSoup("<html>data</html>")

# Beautiful Soup transforms a complex HTML document into a complex tree of Python objects.
# But you’ll only ever have to deal with about four kinds of objects:
# Tag, NavigableString, BeautifulSoup, and Comment.

# See the document for more detail.


def tag_example():
    # My thought: b tag is deprecated.
    # http://www.w3schools.com/tags/tag_b.asp
    tag_soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
    tag = tag_soup.b
    print type(tag)
    print tag
    print tag.string
    print type(tag.get('class'))
    print tag.get('class')
    print tag.name
    # change the tag name
    tag.name = "blockquote"
    print tag
    # attrs
    # Question: why return a list?
    # Doc shows string
    print tag['class']
    print tag.attrs

    tag['class'] = 'verybold'
    tag['id'] = 1
    print tag
    print tag.attrs


if __name__ == '__main__':
    print info()

    # First example
    soup = BeautifulSoup(html_doc)
    # print(soup.prettify())
    # navigate_data_structure(soup)
    # extract_all_a_tags(soup)
    # extract_all_text(soup)

    # Tag example
    tag_example()
