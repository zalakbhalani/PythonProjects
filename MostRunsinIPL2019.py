import requests
from bs4 import BeautifulSoup

response = requests.get("http://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=12741;type=tournament")
soup = BeautifulSoup(response.text, 'html.parser')
table_rows = soup.find_all('tr')
row1 = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row1.append(row)
a = "Most runs scored by a player in IPL 2019"
print(a)
print("="*len(a))

for i in range(10):
    if row1[i] == [] or len(row1[i]) < 4:
        continue
    if len(row1[i]) < 4:
        team = row1[i]
    print(str(row1[i][0])+ "\t" + str(row1[i][4])+ "\t" + str(row1[i+1][0]))




