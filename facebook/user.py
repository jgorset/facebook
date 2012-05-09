import entity

from .descriptors import Integer, String, List, Date, Boolean, Entity
from .page import Page

class User(entity.Entity):
    """User instances represent Facebook users."""

    class Education(entity.Entity):
        """Education instances represent a user's education."""

        school        = Page('school')
        year          = Page('year')
        concentration = List('concentration', Page)
        type          = String('type')

    facebook_id = Integer('id')
    username    = String('username')
    first_name  = String('first_name')
    last_name   = String('last_name')
    name        = String('name')
    locale      = String('locale')
    gender      = String('gender')
    link        = String('link')
    languages   = List('languages', Page)
    timezone    = Integer('timezone')
    updated_at  = Date('updated_time', '%Y-%m-%dT%H:%M:%S+0000')
    is_verified = Boolean('verified')
    bio         = String('bio')
    birthday    = Date('birthday', '%m/%d/%Y')
    education   = List('education', Education)

    @property
    def permissions(self):
        response = self.graph.get('%s/permissions' % self.id)
        return map(lambda x: x[0], response['data'][0].items()) 
