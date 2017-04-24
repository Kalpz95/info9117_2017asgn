# Created by whwong at 21/4/17
Feature: Login Page

  Scenario: Login
    When a user visits the login page
    Then she should see the username field
    And she should see the password field
    And she should see the login button

  Scenario: Login Success
    When a user visits the login page
    And she logs in with username "test" and password "test123"
    Then she should see a message of "Login successful"

  Scenario: Login Failure
    When a user visits the login page
    And she logs in with username "baduser" and password "badpasswd"
    Then she should see a message of "Login failed"

   Scenario: Logout
     Given a user visits the login page
     And she sees the Logout link
     When she clicks on the Logout link
     Then she returns to the site
     And she sees a message telling "You logged out"



