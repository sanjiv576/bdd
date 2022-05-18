Feature: Home Page
# user story
    As a web user,
    I want to see hello message on the home page
    so that I feel welcomed to the site.

Scenario: Hello Message
    Given user visits home page
    Then user should see hello message
    # 200 means success
    Then the response status should be 200