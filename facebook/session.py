"""
facebook.session
~~~~~~~~~~~~~~~~

This module provides a Session object to manage and persist settings across
queries to the Facebook API.
"""

from .user import Entity, User

class Session(object):
    """A Facebook session."""

    def __init__(self, oauth_token=None):
        self.oauth_token = oauth_token

    def User(self, *args, **kwargs):
        kwargs['oauth_token'] = self.oauth_token

        return User(*args, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

def session(*args, **kwargs):
    """Returns a :class:`Session` for context management."""
    return Session(*args, **kwargs)
