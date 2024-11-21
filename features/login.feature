Feature: Login functionality
  As a user
  I want to login to the application
  So that I can create a contract

  Scenario: Successful login with valid credentials
    Given James is on the login page
    When he enters his credentials
      | username | password |
      | Admin     | admin123  |
    And he should see the dashboard
    Then create a contract
      | name | firstName |  Middle_Name | last_name | email | phone | Keywords | notes |
      | Geovanni     | geo  | jose | Quinntero| geo@geo.com|676282| java, js, python| QA test automation GeQuintero |
      And create a contract
      | resume_path  |
      | resume.pdf   |
    
