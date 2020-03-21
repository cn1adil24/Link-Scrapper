from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

visited = set()

def get_links(url, limit):
    
    if len(visited) >= limit:
        return links
    
    links = []
    
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    url=response.url

    for link in soup.find_all('a'):
        link_url = link.get('href')

        if link_url is not None and (link_url.startswith('http') or link_url.startswith('https')):
            if link_url not in visited:
                links.append(link_url)
        
        if link_url is not None and link_url.startswith('/'):
            base = url
            links.append(urljoin(base, link_url))

    return links



def get_all_links(url):
    if url not in visited:
        visited.add(url)
        for link in get_links(url):
            get_all_links(link)
    


url = 'https://en.wikipedia.org/wiki/Main_Page'
limit = 100

get_all_links(url, limit)

for link in visited:
    print(link)