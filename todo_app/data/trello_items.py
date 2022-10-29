from flask import session
import os
import requests
import json
import pymongo
import pprint



def loadenv ():
    return [] 
    global sessionenv
    sessionenv = {
        "secret":os.environ.get('SECRET_KEY'),
        "token":os.environ.get('TOKEN'),
        "board":os.environ.get('BOARD_ID')
        }
    global sessioncred
    sessioncred = "?key="+sessionenv["secret"]+"&token="+sessionenv["token"]

def get_cards():
    client = pymongo.MongoClient(os.environ.get('ConnectionString'))
    db = client['test-database']
    collection = db.test_collection
    items=[]
    for documents in collection.find():
            items.append(documents)

    return items



def get_card_id(card_id):
    return []


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

    post_id = collection.insert_one(query).inserted_id


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
