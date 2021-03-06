"""
The network client is started by the UI client
application.
The network client looks for a file called recording.
When it finds this file, it sends it to the server.
It than deletes the file.
"""

#Libraries
import socket
import sys
import os
import pyglet
import time

'''
#Variables
verbose = True
recordingName = "recording.wav"
recordingExists = os.path.exists(recordingName)
HOST = "104.155.13.116" #This is the Google Cloud compute engine VM instance IP
PORT = 5555
MAX_SIZE = 2048
SAVED = "SAVED"
GoogleCloudServer = (HOST,PORT)
clientSocket = socket.socket() #This is a default, TCP socket

#Script
if verbose: print("Starting connection.")
clientSocket.connect(GoogleCloudServer)
if verbose: print("Looking for recording.")

while not recordingExists:
    recordingExists = os.path.exists(recordingName)

if verbose: print("Recording found. Sending recording size to server.")
recordingSize = os.path.getsize(recordingName) #First, send the file size
clientSocket.send(str(recordingSize).encode())
if verbose: print("Rrecording size:",recordingSize)

if verbose: print("Recording size sent. Sending entire recording to server for processing.")
recording=open (recordingName,"rb") #Open a stream to the recording
partialRecording = recording.read(MAX_SIZE) #1024 bytes out of the whole recording

totalSent = 0
while partialRecording:
    clientSocket.send(partialRecording)
    totalSent = totalSent + len(partialRecording)
    if verbose: print("Sent",totalSent,"out of",recordingSize)
    partialRecording = recording.read(MAX_SIZE)

if verbose: print("Recording sent. Waiting for confirmation.")
confirmation = clientSocket.recv(MAX_SIZE)
confirmation = confirmation.decode()
if verbose: print("Decoded confirmation:",confirmation)
while confirmation != SAVED:
    pass
if verbose: print("Confirmation received. Deleting recording.")
os.remove(recordingName)
if verbose: print("Recording deleted. Closing socket.")
clientSocket.close()
if verbose: print("Socket closed.")
'''

"""
New Client
"""

HOST = "" #This is the Google Cloud compute engine VM instance IP
PORT = 5555
MAX_SIZE = 4096

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSocket.bind((HOST,PORT))

while True:
    print("Receiving.")
    music = pyglet.resource.media( clientSocket.recv(MAX_SIZE) )
    print("Playing.")
    music.play()
    print("Sleeping.")
    time.sleep(5)
    
pyglet.app.run()
