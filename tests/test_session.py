"""Tests for ``facebook.session``."""

from nose.tools import *
from mock import patch, Mock as mock
from facepy import GraphAPI

import facebook

@patch.object(GraphAPI, 'get')
def test_session(mock):
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

    oauth_token = 'abcdefghijklmnopqrstuvwxyz'

    with facebook.session(oauth_token) as session:
        user = session.User('johannes.gorset')

        assert_equal(user.oauth_token, oauth_token)

    user = facebook.User('johannes.gorset')
    assert_equal(user.oauth_token, None) 
