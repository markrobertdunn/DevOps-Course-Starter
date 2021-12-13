from flask import Flask, render_template, request
from werkzeug.utils import redirect #added render template to the import
from todo_app.data.session_items import get_items, add_item #added import of functions from session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items = items)#updated the return to load index.html

@app.route('/add', methods=["POST"])#new route for the post
def add():
    add_item(request.form.get('item'))
    return redirect('/')
