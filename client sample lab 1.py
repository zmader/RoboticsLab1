import socket
from time import *

# CONFIGURATION PARAMETERS
IP_ADDRESS = "raspberrypi-1.local" 	# SET THIS TO THE RASPBERRY PI's IP ADDRESS
CONTROLLER_PORT = 5001
TIMEOUT = 10				# If its unable to connect after 10 seconds, give up. 
                                        # Want this to be a while so robot can initialize.

# connect to the motorcontroller
sock = socket.create_connection( (IP_ADDRESS, CONTROLLER_PORT), TIMEOUT)

""" The t command tests the robot.  It should beep after connecting, move forward 
slightly, then beep on a sucessful disconnect."""
#sock.sendall("t /dev/tty.usbserial-DA01NYDH")			# send a command
#print(sock.recv(128))        # always recieve to confirm that your command was processed

""" The i command will initialize the robot.  It enters the create into FULL mode which
 means it can drive off tables and over steps: be careful!"""
sock.sendall("i /dev/ttyUSB0".encode())
print(sock.recv(128).decode())

"""
    Arbitrary commands look like this 
        a *
    Whatever text is given where the * is, is given to the Create API in the form
        result = robot.*
    then any result will be send back.  If there is no result the command will be echoed.
    
    You can see the possible commands here:
    https://bitbucket.org/lemoneer/irobot
    
    You may wish to extend the control_server.py on the raspberry pi.
"""

sock.sendall("a drive_straight(100)".encode())
print(sock.recv(128).decode())

sleep(2)

sock.sendall("a distance".encode())
print("It has traveled this far: ",sock.recv(128).decode())


""" The c command stops the robot and disconnects.  The stop command will also reset 
the Create's mode to a battery safe PASSIVE.  It is very important to use this command!"""
sock.sendall("c".encode())
print(sock.recv(128).decode())

sock.close()

