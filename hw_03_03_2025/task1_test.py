import pytest 
from task1 import User, UserManager

def test_add_user():
    user_manager = UserManager()
    assert user_manager.add_user('John', 'superpsina@hotmail.com', 42) == ['John', 'superpsina@hotmail.com', 42]
    assert user_manager.add_user('John', 'superpsina@hotmail.com', 42) == 'Пользователь с таким email существует'

def test_del_user():
    user_manager = UserManager()
    user_manager.add_user('John', 'superpsina@hotmail.com', 42)
    assert user_manager.del_user(0) == []
    assert user_manager.del_user(0) == IndexError

def test_search_by_email():
    user_manager = UserManager()
    user_manager.add_user('John', 'superpsina@hotmail.com', 42)
    assert user_manager.search_by_email('superpsina@hotmail.com') == 'Такой email существует'
    assert user_manager.del_user('not_email') == 'Такого email нету' 