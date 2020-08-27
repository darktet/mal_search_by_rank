def perfectNumber(userNumber):
    if userNumber > 50:
        rankNumber = (userNumber // 50) * 50
        return print('over'+str(rankNumber))
    else:
        rankNumber = ''
        return print('50orLessThen50')

print(perfectNumber(99))

































import requests
from bs4 import BeautifulSoup

# number = input('Give me a Number :- ')


def webLink(userRankNumber):
    if userRankNumber >= 50:
        rankNumber = (userRankNumber // 50) * 50

        return print(rankNumber)
    else:
        rankNumber = 50
        return print(50)

# print(webLink(49))


# https://myanimelist.net/topanime.php    (1-50)
# https://myanimelist.net/topanime.php?limit=50 (51-100)

# for x in range(10):
#     anime = mal.Anime(x)
#     print(anime.title)













# webLink(int(input('Import number:- ')))

















