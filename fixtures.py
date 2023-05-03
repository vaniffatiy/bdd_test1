import pytest
from behave import fixture


@fixture
def search_query():
    return "Weather today"


