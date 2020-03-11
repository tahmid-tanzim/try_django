import requests
import json
from bs4 import BeautifulSoup, element

URL = 'https://en.wikipedia.org/wiki/List_of_universities_in_Bangladesh'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='mw-content-text')

wikitbls = results.find_all('table', class_=('wikitable', 'sortable', 'jquery-tablesorter'))

universities = []
pk = 1

for table in wikitbls:
    tbodys = table.find('tbody')
    for index, tbody in enumerate(tbodys, start=0):
        if index > 0 and type(tbody) == element.Tag:
            # print(index, tbody)
            td = tbody.find_all('td')
            obj = {
                "model": "profile.organization",
                "pk": pk,
                "fields": {
                    "name_in_english": '',
                    "type": "Educational Institution",
                    "established_year": '',
                    "location": ''
                }
            }
            for col, item in enumerate(td, start=0):
                # print(col, item)
                if col == 0:
                    pk += 1
                    a_tag = item.find('a')
                    # print(a_tag.text.strip())
                    obj['fields']['name_in_english'] = a_tag.text.strip()
                elif col == 2:
                    # print(item.text.strip())
                    obj['fields']['established_year'] = int(item.text.strip())
                elif col == 3:
                    # print(item.text.strip())
                    obj['fields']['location'] = item.text.strip()
                else:
                    # print(col, item, end='')
                    pass
            universities.append(obj)

print(universities)

with open('/Users/tanzim/Projects/try_django/universities.json', 'w') as fout:
    json.dump(universities, fout)
