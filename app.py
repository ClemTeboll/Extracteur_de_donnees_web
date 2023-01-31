import requests
from bs4 import BeautifulSoup
import csv

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


header = ["title", "description"]

with open("data.csv", "w") as file_csv:
    writer =  csv.writer(file_csv, delimiter=",")
    writer.writerow(header)

    for title, description in zip(titles, descriptions):
        line = [title, description]
        writer.writerow(line)