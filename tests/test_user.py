# encoding: utf-8

"""Tests for ``facebook.user``."""

from datetime import datetime
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
        ],
        'timezone': 2,
        'updated_time': '2012-05-09T18:03:44+0000',
        'verified': True,
        'bio': '<bio>',
        'birthday': '09/15/1988',
        'education': [
            {
                'school': {
                    'id': '111989298827775',
                    'name': 'Vinstra vidaregåande skule'
                },
                'year': {
                    'id': '140617569303679',
                    'name': '2007'
                },
                'type': 'High school'
            },
            {
                'school': {
                    'id': '107952312571140',
                    'name': 'Westerdals School of Communication'
                },
                'year': {
                    'id': '136328419721520',
                    'name': '2009'
                },
                'concentration': {
                    'id': '109803049037749',
                    'name': 'Graphic Design'
                },
                'type': 'College',
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
    assert_equal(2, user.timezone)
    assert_equal(datetime(2012, 5, 9, 18, 3, 44), user.updated_at)
    assert_equal(True, user.is_verified)
    assert_equal('<bio>', user.bio)
    assert_equal(datetime(1988, 9, 15, 0, 0), user.birthday)
    assert_equal('Norwegian', user.languages[0].name)
    assert_equal('Vinstra vidaregåande skule', user.education[0].school.name)
    assert_equal('jgorset@gmail.com', user.email)

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
