import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

titles = soup.find_all("a", class_="gem-c-document-list__item-title")
titlesTexts = []

for title in titles:
    titlesTexts.append(title.string)


descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptionsTexts = []

for description in descriptions:
    descriptionsTexts.append(description.string)