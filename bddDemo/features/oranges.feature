Feature: Orange Basket
    # user stories
    As a farmer
    I want to carry oranges in a Basket
    so that I will be able to carry large number of oranges

# To test above user story, so we need test secnario (also known as BDD)---> contains Given When Then
# fist scenario test
Scenario: Add oranges to a basket

    Given the basket has 2 oranges
    When 4 oranges are added to the masket
    Then the basket contains 6 oranges