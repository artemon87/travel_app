## travel_app
   WEB API with Flask

## Domain:
   Trip Calculator
## Interface:
   Web Api (using Flask)

# Note
   All data is included (no ignores, even virtualenv was pushed)

# Set-up:
   Please activate virtual env (inside travel_app home directory type 'source trip/bin/activate') or create your own one.
   If creating own virtual env please install dependencies listed under req.txt ('pip install -r req.txt')

# Deployment:
   To run an app, type 'python app.py'

# Tests:
   Tests are included under app_resources folder. To run simply type 'pytest' (this will look for any files starting with 'test_' keyword and run them, thus you dont have to be inside app_resource dir)  

# To Know:
* Only GET and POST methods are supported by /v1/calculate api endpoint
* POST method will do all the hard work (calculations) and return the result
* GET method will only read and return the previously saved result from the json file
* API Endpoint **only accepts** payload data with 'travelers' keyword; thus, it expects dictionary of a dictionary, see Sample below
* Access port is 8005
* Full API: http://0.0.0.0:8005/v1/calculate

# Python Sample:
    import requests
    import json
    
    payload = {}
    payload['travelers'] = {}
    payload['travelers']['Artem'] = [30,1,3]
    payload['travelers']['Max'] = [20,10,10]
    payload['travelers']['Nyk'] = [14]
    payload['travelers']['Tata'] = [30,6]
    payload['travelers']['Ly1'] = [70,4]
    url = 'http://0.0.0.0:8005/v1/calculate'
    headers = {'Content-Type' : 'application/json'}
    
    res = requests.post(url, headers = headers, data = json.dumps(payload))
    res.json()
    

