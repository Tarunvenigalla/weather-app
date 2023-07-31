import requests

def weather(city,api_key):
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response=requests.get(url)
    data=response.json()
    if data['cod']!=404:
        main_data=data['main']
        weather_data=data['weather'][0]
        weather_description=weather_data['description']
        temperature_data=main_data['temp']
        humidity_data=main_data['humidity']
        
        print(f'weather in {city}:{weather_description}')
        print(f'Temperature:{int(temperature_data-273.15)}°C')
        print(f'Hunidity:{humidity_data}%')
    else:
        print('City not found...')

if __name__=='__main__':
    api_key=('ce9259e1b5be0bd1d89fc9a1ffde119e')
    city=input('Enter City:')
    weather(city,api_key)