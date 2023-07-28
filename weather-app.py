import requests
api_key=('ce9259e1b5be0bd1d89fc9a1ffde119e')
city=input('Enter City:')
url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    temp=data['main']['temp']
    temp_ce=temp-273.15
    desc = data['weather'][0]['description']
    print(f"Temperature: {int(temp_ce)}'C")
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
    