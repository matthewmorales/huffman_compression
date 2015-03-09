import random
import string
import sys

x = 0;

def create():
    print('Generating ascii.txt') 

    name = 'ascii.txt'  # Name of text file coerced with +.txt

    try:
        file = open(name,'wb')   # Trying to create a new file or open one
        for x in range(0, 1000000):
			file.write(random.choice(string.ascii_lowercase))
        file.close()
        
    except:
        print('File Creation Failed')
        sys.exit(0) # quit Python

create()

	