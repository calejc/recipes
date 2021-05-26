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
            recipe = set_ingredients(recipe)
            return recipe
        except Exception as e:
            print(e)
            return None


def set_ingredients(recipe):
    ingredient_strings = [i for i in recipe.ingredients]
    try:
        parsed = json.loads(parse_ingredients(ingredient_strings))
        recipe.ingredients = [set_ingredient(i) for i in parsed]
        return recipe
    except Exception as e:
        try:
            recipe.ingredients = [setIngredient({'name': s, 'input': s}) for s in ingredient_strings]
            return recipe
        except Exception as ex:
            print(ex)
            recipe.ingredients = ingredient_strings
            return recipe

def set_ingredient(schema):
    try:
        return Ingredient(schema).__dict__
    except Exception as e:
        return schema
