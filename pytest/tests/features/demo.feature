Feature: Demo
    A site which demos the use of pytest-bdd

    Scenario Outline: Login with different credentials
        Given I am on the login page
        When I login with <username> and <password>
        Then I should be in the overview page with correct credentials

        Examples:
            | username   | password   |
            | demoname1  |  password1 |
            | username2  | password2  |
            | logincred3 | P5$$W0RD3  |

    Scenario: Valid number in available credit
        Given I am on the login page
        When I login with demoname1 and password1
        Then I should be in the overview page with correct credentials
        Then I should see the available credit is 17800

    
        
    