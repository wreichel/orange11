import json
import requests

response = requests.get('https://api.weatherapi.com/v1/current.json?key=937eb4bc98c44c20a7195358231301&q=Nowy Dwór Mazowiecki&aqi=no')
dane=response.json()

print(dane)