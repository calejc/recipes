import requests, json
from bs4 import BeautifulSoup
from app.models import Schema, Recipe, Ingredient
from app.ingredient_phrase_tagger.bin.parse_ingredients import run as parse_ingredients


def parsee(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    with requests.Session() as session:
        session.headers = headers
        try:
            r = session.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            recipe = Recipe(Schema([json.loads(str(s.string)) for s in soup.find_all("script", {'type' : "application/ld+json"})]).target_schema)
            parsed = json.loads(parse_ingredients(recipe.fullStringIngredients))
            recipe.ingredients = [Ingredient(i).__dict__ for i in parsed]
            return recipe
        except:
            return None
