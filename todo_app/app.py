from flask import Flask, render_template, request
from werkzeug.utils import redirect #added render template to the import
from todo_app.data.session_items import get_items, add_item #added import of functions from session_items
from todo_app.data.trello_items import get_cards, add_card, update_card, loadenv #added import of functions from session_items
import requests, os

from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    loadenv()
    


    @app.route('/')
    def index():
        trello = get_cards()
        return render_template('index.html', cards = trello, to_do = os.environ.get('TO_DO'), doing = os.environ.get('DOING'), done=os.environ.get('DONE'))#updated the return to load index.html

    @app.route('/add', methods=["POST"])#new route for the post
    def add():
        add_card(request.form.get('item'), request.form.get('description'), request.form.get('due'))
        return redirect('/')

    @app.route('/todo', methods=["POST"])
    def update_todo():
        update_card(request.form.get('id'), os.environ.get('TO_DO'))
        return redirect('/')

    @app.route('/done', methods=["POST"])
    def update_done():
        update_card(request.form.get('id'), os.environ.get('DONE'))
        return redirect('/')

    @app.route('/doing', methods=["POST"])
    def update_doing():
        update_card(request.form.get('id'), os.environ.get('DOING'))
        return redirect('/')
    return app