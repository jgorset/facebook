class Structure(object):
    """Structures represent anonymous objects in the Facebook API (e.g. a user's education history)."""

    def __init__(self, **attributes):
        self.__dict__.update(attributes)

    def __repr__(self):
        return '<%s>' % self.__class__.__name__
