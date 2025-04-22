from urllib import request, error
#import a module with classes and functions which help opening URL's
from bs4 import BeautifulSoup
#A library that makes webscraping easier

site = "https://data.worldbank.org/indicator/SI.POV.GINI"

response = BeautifulSoup(request.urlopen(site),"html.parser")
TAB = response.find("div", class_='btn-item download')
print(TAB)
rows = TAB.find_all("a")
print(rows)
"""with open("Crime.csv", "w") as file:
    file.write(".., Country, Crime index, Safety index")
    for row in rows:
        cells = row.find_all("td")
        row_contents = []
        for cell in cells:
            row_contents.append(cell.text.strip())
        print(row_contents)
        file.write(",".join(row_contents) + "\n")"""

