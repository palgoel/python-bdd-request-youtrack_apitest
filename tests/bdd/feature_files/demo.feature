# Created by NS4538 at 7/21/2020
Feature:(REST-API) Get from mock rest api a json response
  # Currently the bearer token is for root login


  Scenario: verify the status code
    Given user is logged in youtrack
    When json response is retrieved with list of projects
    Then verify that status code returned is "200"

#    # as of now wrong project id as 0-3 is given when really need to run change project id to 0-0 or 0-1
  Scenario Outline: Create a youtrack issue for particular project based on project assigned
    And user should be able to add an issue to "<project_id>"
   Examples:
  |project_id|
  |0-0       |
  |0-1       |

