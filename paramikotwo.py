with open("simpletext.txt", "r") as file:
    data = file.readlines()
    for line in data:
        print(line.split())

# string = "192.168.1.12 root soelapyaehtun"
# print(string.strip())
# print(string.split())
# print(string)