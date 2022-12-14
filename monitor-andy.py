# this is a test for git
import re
import time
import os
from  dotenv import load_dotenv

load_dotenv('./.env')
# file = open('/var/lib/docker/containers/b124597d22dd3508029ee5a394244ff9e1899a510d99ae65f09d9ced5b20034f/b124597d22dd3508029ee5a394244ff9e1899a510d99ae65f09d9ced5b20034f-json.log', 'r')

file = open(os.getenv('LOG-FILE'), 'r')
print(len(file))
pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'


# with open("/home/ec2-user/Project/Logs/ip.txt", 'r+') as result:
with open("./ip.txt", 'w') as result:
    for line in file:
        # print("I\'am Working!")
        # print(len(result.readlines()))
        line_split = line.split(':')[1]
        ip = re.findall(pattern, line_split)

        if len(ip) != 0:
            result.write(str(ip[0]) + "\n")
            
    
    print("The file is complete!")
    file.close()