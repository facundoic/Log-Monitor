import re
import time
import os

file = open('/var/lib/docker/containers/b124597d22dd3508029ee5a394244ff9e1899a510d99ae65f09d9ced5b20034f/b124597d22dd3508029ee5a394244ff9e1899a510d99ae65f09d9ced5b20034f-json.log', 'r')
pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'



def main():
    global result
    while True:
        with open("/home/ec2-user/Project/Logs/ip.txt", 'r+') as result:
            for line in file:
                if len(result.readlines()) < 20:
                    print("I\'am Working!")
                    print(result.readlines())
                    line_split = line.split(':')[1]
                    ip = re.findall(pattern, line_split)

                    if len(ip) != 0:
                        result.write(str(ip[0]))
                else:
                    print("The file is complete!")
                    file.close()
                    result.close()
                    continue        
if __name__ == '__main__':
   main()
