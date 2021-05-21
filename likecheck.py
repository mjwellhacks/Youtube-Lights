import requests
import json
import time
from gpiozero import LED #Libray Used For GPIO Control On Raspberry Pi
led = LED(2)
last = -1
key = "" #Youtube API Key
vidid= "dQw4w9WgXcQ" #ID For Youtube Video 
while True:
    response = requests.get("https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+vidid+"&key="+key) #Querys Youtubes API To Get Video Rating Data
    results=response.json()
    if int(results["items"][0]["statistics"]["likeCount"])>last: #Checks If The Video Has More Likes Than The Last Time The Loop Repeated
        print(results["items"][0]["statistics"]["likeCount"]) #Prints The Amount Of Likes
        led.on() #Turns On The Lights
        time.sleep(1) #Waits One Second
        led.off() #Turns Off The Lights
    last = int(results["items"][0]["statistics"]["likeCount"]) #Stores The Current Like Count To Compare The Next Time The Loop Runs
    time.sleep(2) #Waits Two Seconds Before Requerying Youtube
