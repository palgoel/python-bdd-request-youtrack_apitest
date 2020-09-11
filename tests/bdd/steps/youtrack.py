from behave import *
import requests
from config.test_run_config import *
use_step_matcher("re")

@Given('user is logged in youtrack')
def step_impl(context):
    pass



@step('json response is retrieved with list of projects')
def step_impl(context):
    context.response = context.s.get(URL)
    print("list of projects =", context.response.json())

@then('verify that status code returned is "(.*)"')
def step_impl(context,code):
    print ("Status code =",context.response.status_code)
    assert context.response.status_code == int(code), "Response code is different: %s" % context.response.status_code + \
                                               "   Error: " + str(context.response.content)

@step('user should be able to add an issue to "(.*)"')
def step_impl(context,project_id):
    endpoint = 'https://apitesting.myjetbrains.com/youtrack/api/issues'
    json ={
                  # "project": {"id": project_id},
                  "project": {"id": "0-1"},
                  "summary": "Created one more issue using Docker image by maintaining session object!",
                  "description": "Created  one more issue using Docker image by maintaining session object."
          }
    resp = context.s.post(endpoint, json=json)
    resp_json = resp.json()
    print("created issue json =", resp_json)

@Given('new user is logged in youtrack')
def step_impl(context):
    context.s = requests.Session()
    context.s.auth = ('ApiUser', 'ApiUser') # user is changed from what is defined in test_run_config
    context.s.get(URL) #can give any URL rom what is defined in test_run_config

