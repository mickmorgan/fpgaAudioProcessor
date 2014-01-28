# FPGA_Client v.1.0
# Michael Morgan
# A program to communicate with FPGA via UART, send and receive audio data

import time
import struct
import serial
import wave
import sys
import array
from Tkinter import Tk
from tkFileDialog import askopenfilename

# Prompt user to browse for file
try:
    Tk().withdraw()
    filename = askopenfilename()
    f = wave.open(filename, 'r')
except IOError:
    print "Exiting program..."
    sys.exit(0)
except:
    print "Unexpected file type"
    print "Exiting program..."
    sys.exit(0)
    
# Output file details to user
print "Details of selected file:", filename, "\n"
time.sleep(1)
print "Number of channels: ", f.getnchannels()
print "Sampling Rate: ", f.getframerate(), "Hz"
print "Sample width: ", f.getsampwidth(), "byte(s)"
print "Compression type: ", f.getcompname(), "\n"

# Perform file compatibilty checks 
if f.getnchannels() != 1:
    print "Invalid selection: file must be mono"
    print "Exiting program..."
    sys.exit(0)
##if f.getframerate() != 8000:
##    print "Invalid selection: file must have sampling rate of 8000 Hz"
##    print "Exiting program..."
    sys.exit(0)
if f.getsampwidth() != 1:
    print "Invalid selection: file must be 8 bit PCM"
    print "Exiting program..."
    sys.exit(0)
if f.getcompname() != "not compressed":
    print "Invalid selection: file must be uncompressed"
    print "Exiting program..."

# Create array to contain audio data
numOfFrames = f.getnframes()
fData = []
RTS_Data = []
procData = []

# Fill array with data
for i in xrange (0, numOfFrames):
    f.setpos(i)
    fData.insert(i,f.readframes(1))

f.close()

# print samples in binary format:
# samples stored as little endian unsigned bytes (interpreted as ASCII if printed directly) in fData
# struct.unpack() converts this to a tuple containing the value of that byte as an integer
# format() takes the 0th element of that tuple (an integer) and converts it to a binary byte with the format code "08b"
#for j in xrange (0, numOfFrames):
#    RTS_Data.insert(j, format(struct.unpack('B', fData[j])[0], "08b"))

# Initialise serial port
ser = serial.Serial('COM7', 115200)
print "Outgoing serial port:", ser.name, "\n"
#serIn = serial.Serial('COM12', 9600)

# Pipe out audio samples on serOut, receive processed samples on serIn
print "Transmitting audio data to FPGA device...\n"
for i in xrange (0, numOfFrames):
#    ser.write(RTS_Data[i])
    ser.write(fData[i])
#    procData.insert(i, ser.read(8))
    print i, "of", numOfFrames
print "\n File transfer successful!\n"
ser.close()
#serIn.close()

# Initializse incoming serial port
#serIn = serial.Serial('COM12', 9600)
#print "Incoming serial port:", serIn.name, "\n"
#serIn.close()

# Store incoming processed samples in procData
#for i in xrange (0, 1000):
#    procData.insert(ser.read(8))
#    print i
#print "Done"
#ser.close()




