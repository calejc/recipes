from flask import request, render_template
from app.module import parsee
import json
from app.ingredient_phrase_tagger.bin import parse_ingredients

from app import app



@app.route('/api', methods=['POST'])
def api():
    url = request.get_json()['url']
    return parsee(url).__dict__ if parsee(url) else "Unable to parse recipe"

@app.route('/api/v2', methods=['POST'])
def apiv2():
    url = request.form['url']
    return parsee(url).__dict__ if parsee(url) else "Unable to parse recipe"

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")