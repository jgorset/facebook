import entity

from .descriptors import Integer, String, List, Date, Boolean, Entity
from .page import Page
from .structure import Structure

class User(entity.Entity):
    """User instances represent Facebook users."""

    username      = String('username')
    first_name    = String('first_name')
    last_name     = String('last_name')
    name          = String('name')
    locale        = String('locale')
    gender        = String('gender')
    link          = String('link')
    languages     = List('languages', Page)
    timezone      = Integer('timezone')
    updated_at    = Date('updated_time', '%Y-%m-%dT%H:%M:%S+0000')
    is_verified   = Boolean('verified')
    bio           = String('bio')
    birthday      = Date('birthday', '%m/%d/%Y')
    email         = String('email')
    hometown      = Entity('hometown', Page)

    @property
    def interested_in(self):
        """
        A list of strings describing the genders the user is interested in.
        """
        genders = []

        for gender in self.cache['interested_in']:
            genders.append(gender)

        return genders

    @property
    def education(self):
        """
        A list of structures describing the user's education history.

        Each structure has attributes ``school``, ``year``, ``concentration`` and ``type``.

        ``school``, ``year`` reference ``Page`` instances, while ``concentration`` is a list of ``Page``
        instances. ``type`` is just a string that describes the education level.

        .. note:: ``concentration`` may be ``False`` if the user has not specified his/her
                  concentration for the given school.
        """
        educations = []

        for education in self.cache['education']:
            school        = Page(**education.get('school'))
            year          = Page(**education.get('year'))
            type          = education.get('type')
            
            if 'concentration' in education:
                concentration = map(lambda c: Page(**c), education.get('concentration'))
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
