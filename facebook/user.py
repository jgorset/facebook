from entity import Entity

from descriptors import Integer, String

class User(Entity):
    """User instances represent Facebook users."""

    facebook_id = Integer('id')
    username    = String('username')
    first_name  = String('first_name')
    last_name   = String('last_name')
    name        = String('name')
    locale      = String('locale')
    gender      = String('gender')
    link        = String('link')

    @property
    def permissions(self):
        response = self.graph.get('%s/permissions' % self.id)
        return map(lambda x: x[0], response['data'][0].items())
