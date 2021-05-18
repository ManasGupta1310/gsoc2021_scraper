import requests
from bs4 import BeautifulSoup
import csv

csv_file=open('gosc2021.csv', 'w', encoding="utf-8")

csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Name', 'Organization', 'Project'])

for x in range(1,66):
    URL = "https://summerofcode.withgoogle.com/api/program/current/project/?page="+str(x)+"&page_size=20"
    
    source= requests.get(URL)
    response=source.json()
    projects=response["results"]

    for x in range(1,len(projects)):
        name=projects[x]['student']['display_name']
        org=projects[x]['organization']['name']
        proj=projects[x]['title']
        print(name)
        print(org)
        print(proj)
        print()

        csv_writer.writerow([name, org, proj])


csv_file.close()