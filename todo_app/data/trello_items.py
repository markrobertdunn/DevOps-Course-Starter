from flask import session
import os
import requests
import json


from dotenv import load_dotenv


load_dotenv()

sessionenv = {
    "secret":os.environ.get('SECRET_KEY'),
    "token":os.environ.get('TOKEN'),
    "board":os.environ.get('BOARD_ID')
}
sessioncred = "?key="+sessionenv["secret"]+"&token="+sessionenv["token"]

def get_cards():
    cards_url = "https://api.trello.com/1/boards/"+sessionenv["board"]+"/cards"+sessioncred
    card = requests.request(
        "GET",
        cards_url
   )
    cards = card.json()
    return cards

def get_card_id(card_id):
    card_id_url = "https://api.trello.com/1/boards/"+sessionenv["board"]+"/cards/"+card_id+sessioncred
    response = requests.request(
        "GET",
        card_id_url
    )
    return response.copy

def add_card(card_title,card_description):
    url = "https://api.trello.com/1/cards"+sessioncred

    headers = {
    "Accept": "application/json"
    }

    query = {
    'idList': os.environ.get('TO_DO'),
    'name': card_title,
    'desc': card_description
    }

    response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
    )
    print(response.text)


def update_card(card_id,card_status):
    url = "https://api.trello.com/1/cards/"+card_id+sessioncred

    headers = {
    "Accept": "application/json"
    }

    response = requests.request(
    "PUT",
    url,
    headers=headers
    )

