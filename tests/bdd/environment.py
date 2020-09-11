import requests
from config.test_run_config import *

def before_feature(context,feature):
    context.s = requests.Session()
    context.s.auth = (USERNAME, PASSWORD)
    resp = context.s.get(URL)
    print (resp.headers)