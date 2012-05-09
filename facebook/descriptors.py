class Descriptor(object):
    def __init__(self, attribute):
        """
        Create a new descriptor.

        :param attribute: A string describing the name of the attribute in Facebook's Graph API.
        """
        self.attribute = attribute

    def __get__(self, instance, owner):
        if not instance._cache:
            instance._cache = instance.graph.get('%s' % instance.id)

        return instance._cache[self.attribute]

class String(Descriptor):

    def __get__(self, instance, owner):
        return str(super(String, self).__get__(instance, owner))

class Integer(Descriptor):

    def __get__(self, instance, owner):
        return int(super(Integer, self).__get__(instance, owner))
