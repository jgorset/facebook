from nose.tools import *

def assert_instance_of(expected, actual, msg=None):
    """Verify that object is an instance of expected """
    assert isinstance(actual, expected), msg

def assert_not_instance_of(expected, actual, msg=None):
    """Verify that object is not an instance of expected """
    assert not isinstance(actual, expected, msg)

def assert_none(actual, msg=None):
    """Verify that item is None"""
    assert_equal(None, actual, msg)

def assert_not_none(actual, msg=None):
    """Verify that item is None"""
    assert_not_equal(None, actual, msg)

def assert_match(pattern, string, msg=None):
    """Verify that the pattern matches the string"""
    assert_not_none(re.search(pattern, string), msg)

def assert_not_match(pattern, string, msg=None):
    """Verify that the pattern does not match the string"""
    assert_none(re.search(pattern, string), msg)
