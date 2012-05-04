from entity import Entity

class User(Entity):
    """User instances represent Facebook users."""

    attributes = [
        ('facebook_id', 'id', int),
        ('username', 'username', str),
        ('first_name', 'first_name', str),
        ('last_name', 'last_name', str),
        ('name', 'name', str),
        ('locale', 'locale', str),
        ('gender', 'gender', str),
        ('link', 'link', str)
    ]

    @property
    def permissions(self):
        response = self.graph.get('%s/permissions' % self.id)
        return map(lambda x: x[0], response['data'][0].items())
