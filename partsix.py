# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and
#  another message when it is destroyed (destructor).

#solution

class Loggar:
    def __init__(self):
        print(" Message Before: Logger object created.") # constuructor message

    def __del__(self):
        print("Message After: Logger object destrutor.")

log = Loggar()
del log
              

