# Saving to file goes in here.

def start(data):
    with open('saves.txt','r') as saves:
        data = saves.read()
