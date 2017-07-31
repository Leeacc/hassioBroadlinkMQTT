#!/usr/bin/python
import paho.mqtt.client as mqtt
import sys
import datetime
import subprocess
import broadlink

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

def ac16():
    print str(datetime.datetime.now()).split('.')[0] , "- off"
    subprocess.call("python BlackBeanControl.py -c temp16")
def ac17():
    print str(datetime.datetime.now()).split('.')[0] , "- 17"
    subprocess.call("python BlackBeanControl.py -c temp17")
def ac18():
    print str(datetime.datetime.now()).split('.')[0] , "- 18"
    subprocess.call("python BlackBeanControl.py -c temp18")
def ac19():
    print str(datetime.datetime.now()).split('.')[0] , "- 19"
    subprocess.call("python BlackBeanControl.py -c temp19")
def ac20():
    print str(datetime.datetime.now()).split('.')[0] , "- 20"
    subprocess.call("python BlackBeanControl.py -c temp20")
def ac21():
    print str(datetime.datetime.now()).split('.')[0] , "- 21"
    subprocess.call("python BlackBeanControl.py -c temp21")
def ac22():
    print str(datetime.datetime.now()).split('.')[0] , "- 22"
    subprocess.call("python BlackBeanControl.py -c temp22")
def ac23():
    print str(datetime.datetime.now()).split('.')[0] , "- 23"
    subprocess.call("python BlackBeanControl.py -c temp23")
def ac24():
    print str(datetime.datetime.now()).split('.')[0] , "- 24"
    subprocess.call("python BlackBeanControl.py -c temp24")
def ac25():
    print str(datetime.datetime.now()).split('.')[0] , "- 25"
    subprocess.call("python BlackBeanControl.py -c temp25")
def ac26():
    print str(datetime.datetime.now()).split('.')[0] , "- 26"
    subprocess.call("python BlackBeanControl.py -c temp26")
def ac27():
    print str(datetime.datetime.now()).split('.')[0] , "- 27"
    subprocess.call("python BlackBeanControl.py -c temp27")
def ac28():
    print str(datetime.datetime.now()).split('.')[0] , "- 28"
    subprocess.call("python BlackBeanControl.py -c temp28")
def ac29():
    print str(datetime.datetime.now()).split('.')[0] , "- 29"
    subprocess.call("python BlackBeanControl.py -c temp29")
def ac30():
    print str(datetime.datetime.now()).split('.')[0] , "- 30"
    subprocess.call("python BlackBeanControl.py -c temp30")

options = {16 : ac16,
           17 : ac17,
           18 : ac18,
           19 : ac19,
           20 : ac20,
           21 : ac21,
           22 : ac22,
           23 : ac23,
           24 : ac24,
           25 : ac25,
           26 : ac26,
           27 : ac27,
           28 : ac28,
           29 : ac29,
           30 : ac30
}


## subscribe a topic
def on_connect(client, userdata, flags, rc):
    client.subscribe("bedroom/ac")

def on_message(client, userdata, msg):
    try:
        options[int(msg.payload)]()
    except ValueError:
        print "[{msg}] - Only nubers here".format(msg = str(msg.payload.rstrip()))
client = mqtt.Client()
client.on_connect = on_connect
client.connect("10.10.10.10", 1883, 60)
client.on_message = on_message
client.loop_forever()