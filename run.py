import requests
from bs4 import BeautifulSoup
_rankNum = input('import witch top anime yo want to see:-')
if int(_rankNum) > 50:
    val = int(_rankNum)
    int_val = val//50
    int_num = int_val*50
    str_num = str(int_num)
    mallink = 'https://myanimelist.net/topanime.php'
    _linkreq = '?limit='
    finalurl = (mallink+_linkreq+str_num)
else:
    finalurl = 'https://myanimelist.net/topanime.php'
website = requests.get(finalurl)
soup = BeautifulSoup(website.text, 'lxml')
for div_rank in soup.findAll('tr', class_='ranking-list'):
    rank = div_rank.td.span.text
    ranknumber = rank
    div_name = div_rank.find('div', class_='di-ib clearfix')
    name = div_name.a.text
    global_score = div_rank.find('div', class_='js-top-ranking-score-col di-ib al')
    global_score = global_score.span.text
    anime_link = div_rank.find('a', class_='hoverinfo_trigger fl-l fs14 fw-b')['href']
    if ranknumber == _rankNum:
        print(rank+') '+name)
        print (global_score)
        print(anime_link)



