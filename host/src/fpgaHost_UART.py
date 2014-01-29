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

# Initialise serial port
ser = serial.Serial('COM11', 115200)
print "Outgoing serial port:", ser.name, "\n"

# Pipe out audio samples on serial port
print "Transmitting audio data to FPGA device...\n"
for i in xrange (0, numOfFrames):
    ser.write(fData[i])
print "File transfer successful!\n"

# Attempt read from serial port
print "Reading from serial port"
for i in xrange (0, numOfFrames):
    procData.insert(i, ser.read(8))
print "Done"
ser.close()




