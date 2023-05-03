import pytest
from behave import fixture


@pytest.fixture
def search_query():
    return "Weather today"


