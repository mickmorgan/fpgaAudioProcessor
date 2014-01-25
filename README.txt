This project is a configurable audio processing module implemented digitally on an FPGA. Audio is configured on a PC using a client written in Python, sent via USB to an external FPGA for processing and returned to the PC for file reassembly and playback.

The software currently supports the processing of mono, 8000Hz .wav files - but support for higher quality audio will be added upon successful operation of the software.

This repo contains two pieces of software: 

- A PC-based client written in Python, which will be compiled into an executable using py2exe when fully operational;

- A Xilinx ISE project containing source VHDL and bitstream files targeted for the Digilent Atlys (Xilinx Spartan-6)   

This project is currently in development as part of an Electrical Engineering FYP in NUI Galway, Ireland. For more information, please contact me at m.morgan4@nuigalway.ie.