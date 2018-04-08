import pytest
import requests
import json
from . import resource_helpers 
from . import travelers 
from . import resources

def prep():
    m1 = travelers.Member('Artem', [20,13,23.98])
    m2 = travelers.Member('Max', [7,23,14.65,8.43])
    m3 = travelers.Member('Nyk', [11.80,12,9])
    m4 = travelers.Member('Tata', [20,4,6.90])
    m5 = travelers.Member('Ly', [24,50])
    return [m1, m2, m3, m4, m5]

def test_most_spent_order():
    arr = prep()
    arr = resource_helpers.get_most_spent_order(arr)
    assert isinstance(arr, list)
    assert len(arr) is 5
    assert arr[0].name is 'Ly'
    assert arr[len(arr) -1].name is 'Tata'

def test_get_total_spent():
    arr = prep()
    total = resource_helpers.get_total_spent(arr)
    assert isinstance(total, float) or isinstance(total, int)
    assert total > 0

def test_disbursement_helper():
    arr = prep()
    total = resource_helpers.get_total_spent(arr)
    result = resource_helpers.disbursement_helper(arr, total / 5)
    assert isinstance(result, bool)

def test_pay_back_to():
    arr = prep()
    average = resource_helpers.get_total_spent(arr) / 5
    result = resource_helpers.pay_back_to(arr, arr[2], average, 7)
    assert isinstance(result, int)

def test_disbursement():
    arr = prep()
    result = resource_helpers.disbursement(arr)
    assert isinstance(result, dict)
    assert result == {'Ly': {'owns to': {}}, 
                      'Artem': {'owns to': {}}, 
                      'Max': {'owns to': {}}, 
                      'Nyk': {'owns to': {'Ly': 16.75}}, 
                      'Tata': {'owns to': {'Ly': 7.7, 'Artem': 7.43, 'Max': 3.53}}}

def prep_payload():
    payload = {}
    payload['travelers'] = {}
    payload['travelers']['Artem'] = [30, 30]
    payload['travelers']['Max'] = [25, 20]
    payload['travelers']['Nyk'] = [5, 5]
    payload['travelers']['Tata'] = [1, 4]
    payload['travelers']['Ly'] = [2, 3]
    payload['travelers']['Ly'] = [2, 3]
    return payload

def test_api_normal():
    url = 'http://0.0.0.0:8005/v1/calculate'
    headers = {'Content-Type' : 'application/json'}
    payload = prep_payload()

    res = requests.post(url, headers = headers, data = json.dumps(payload))
    assert res.json()['status'] == 'success'

def test_api_missing_json():
    url = 'http://0.0.0.0:8005/v1/calculate'
    payload = prep_payload()

    res = requests.post(url, data = json.dumps(payload))
    assert res.json()['message'] == 'content is not in json format'

def test_api_invalid_content():
    url = 'http://0.0.0.0:8005/v1/calculate'
    headers = {'Content-Type' : 'application/json'}
    payload = {}
    payload['traveler'] = {}
    payload['traveler']['Artem'] = [30, 30]

    res = requests.post(url, headers = headers, data = json.dumps(payload))
    assert res.json()['message'] == "missing traveler's data"


