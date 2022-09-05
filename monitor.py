import re

file = open('/var/lib/docker/containers/b124597d22dd3508029ee5a394244ff9e1899a510d99ae65f09d9ced5b20034f/b124597d22dd3508029ee5a394244ff9e1899a510d99ae65f09d9ced5b20034f-json.log', 'r')
pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
result = open("/home/ec2-user/Proyect/Logs/ip.txt", 'w')

def main():
    for line in file:
        line_split = line.split(':')[1]
        ip = re.findall(pattern, line_split)
        
        result.write(str(ip[0]))

    file.close()
    result.close()

if __name__ == '__main__':
    main()