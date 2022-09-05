file = open('/var/lib/docker/containers/b124597d22dd3508029ee5a394244ff9e1899a510d99ae65f09d9ced5b20034f/b124597d22dd3508029ee5a394244ff9e1899a510d99ae65f09d9ced5b20034f-json.log', 'r')

def main():
    for line in file:
        line_split = line.split(':')
        print(line_split[1])

    file.close()

if __name__ == '__main__':
    main()