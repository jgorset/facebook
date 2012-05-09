from entity import Entity

from .descriptors import Integer, String, Boolean

class Page(Entity):
    """Page instances represent Facebook pages."""

    facebook_id         = Integer('id')
    name                = String('name')
    picture             = String('picture')
    link                = String('link')
    likes               = Integer('likes')
    category            = String('category')
    is_published        = Boolean('is_published')
    is_community_page   = Boolean('is_community_page')
    description         = String('description')
    talking_about_count = Integer('talking_about_count')
