import requests
from bs4 import BeautifulSoup


def rankUrl(animeType, rankNumber=0):
    calculatRankNumber = ((rankNumber - 1) // 50) * 50
    if rankNumber <= 50:
        url = f'https://myanimelist.net/topanime.php?type={animeType}'
    else:
        url = f'https://myanimelist.net/topanime.php?type={animeType}&limit={calculatRankNumber}'
    return url


def website(animeType, rankNumber):
    soup = BeautifulSoup(requests.get(
        rankUrl(animeType, rankNumber)).text, 'lxml')
    for trRank in soup.findAll('tr', class_='ranking-list'):
        rank = trRank.td.span.text
        animeName = trRank.find('div', class_='di-ib clearfix').a.text
        imgLink = trRank.findAll('td')[1].a.img['data-src']
        globalScore = trRank.find(
            'div', class_='js-top-ranking-score-col di-ib al').span.text
        animeLink = trRank.find(
            'a', class_='hoverinfo_trigger fl-l fs14 fw-b')['href']
        if rank == str(rankNumber):
            return {'rank': rank, 'animeName': animeName,
                    'globalScore': globalScore, 'animeLink': animeLink, 'imgLink': imgLink}


print(website('anime', int(22)))
print(website('upcoming', int(78)))
print(website('movie', int(120)))

