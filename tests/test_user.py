"""Tests for ``facebook.user``."""

from nose.tools import *
from mock import patch, Mock as mock
from facepy import GraphAPI

import facebook
from facebook import User

@patch.object(GraphAPI, 'get')
def test_get(mock):
    mock.return_value = {
        'username': 'johannesgorset',
        'first_name': 'Johannes',
        'last_name': 'Gorset',
        'name': 'Johannes Gorset',
        'locale': 'en_GB',
        'gender': 'male',
        'link': 'http://facebook.com/johannesgorset',
        'id': '586052336'
    }

    user = User('johannes.gorset')

    user.load()

    mock.assert_called_with('johannes.gorset')

    assert_equal(user.username, 'johannesgorset')
    assert_equal(user.first_name, 'Johannes')
    assert_equal(user.last_name, 'Gorset')
    assert_equal(user.name, 'Johannes Gorset')
    assert_equal(user.locale, 'en_GB')
    assert_equal(user.gender, 'male')
    assert_equal(user.link, 'http://facebook.com/johannesgorset')
    assert_equal(user.facebook_id, 586052336)

@patch.object(GraphAPI, 'get')
def test_permissions(mock):
    mock.return_value = {
        'data': [
            {
                'user_location': 1,
                'user_relationships': 1
            }
        ]
    }

    with facebook.session('<token>') as session:
        user = session.User('johannes.gorset')

        permissions = user.permissions

        mock.assert_called_with('johannes.gorset/permissions')
        
        assert_in('user_location', permissions)
        assert_in('user_relationships', permissions)
