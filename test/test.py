import requests
from time import sleep

data = {
  'temp' : 70,
  'humd' : 5,
  'pressure' : 1000
}

print("Sending data...")
r = requests.put('http://127.0.0.1', data = data)
print("Data sent")

sleep(0.5)

print("Status code: ", r.status_code)
