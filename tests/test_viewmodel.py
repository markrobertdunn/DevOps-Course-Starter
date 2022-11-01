from todo_app.data.viewmodel import Viewmodel
from todo_app.data.trello_items import Item
import pytest, os
from dotenv import load_dotenv, find_dotenv

@pytest.fixture
def item_list():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    item1 = Item("1","Test Item","Test Description",None,"To-Do")
    item2 = Item("2","Another Test Item","AnotherTest Description",None,"Doing")
    item3 = Item("3","Yet Another Test Item","Yet AnotherTest Description",None,"Done")
    itemlist = [item1,item2,item3]
    return itemlist

def test_return_todo(item_list):
    myviewmodel = Viewmodel(item_list)
    result = myviewmodel.todoitems()
    assert result == [item_list[0]]

def test_return_doing(item_list):
    myviewmodel = Viewmodel(item_list)
    result = myviewmodel.doingitems()
    assert result == [item_list[1]]

def test_return_done(item_list):
    myviewmodel = Viewmodel(item_list)
    result = myviewmodel.doneitems()
    assert result == [item_list[2]]