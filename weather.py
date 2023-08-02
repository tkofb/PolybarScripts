import requests

# def celsiusToFahrenheit(num):
#     convertedNum = (num*1.8) + 32
#     return convertedNum

params = { 
    'zip': '21801',
    'appid': '68454091de219371a75b27123462f4d0',
    'units': 'imperial'
}

request = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params = params)

try: 
    if request.status_code == 200:
        currentTemp = int(request.json()['main']["feels_like"])
        returnString = f"{currentTemp}°F"
        print(returnString)
       
except:
   
    print("0")
    


