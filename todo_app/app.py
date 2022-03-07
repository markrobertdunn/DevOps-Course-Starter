from flask import Flask, render_template, request
from werkzeug.utils import redirect #added render template to the import
from todo_app.data.session_items import get_items, add_item #added import of functions from session_items
from todo_app.data.trello_items import get_cards, add_card #added import of functions from session_items
import requests, os

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    trello = get_cards()
    return render_template('index.html', cards = trello, to_do = os.environ.get('TO_DO'), doing = os.environ.get('DOING'), done=os.environ.get('DONE'))#updated the return to load index.html

@app.route('/add', methods=["POST"])#new route for the post
def add():
    add_card(request.form.get('item'), request.form.get('description'), request.form.get('due'))
    return redirect('/')
