"""Orange Basket feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from project.oranges import OrangeBasket

# Note to make correction: correct path
@scenario('../features/oranges.feature', 'Add oranges to a basket')
def test_add_oranges_to_a_basket():
    """Add oranges to a basket."""

# Note to make correction: add target fixture
# Note: fixture ---> to use same object for multiple places
@given('the basket has 2 oranges', target_fixture='basket')
def the_basket_has_2_oranges():
    return OrangeBasket(initial_count=2)  # returns object of the basket

# Note to make correction: change acorin
@when('4 oranges are added to the masket')
def oranges_are_added_to_the_masket(basket):  # Note: basket is object which is already defined  above 
    basket.add(4)

@then('the basket contains 6 oranges')
def the_basket_contains_6_oranges(basket):
    assert basket.count == 6

