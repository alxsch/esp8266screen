import gc
from umqtt.simple import MQTTClient
import ubinascii
import esp
import simplehttp
import uos, machine, network
import helloworld

esp.osdebug(None)
gc.collect()
helloworld.hello_screen()
simplehttp.main()


ssid = ''
passwd = ''
mqtt_server = ''
mqtt_user = b''
mqtt_pass = b''
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'tele/office-temp1/SENSOR'

last_msg = 0
msg_interval = 10
counter = 0

sta = network.WLAN(network.STA_IF)

sta.active(True)
sta.connect(ssid, passwd)

while sta.isconnected() is False:
    pass
