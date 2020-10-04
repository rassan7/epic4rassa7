import requests

def Weather():
    api_address='http://api.openweathermap.org/data/2.5/weather?q=bienhoa&appid=cee343d33e41970dd63c44b39c8620ab'
    # city = input('Enter the City Name :')
    url = api_address 
    json_data = requests.get(url).json()
    format_add = json_data['main']
    print(format_add)
    print("Weather is {0} Temperature is mininum {1} Celcius and maximum is {2} Celcius".format(
        json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
    return format_add