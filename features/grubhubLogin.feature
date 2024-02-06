Feature:GrubHub Login

    Scenario: login to grubhub with valid parameters
     Given I launch edge browser
     When I open grubhub home page
     And Click on Sign In button
     And Enter username "gadirlivusala@gmail.com " and password "Timetoeat"
     And Click on login button
     Then User must successfully land on main page


  Scenario Outline: login to grubhub with valid parameters
     Given I launch edge browser
     When I open grubhub home page
     And Click on Sign In button
     And Enter username "<username>" and password "<password>"
     And Click on login button
     Then User must successfully land on main page

     Examples:
       | username                | password |
       | gadirlivusala@gmail.com | Timetoeat|
       | gadirlivusala@gmail.com | password |

