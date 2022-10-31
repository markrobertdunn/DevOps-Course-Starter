from flask import session
import os
import requests
import json
import pymongo
import pprint





def get_cards():
    client = pymongo.MongoClient(os.environ.get('ConnectionString'))
    db = client['test-database']
    collection = db.test_collection
    items=[]
    returned_items=[]
    for document in collection.find():
            items.append(document)
    

    for item in items:
        my_item=Item(item["_id"],item["name"],item["desc"],item["due"],item["status"])
        returned_items.append(my_item)
    return returned_items


def add_card(card_title,card_description,due_date):

    client = pymongo.MongoClient(os.environ.get('ConnectionString'))
    db = client['test-database']
    collection = db.test_collection
    query = {
    'status': "To-Do",
    'name': card_title,
    'desc': card_description,
    'due':due_date
    }

    collection.insert_one(query)


def update_card(card_id,idList):
    url = "https://api.trello.com/1/cards/"+card_id+sessioncred

    headers = {
    "Accept": "application/json"
    }

    query = {
    'idList': idList
    }
    response = requests.request(
    "PUT",
    url,
    headers=headers,
    params=query
    )
    print(response.text)

class Item:
    def __init__(self, _id, name, desc, due, status):
        self.id = _id
        self.name = name
        self.desc = desc
        self.due = due
        self.status = status
