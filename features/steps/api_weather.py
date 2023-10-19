import requests
from behave import given, when, then

url = "https://weatherapi-com.p.rapidapi.com/current.json"
headers = {
    "X-RapidAPI-Key": "fa131aaf22msh8f4db4b9f53fdedp191f2fjsnd82916167abb",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}


@given('the user wants to get current weather information')
def step_given_user_wants_weather_info(context):
    pass


@when('the user makes a request with latitude {latitude} and longitude {longitude}')
def step_when_user_makes_request(context, latitude, longitude):
    latitude_strip = latitude.strip('"')
    longitude_strip = longitude.strip('"')

    context.querystring = {'q':  f'{latitude_strip}, {longitude_strip}'}
    context.response = requests.get(url, headers=headers, params=context.querystring)
    context.weather_data = context.response.json()


@then('the response should contain the location information')
def step_then_response_should_contain_location_info(context):
    location_data = context.weather_data.get('location')
    assert location_data is not None
    assert location_data['country'] == context.table[0]['country']
    assert location_data['region'] == context.table[0]['region']
