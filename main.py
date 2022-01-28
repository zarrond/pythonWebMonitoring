import requests
import os
from datetime import datetime as d
import time

dir = os.path.dirname(__file__)

while True:

    with open(dir + "/data.txt", "a") as f:
        s = requests.get('http://api.ipify.org/').text
        f.write(s + " : " + d.now().strftime("%d/%m/%Y at %H:%M:%S") +"\n")
    
    time.sleep(10)
