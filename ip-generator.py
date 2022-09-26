import time
from random import seed
from random import choice
from random import random
ipList=["95.214.235.205","71.6.232.7","135.125.244.48","209.222.252.91","143.198.51.242","20.249.209.60","94.102.61.10","61.0.14.134"]
seed(1)
# log example:
# {"log":"185.216.71.242 - - [05/Sep/2022:08:14:48 +0000] \"GET / HTTP/1.1\" 200 45\n","stream":"stdout","time":"2022-09-05T08:14:48.657937253Z"}
try:
    
        while(1):
            randValue = random()
            scaledValue = 0.1 + (randValue * (1.5 - 0.1))
            print(scaledValue)
            time.sleep(scaledValue)
            namedTuple = time.localtime() # get struct_time
            timeString = time.strftime("%d/%b/%Y:%H:%M:%S", namedTuple)
            otherTimeString = time.strftime("%Y-%m-%dT%H:%M:%SZ", namedTuple)
            logToAppend='{"log":"' + choice(ipList) + ' - - [' + timeString + ' +0000] \\"GET / HTTP1.1\\" 200 45\\n","stream":"stdout","time":"' + otherTimeString + '"}'
            with open("./b124597d22dd3508029ee5a394244ff9e1899a510d99ae65f09d9ced5b20034f-json.log","a") as file1:
                file1.write(logToAppend + '\n')
            #print(logToAppend)                             
except:
    print("Bad path to log file please review in code")


