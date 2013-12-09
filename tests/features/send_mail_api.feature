Feature: Send Mail API Form
  In order to learn the API for sending mail
  As a customer
  I want a web-based form that calls the send mail API

Scenario: Fill out all form fields and send mail
  Given I am on the SendGrid API Workshop page
  When I enter my credentials in the login form
    And I open the send mail API form
    And I enter valid values in all the fields of the send mail API form
    And I click on the Try It button on the send mail API form
  Then the send mail API form should display a "success" response
  

 