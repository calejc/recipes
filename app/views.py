from flask import request, render_template
from app.module import parse
from app.models import *
import json

from app import app



@app.route('/api', methods=['POST'])
def api():
    url = request.form['url']
    return parse(url).__dict__ if parse(url) else "Unable to parse recipe"



@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")