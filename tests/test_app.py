
import pytest
import mongomock
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


class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

# Stub replacement for requests.get(url)
def stub(method,url):

    fake_response_data = None
    query = [{
            '_id': '123abc',
            'name': 'My fake card',
            'status': 'To-Do',
            'desc' : 'some description',
            'due' : None
        }]

    fake_response_data = query
    return StubResponse(fake_response_data)



def test_index_page(client):
    document = {
        '_id' : "635be25a7e52bb441c9a87c9",
        'status': "To-Do",
        'name': "card_title",
        'desc': "card_description"
        }
    collection = mongomock.MongoClient().db.collection
    collection.insert_one(document)
    # Make a request to our app's index page
    response = client.get('/')

    assert response.status_code == 200
#    assert 'card_title' in response.data.decode()