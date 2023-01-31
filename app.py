import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

def findClassInSpecificTag(tag, SearchedClass):
    return soup.find_all(tag, class_= SearchedClass)

def appendTextInList(src, currentList):
    for title in src:
        currentList.append(title.string)
    return currentList

titles = findClassInSpecificTag("a", "gem-c-document-list__item-title")
titlesTexts = []
titlesResult = appendTextInList(titles, titlesTexts)

descriptions = findClassInSpecificTag("p", "gem-c-document-list__item-description")
descriptionsTexts = []
descriptionsResult = appendTextInList(descriptions, descriptionsTexts)

print(descriptionsResult)