# sys module
import sys

#* run the file with following command: 
#* python sys.py red green blue

print(sys.argv) # - ['testing_sys.py', 'red', 'green', 'blue']

# the command line args are - ['testing_sys.py', 'red', 'green', 'blue']

print(len(sys.argv)) #? 4 

print(sys.argv[0]) #? testing_sys.py