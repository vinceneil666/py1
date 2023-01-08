import sys
# Saving the reference of the standard output
original_stdout = sys.stdout 	

with open('demo.txt', 'w') as f:
    sys.stdout = f
    print('Hello,')
    print('This message will be written to a file.')
    print('And thats it......')
    sys.stdout = original_stdout 

print('This message will be written to the screen.')