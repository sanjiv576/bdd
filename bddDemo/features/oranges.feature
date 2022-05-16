Feature: Orange Basket
    # user stories
    As a farmer
    I want to carry oranges in a Basket
    so that I will be able to carry large number of oranges

# To test above user story, so we need test secnario (also known as BDD)---> contains Given When Then
# fist scenario test
Scenario Outline: Add oranges to a basket

    Given the basket has <start> oranges
    When <more> oranges are added to the basket
    Then the basket contains <final> oranges

    Examples:
        | start | more | final |
        | 5  | 4  | 9 |
        | 5  | 3  | 8 |
        | 5  | 1  | 6 |
        | 5  | 2  | 7 |



Scenario Outline: Remove oranges from the basket

    Given the basket has <start> oranges
    When <more> oranges are removed from the basket
    Then the basket contains <final> oranges

    Examples:
        | start | more | final |
        | 4 | 3 | 1 |