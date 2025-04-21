from urllib import request, error
#import a module with classes and functions which help opening URL's
from bs4 import BeautifulSoup
#A library that makes webscraping easier

site = "https://worldpopulationreview.com/country-rankings/crime-rate-by-country"

response = BeautifulSoup(request.urlopen(site),"html.parser")
TAB = response.find("table", class_="wpr-table min-w-full border-collapse")

rows = TAB.find_all("tr")

with open("Crime.csv", "w") as file:
    file.write(".., Country, Crime index, Safety index")
    for row in rows:
        cells = row.find_all("td")
        row_contents = []
        for cell in cells:
            row_contents.append(cell.text.strip())
        print(row_contents)
        file.write(",".join(row_contents) + "\n")
