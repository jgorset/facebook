Facebook
========

About
-----

Facebook makes it even easier to interact with Facebook's Graph API.

Usage
-----

::

    import facebook 

    # Query Facebook anonymously
    user = facebook.User('johannes.gorset')

    user.facebook_id    # => 586052336
    user.first_name     # => 'Johannes'
    user.last_name      # => 'Gorset'
    user.name           # => 'Johannes Gorset'
    user.link           # => 'http://facebook.com/johannesgorset'

    # Query Facebook on behalf of a user
    user = facebook.User('johannes.gorset', oauth_token = oauth_token)

    user.permissions        # => ['user_location', 'user_relationships']
    user.friends            # => [<User #586052345>, <User #556022345>, <User #586252349>, ...]
    user.friends[0].name    # => "John Doe"
    user.friends[0].link    # => "http://facebook.com/john.doe"

Disclaimer
----------

I'm not nearly done yet, and I probably never will be.

Installation
------------

::

    $ pip install facebook

I love you
----------

Johannes Gorset made this. You should `tweet me <http://twitter.com/jgorset>`_ if you can't get it
to work. In fact, you should tweet me anyway.
