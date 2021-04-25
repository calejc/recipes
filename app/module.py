import requests, json
from bs4 import BeautifulSoup
from app.models import Schema, Recipe


def parse(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    with requests.Session() as session:
        session.headers = headers
        try:
            r = session.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            return Recipe(Schema([json.loads(str(s.string)) for s in soup.find_all("script", {'type' : "application/ld+json"})]).target_schema)
        except:
            return None
