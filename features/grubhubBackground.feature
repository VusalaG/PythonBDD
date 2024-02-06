Feature: Main page functions

   Background: Common steps
     Given I launch edge browser
     When I open grubhub home page
     And Click on Sign In button
     And Enter username "gadirlivusala@gmail.com " and password "Timetoeat"
     And Click on login button


  Scenario:  Login to grubhub with valid parameters
     Then User must successfully land on main page

  Scenario: Navigate to Account
     And Click profile button
     And Click on Payment button
     Then Your Account page should be displayed

  Scenario: Navigate to Help option
     And Click profile button
     And CLick on Help button
     Then Help page should be displayed
