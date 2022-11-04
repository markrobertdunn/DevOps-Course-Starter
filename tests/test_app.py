
import pytest
import mongomock
import pymongo
import os
from todo_app import app
from dotenv import load_dotenv, find_dotenv

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_index_page(client):
    query = {
        '_id' : "635be25a7e52bb441c9a87c9",
        'status': "To-Do",
        'name': "card_title",
        'desc': "card_description",
        'due': None
        }
    db_client = pymongo.MongoClient(os.environ.get('CONNECTIONSTRING'))
    db = db_client['test-database']
    collection = db.test_collection
    collection.insert_one(query)
    # Make a request to our app's index page
    response = client.get('/')

    assert response.status_code == 200
    assert 'card_title' in response.data.decode()