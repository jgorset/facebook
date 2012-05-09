"""Tests for ``facebook.user``."""

from mock import patch, Mock as mock
from facepy import GraphAPI

import facebook
from facebook import Entity, User, Page

from .asserts import *

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
        'id': '586052336',
        'languages': [
            {
                'id': '107381149291932',
                'name': 'Norwegian'
            },
            {
                'id': '106059522759137',
                'name': 'English'
            }
        ]
    }

    user = User('johannes.gorset')

    assert_equal('johannesgorset', user.username)
    assert_equal('Johannes', user.first_name)
    assert_equal('Gorset', user.last_name)
    assert_equal('Johannes Gorset', user.name)
    assert_equal('en_GB', user.locale)
    assert_equal('male', user.gender)
    assert_equal('http://facebook.com/johannesgorset', user.link)
    assert_equal(586052336, user.facebook_id)
    assert_instance_of(Page, user.languages[0])

    mock.assert_called_with('johannes.gorset')

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
