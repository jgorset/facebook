from datetime import datetime

class Descriptor(object):

    def __init__(self, attribute):
        """
        Create a new descriptor.

        :param attribute: A string describing the name of the attribute in Facebook's Graph API.
        """
        self.attribute = attribute

    def __get__(self, instance, owner):
        return instance.cache.get(self.attribute)

class String(Descriptor):

    def __get__(self, instance, owner):
        data = super(String, self).__get__(instance, owner)

        if data:
            return str(data)
        else:
            return data

class Integer(Descriptor):

    def __get__(self, instance, owner):
        data = super(Integer, self).__get__(instance, owner)

        if data:
            return int(data)
        else:
            return data

class Boolean(Descriptor):

    def __get__(self, instance, owner):
        data = super(Boolean, self).__get__(instance, owner)

        if data:
            return bool(data)
        else:
            return data

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
        data = super(Date, self).__get__(instance, owner)

        if data:
            return datetime.strptime(data, self.format)
        else:
            return data

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

        if data:
            return self.cls(oauth_token = instance.oauth_token, **data)
        else:
            return None
