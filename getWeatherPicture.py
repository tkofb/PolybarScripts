import requests


params = { 
    'zip': '21801',
    'appid': '68454091de219371a75b27123462f4d0',
    'units': 'imperial'
}

symbol = "" #Cloud

try:
    request = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params = params)
except:
     print("",end="")

symbol = "" #Cloud

try: 
   if request.status_code == 200:
        currentDescription = request.json()['weather'][0]['main']
        currentWeatherID = str(request.json()['weather'][0]['id'])[0]
        
        if currentDescription == 'Thunderstorm':
            symbol = '' #Thunderstorm
        
        if currentDescription == 'Drizzle' or currentDescription == 'Rain':
            symbol = '' #Rain
        
        if currentDescription == 'Snow':
            symbol = '' #Snow
            
        if currentDescription == 'Fog' or currentWeatherID == "7":
            symbol = '󰖑' #Fog
        
        if currentDescription == 'Clear':
            symbol = '' #Sun
            
        print(symbol)
except:
    print(symbol)