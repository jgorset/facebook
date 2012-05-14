from facepy import GraphAPI

class Entity(object):
    """Entities are the base class for anything on Facebook."""

    oauth_token = None
    """A string describing an OAuth token."""

    _cache = None
    """Graph API cache for this object."""

    def __init__(self, id, oauth_token=None):
        """
        Get the entity with the given id.

        :param id: An integer or string describing the Facebook id of the entity.
        :param oauth_token: A string describing an OAuth token.
        """
        self.oauth_token = oauth_token
        self.id = id

    @property
    def cache(self):
        """Query or return the Graph API representation of this resource."""
        if not self._cache:
            self._cache = self.graph.get('%s' % self.id)

        return self._cache

    @property
    def graph(self):
        return GraphAPI(self.oauth_token)
