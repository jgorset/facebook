"""Tests for ``facebook.page``."""

from mock import patch, Mock as mock
from facepy import GraphAPI

import facebook
from facebook import Entity, User, Page

from .asserts import *

@patch.object(GraphAPI, 'get')
def test_get(mock):
    mock.return_value = {
        'id': '107381149291932',
        'name': 'Norwegian language',
        'picture': '<url>',
        'likes': '15775',
        'category': 'Interest',
        'is_published': True,
        'is_community_page': True,
        'description': '<description>',
        'talking_about_count': 110
    }

    page = Page('107381149291932')

    assert_equal(107381149291932, page.facebook_id)
    assert_equal('Norwegian language', page.name)
    assert_equal('<url>', page.picture)
    assert_equal(15775, page.likes)
    assert_equal('Interest', page.category)
    assert_equal(True, page.is_published)
    assert_equal(True, page.is_community_page)
    assert_equal('<description>', page.description)
    assert_equal(110, page.talking_about_count)

    mock.assert_called_with('107381149291932')
