from datetime import datetime

import entity

from .descriptors import Integer, String, Date, Boolean, Entity
from .page import Page
from .structure import Structure
from .employment import Employment

class User(entity.Entity):
    """User instances represent Facebook users."""

    username = String('username')
    """The user's Facebook username."""

    first_name = String('first_name')
    """The user's first name."""

    middle_name = String('middle_name')
    """The user's middle name."""

    last_name = String('last_name')
    """The user's last name."""

    name = String('name')
    """The user's full name."""

    locale = String('locale')
    """The user's locale."""

    gender = String('gender')
    """The user's gender."""

    link = String('link')
    """The URL of the profile for the user on Facebook."""

    timezone = Integer('timezone')
    """The user's timezone offset from UTC."""

    updated_at = Date('updated_time', '%Y-%m-%dT%H:%M:%S+0000')
    """The last time the user's profile was updated."""

    is_verified = Boolean('verified')
    """The user's account verification status."""

    bio = String('bio')
    """The user's biography."""

    birthday = Date('birthday', '%m/%d/%Y')
    """The user's birthday."""

    email = String('email')
    """The proxied or contact email address granted by the user."""

    hometown = Entity('hometown', Page)
    """The user's hometown."""

    location = Entity('location', Page)
    """The user's current city."""

    political_view = String('political')
    """The user's political view."""

    quotes = String('quotes')
    """The user's favorite quotes."""

    relationship_status = String('relationship_status')
    """
    The user's relationship status:

    Single, In a relationship, Engaged, Married, It's complicated, In an open relationship,
    Widowed, Separated, Divorced, In a civil union, In a domestic partnership
    """

    religion = String('religion')
    """The user's religion."""

    significant_other = Entity('significant_other', Page)
    """The user's significant other."""

    website = String('website')
    """The URL of the user's personal website."""

    @property
    def work(self):
        """
        A list of :class:`Employment` instances describing the user's work history.

        Each structure has attributes ``employer``, ``position``, ``started_at`` and ``ended_at``.

        ``employer`` and ``position`` reference ``Page`` instances, while ``started_at`` and ``ended_at``
        are datetime objects.
        """
        employments = []

        for work in self.cache['work']:
            employment = Employment(
                employer = work.get('employer'),
                position = work.get('position'),
                started_at = work.get('start_date'),
                ended_at = work.get('end_date')
            )

            employments.append(employment)

        return employments

    @property
    def languages(self):
        """
        A list of strings describing the user's languages.
        """
        languages = []

        for language in self.cache['languages']:
            language = Structure(
                id = language['id'],
                name = language['name']
            )

            languages.append(language)

        return languages

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
        A list of strings describing permissions.

        See Facebook's exhaustive `Permissions Reference <http://developers.facebook.com/docs/authentication/permissions/>`_
        for a list of available permissions.
        """
        response = self.graph.get('%s/permissions' % self.id)

        permissions = []
        for permission, state in response['data'][0].items():
            permissions.append(permission)
        
        return permissions

    @property
    def accounts(self):
        """
        A list of structures describing apps and pages owned by this user.
        """
        response = self.graph.get('%s/accounts' % self.id)

        accounts = []
        for item in response['data']:
            account = Structure(
                page = Page(
                    id = item['id'],
                    name = item['name'],
                    category = item['category']
                ),
                access_token = item['access_token'],
                permissions = item['perms']
            )

            accounts.append(account)

        return accounts
