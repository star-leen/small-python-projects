import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
votes = soup.select('.score')

def creat_custom_hn(link_list, vote_list):
    hn = []
    for idx, item in enumerate(link_list):
        title = link_list[idx].getText()
        link = link_list[idx].get('href', None)
        points = int(vote_list[idx].getText().replace(' points', ''))
        print(points)
        hn.append({'title': title, 'link': link})
    return(hn)
    
creat_custom_hn(links, votes)

