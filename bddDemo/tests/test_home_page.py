"""Home Page feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from requests_html import HTMLSession

@scenario('../features/home_page.feature', 'Hello Message')
def test_hello_message():
    """Hello Message."""


@given('user visits home page', target_fixture='res')
def user_visits_home_page():
    """user visits home page."""
    ses = HTMLSession()
    res = ses.get('http://localhost:5000')
    return res


@then('the response status should be 200')
def the_response_status_should_be_200(res):
    """the response status should be 200."""
    assert 200 == res.status_code
    


@then('user should see hello message')
def user_should_see_hello_message(res):
    """user should see hello message."""
    #testing whether hello is present in page

    assert 'hello' in res.text
    

