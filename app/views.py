from flask import request, render_template
from app.module import parse
import json

from app import app



@app.route('/api', methods=['POST'])
def api():
    url = request.get_json()['url']
    return parse(url).__dict__ if parse(url) else "Unable to parse recipe"

@app.route('/api/v2', methods=['POST'])
def apiv2():
    url = request.form['url']
    return parse(url).__dict__ if parse(url) else "Unable to parse recipe"


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")