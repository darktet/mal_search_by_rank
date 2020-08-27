import requests
from bs4 import BeautifulSoup

def rankUrl(userNumber=0, listType = 'anime'):
    calculatUserNumber = ((userNumber - 1) // 50) * 50
    if userNumber <= 50:
        url = f'https://myanimelist.net/topanime.php?type={listType}'
    else:
        url = f'https://myanimelist.net/topanime.php?type={listType}&limit={calculatUserNumber}'     
    return url

def website(url):
    website = requests.get(url)
    soup = BeautifulSoup(website.text, 'lxml')
    for div_rank in soup.findAll('tr', class_='ranking-list'):
        rank = div_rank.td.span.text
        div_name = div_rank.find('div', class_='di-ib clearfix')
        name = div_name.a.text
        global_score = div_rank.find(
            'div', class_='js-top-ranking-score-col di-ib al')
        global_score = global_score.span.text
        anime_link = div_rank.find(
            'a', class_='hoverinfo_trigger fl-l fs14 fw-b')['href']
        print(rank+') '+name)
        print(global_score)
        print(anime_link)
website(rankUrl())


