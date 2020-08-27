import requests
from bs4 import BeautifulSoup


def perfectNumber(message):
    message = message
    while True:
        try:
            user_input = int(input('Witch Rank Number You Want to See:- '))
        except ValueError:
            print('Please Import only NUMBER')
            continue
        else:
            return user_input


_rankNum = perfectNumber('message')
if _rankNum > 50:
    int_val = _rankNum//50
    int_num = int_val*50
    finalurl = ('https://myanimelist.net/topanime.php?limit='+str(int_num))
else:
    finalurl = 'https://myanimelist.net/topanime.php'

website = requests.get(finalurl)
soup = BeautifulSoup(website.text, 'lxml')
for div_rank in soup.findAll('tr', class_='ranking-list'):
    rank = div_rank.td.span.text
    div_name = div_rank.find('div', class_='di-ib clearfix')
    name = div_name.a.text
    global_score = div_rank.find('div', class_='js-top-ranking-score-col di-ib al')
    global_score = global_score.span.text
    anime_link = div_rank.find('a', class_='hoverinfo_trigger fl-l fs14 fw-b')['href']
    if rank == str(_rankNum):
        print(rank+') '+name)
        print (global_score)
        print(anime_link)

