Facebook
========

About
-----

Facebook makes it even easier to interact with Facebook's Graph API.

Usage
-----

::

    import facebook 

    with facebook.session(oauth_token) as session:
        user = session.User('johannes.gorset')

        user.facebook_id    #=> 586052336
        user.first_name     #=> 'Johannes'
        user.last_name      #=> 'Gorset'
        user.name           #=> 'Johannes Gorset'
        user.link           #=> 'http://facebook.com/johannesgorset'
        user.permissions    #=> ['user_location', 'user_relationships']

Installation
------------

::

    $ pip install facebook
