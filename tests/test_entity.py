"""Tests for ``facebook.entity``."""

from nose.tools import *
from mock import patch, Mock as mock
from facepy import GraphAPI

from facebook import Entity

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

    entity = Entity('johannes.gorset')

    entity.load()

    mock.assert_called_with('johannes.gorset')
