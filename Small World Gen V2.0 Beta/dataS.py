# Saving to file goes in here.

def start(data):
    with open('Small World Gen V2.0 Beta\saves.csv','r') as saves:
        data = saves.read()


def save(code):
    print("Hi")
    with open('Small World Gen V2.0 Beta\saves.csv', 'w') as saves:
        saves.write(str(code))
