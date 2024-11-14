import requests
import json

url = 'https://gbfs.lyft.com/gbfs/2.3/dca-cabi/en/station_information.json'

response = requests.get(url)
data = response.json()

stations_info = data['data']['stations']

status_url = 'https://gbfs.lyft.com/gbfs/2.3/dca-cabi/en/station_status.json'

status_response = requests.get(status_url)
status_data = status_response.json()
stations_status = status_data['data']['stations']

for station in stations_info:
    station_id = station['station_id']
    capacity = station['capacity']
    name = station['name']
    for station_status in stations_status:
        if station['station_id'] == station_status['station_id']:
            bikes_available = station_status['num_bikes_available']
            print(f"Name: {name}, Station ID: {station_id}, Num Bikes: {bikes_available}, Capacity: {capacity} ")


    
