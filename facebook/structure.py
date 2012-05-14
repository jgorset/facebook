class Structure(object):
    """Structures represent anonymous objects in the Facebook API (e.g. a user's education history)."""

    def __init__(self, **attributes):
        self.__dict__.update(attributes)
