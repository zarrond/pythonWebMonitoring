import requests
import os
from datetime import datetime as d
import time

def get(url):
    response = None
    try:
        response = requests.get(url)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Oops: Something Else",err)
    return response


dirr = os.path.dirname(os.path.realpath(__file__))

print(dirr)
while True:
    with open(dirr + r"\data.txt", "a") as f:
        response = get('http://api.ipify.org/')
        if(response is not None):
            s = response.text
            f.write(s + " : " + d.now().strftime("%d/%m/%Y at %H:%M:%S") +"\n")
    time.sleep(10)


