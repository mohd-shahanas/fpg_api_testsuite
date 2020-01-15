"""Common Assertion methods"""

import requests


def assertion_message(actual, expected, keyword=''):
    """Add more information to the assertion message in case of a failure."""
    return f'Response is {actual}, should {keyword} be {expected}'


def assert_equal(actual, expected):
    assert actual == expected, assertion_message(actual, expected)


def assert_not_equal(actual, expected):
    assert actual != expected, assertion_message(actual, expected,
                                                keyword="not")
