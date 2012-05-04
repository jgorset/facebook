from facepy import GraphAPI

class Entity(object):
    """Entities are the base class for anything on Facebook."""

    oauth_token = None
    """A string describing an OAuth token."""

    def __init__(self, id, oauth_token=None):
        """
        Get the entity with the given id.

        :param id: An integer or string describing the Facebook id of the entity.
        :param oauth_token: A string describing an OAuth token.
        """
        self.oauth_token = oauth_token
        self.id = id

    def load(self):
        self.response = self.graph.get('%s' % self.id)

    @property
    def graph(self):
        return GraphAPI(self.oauth_token)

    def __getattr__(self, missing_attribute):
        for attribute, key, parser in self.attributes:
            if attribute == missing_attribute:
                if not hasattr(self, 'response'):
                    self.load()

                return parser(self.response[key])
