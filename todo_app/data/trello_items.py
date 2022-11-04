from flask import session
import os
import pymongo
from bson import ObjectId

def get_cards():
    client = pymongo.MongoClient(os.environ.get('CONNECTIONSTRING'))
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

    client = pymongo.MongoClient(os.environ.get('CONNECTIONSTRING'))
    db = client['test-database']
    collection = db.test_collection
    query = {
    'status': "To-Do",
    'name': card_title,
    'desc': card_description,
    'due':due_date
    }

    collection.insert_one(query)


def update_card(card_id,status):
    client = pymongo.MongoClient(os.environ.get('CONNECTIONSTRING'))
    db = client['test-database']
    collection = db.test_collection

    collection.update_one({'_id': ObjectId(card_id)}, {'$set': {'status':status}})


class Item:
    def __init__(self, _id, name, desc, due, status):
        self.id = _id
        self.name = name
        self.desc = desc
        self.due = due
        self.status = status
