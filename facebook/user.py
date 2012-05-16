import entity

from .descriptors import Integer, String, List, Date, Boolean, Entity
from .page import Page
from .structure import Structure

class User(entity.Entity):
    """User instances represent Facebook users."""

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
    email       = String('email')

    @property
    def education(self):
        """
        Return a list of structures describing the user's education history.

        Each structure has attributes ``school``, ``year`` and optionally ``concentration``,
        which reference ``Page`` instances. There may also be an attribute ``type`` which is simply
        a string that describes the education level.
        """
        educations = []

        for education in self.cache['education']:
            school        = Page(**education.get('school'))
            year          = Page(**education.get('year'))
            type          = education.get('type')
            
            if 'concentration' in education:
                concentration = Page(**education.get('concentration'))
            else:
                concentration = False

            education = Structure(
                school = school,
                year = year,
                concentration = concentration,
                type = type
            )

            educations.append(education)

        return educations

    @property
    def permissions(self):
        """
        Return a list of strings describing permissions.

        See Facebook's exhaustive `Permissions Reference <http://developers.facebook.com/docs/authentication/permissions/>`_
        for a list of available permissions.
        """
        response = self.graph.get('%s/permissions' % self.id)

        permissions = []
        for permission, state in response['data'][0].items():
            permissions.append(permission)
        
        return permissions
