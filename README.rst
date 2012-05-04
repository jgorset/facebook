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
    with facebook.session(oauth_token) as session:
        user = session.User('johannes.gorset')

        user.permissions    # => ['user_location', 'user_relationships']
        user.friends        # => [<Facebook User>, <Facebook User>, <Facebook User>, ...]

Disclaimer
----------

I'm not nearly done yet.

Installation
------------

::

    $ pip install facebook

I love you
----------

Johannes Gorset made this. You should `tweet me <http://twitter.com/jgorset>`_ if you can't get it
to work. In fact, you should tweet me anyway.
