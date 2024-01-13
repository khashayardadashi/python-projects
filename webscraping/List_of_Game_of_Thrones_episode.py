import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'

r=requests.get(url)
b=BeautifulSoup(r.text ,'html.parser')

eps=[]
ep_table=b.find_all('table',class_='wikiepisodetable')

for table in ep_table:
    headers=[]
    rows=table.find_all('tr')
    for header in table.find('tr').find_all('th'):
        headers.append(header.text)
    for row in table.find_all('tr')[1:]:
        v=[]
        for col in row.find_all(['td','th']):
            v.append(col.text)
    if v:
        eps_dict={headers[i]:v[i] for i in range(len(v))}
        eps.append(eps_dict)

for j in eps:
    print(j)
