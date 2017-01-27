import thingspeak
from time import sleep

data = {
    'field1' : '70'
}

channel = thingspeak.Channel('219319', 'api_key', 'write_api_key')

while True:
    channel.update(data)
    sleep(20)
