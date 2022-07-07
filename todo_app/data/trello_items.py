from flask import session
import os
import requests
import json



def loadenv ():
    global sessionenv
    sessionenv = {
        "secret":os.environ.get('SECRET_KEY'),
        "token":os.environ.get('TOKEN'),
        "board":os.environ.get('BOARD_ID')
        }
    global sessioncred
    sessioncred = "?key="+sessionenv["secret"]+"&token="+sessionenv["token"]

def get_cards():
    cards_url = "https://api.trello.com/1/boards/"+sessionenv["board"]+"/cards"+sessioncred
    card = requests.request(
        "GET",
        cards_url
   )
    cards = card.json()
    items=[]
    for card in cards:
        item=Item(card["id"],card["name"],card["desc"], card["due"], card["idList"])
        items.append(item)
    return items


def get_card_id(card_id):
    card_id_url = "https://api.trello.com/1/boards/"+sessionenv["board"]+"/cards/"+card_id+sessioncred
    item = requests.request(
        "GET",
        card_id_url
    )
    item = Item.from_trello_card.json()
    return item

def add_card(card_title,card_description,due_date):
    url = "https://api.trello.com/1/cards"+sessioncred  

    headers = {
    "Accept": "application/json"
    }

    query = {
    'idList': os.environ.get('TO_DO'),
    'name': card_title,
    'desc': card_description,
    'due':due_date
    }

    response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
    )
    print(response.text)


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
    def __init__(self, id, name, desc, due, idList):
        self.id = id
        self.name = name
        self.desc = desc
        self.due = due
        self.idList = idList
