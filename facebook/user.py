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

    @property
    def education(self):
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
        response = self.graph.get('%s/permissions' % self.id)
        return map(lambda x: x[0], response['data'][0].items()) 
