import requests


params = { 
    'access_key': '3735019f0d3687983087e3b0c04e9d38',
    'query': 'Salisbury, Maryland'
}


def celsiusToFahrenheit(num):
    convertedNum = (num*1.8) + 32
    return convertedNum

request = requests.get(url="http://api.weatherstack.com/current", params = params)


try: 
    if request.status_code == 200:
        currentTemp = request.json()['current']["temperature"]
        currentTemp = int(celsiusToFahrenheit(currentTemp))
        returnString = f"{currentTemp}°F"
        print(returnString)
       
except:
    print("0")
    


