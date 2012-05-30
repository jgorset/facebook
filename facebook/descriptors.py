from datetime import datetime

from .exceptions import PermissionDenied

class Descriptor(object):

    def __init__(self, attribute):
        """
        Create a new descriptor.

        :param attribute: A string describing the name of the attribute in Facebook's Graph API.
        """
        self.attribute = attribute

    def __get__(self, instance, owner):
        try:
            return instance.cache[self.attribute]
        except:
            raise PermissionDenied('You do not have permission to load %s for this entity' % self.attribute)

class String(Descriptor):

    def __get__(self, instance, owner):
        return str(super(String, self).__get__(instance, owner))

class Integer(Descriptor):

    def __get__(self, instance, owner):
        return int(super(Integer, self).__get__(instance, owner))

class Boolean(Descriptor):

    def __get__(self, instance, owner):
        return bool(super(Boolean, self).__get__(instance, owner))

class Date(Descriptor):

    def __init__(self, attribute, format):
        """
        Create a new descriptor.

        :param attribute: A string describing the name of the attribute in Facebook's Graph API.
        :param format: A strptime-compatible string describing the format of the date.
        """
        self.attribute = attribute
        self.format = format

    def __get__(self, instance, owner):
        return datetime.strptime(super(Date, self).__get__(instance, owner), self.format)

class Entity(Descriptor):

    def __init__(self, attribute, cls):
        """
        Create a new descriptor.

        :param attribute: A string describing the name of the attribute in Facebook's Graph API.
        :param cls: A type describing the class that the entity will be initialized from.
        """
        self.attribute = attribute
        self.cls = cls

    def __get__(self, instance, owner):
        data = super(Entity, self).__get__(instance, owner)

        return self.cls(oauth_token = instance.oauth_token, **data)
