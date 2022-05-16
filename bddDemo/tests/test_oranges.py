"""Orange Basket feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)

from project.oranges import OrangeBasket

# Note to make correction: correct path
@scenario('../features/oranges.feature', 'Add oranges to a basket')
def test_add_oranges_to_a_basket():
    """Add oranges to a basket."""

@scenario('../features/oranges.feature', 'Remove oranges from the basket')
def test_remove_oranges_to_a_basket():
    """Remove oranges to a basket."""

# Note to make correction: add target fixture
# Note: fixture ---> to use same object for multiple places
@given(parsers.parse('the basket has {start:d} oranges'), target_fixture='basket')
def the_basket_has_2_oranges(start):
    return OrangeBasket(initial_count=start)  # returns object of the basket

# Note to make correction: change acorin
@when(parsers.parse('{more:d} oranges are added to the basket'))
def oranges_are_added_to_the_basket(basket, more):  # Note: basket is object which is already defined  above 
    basket.add(more)


@when(parsers.parse('{more:d} oranges are removed from the basket'))
def oranges_are_removed_to_the_basket(basket, more):  # Note: basket is object which is already defined  above 
    basket.remove(more)

@then(parsers.parse('the basket contains {final:d} oranges'))
def the_basket_contains_6_oranges(basket, final):
    assert basket.count == final

