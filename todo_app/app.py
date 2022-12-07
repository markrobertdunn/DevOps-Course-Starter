from flask import Flask, render_template, request
from werkzeug.utils import redirect #added render template to the import
from todo_app.data.database_items import get_cards, add_card, update_card #added import of functions from session_items
from todo_app.data.viewmodel import Viewmodel
import os

from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        trello = get_cards()
        return render_template('index.html', view_model=Viewmodel(trello))#updated the return to load index.html

    @app.route('/add', methods=["POST"])#new route for the post
    def add():
        add_card(request.form.get('item'), request.form.get('description'), request.form.get('due'))
        return redirect('/')

    @app.route('/todo', methods=["POST"])
    def update_todo():
        update_card(request.form.get('id'), "To-Do")
        return redirect('/')

    @app.route('/done', methods=["POST"])
    def update_done():
        update_card(request.form.get('id'), "Done")
        return redirect('/')

    @app.route('/doing', methods=["POST"])
    def update_doing():
        update_card(request.form.get('id'), "Doing")
        return redirect('/')
    return app