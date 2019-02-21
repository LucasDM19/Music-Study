from __future__ import division #Avoid division problems in Python 2, used in emiteSom3

# Maneira mais didatica
def emiteSom1():
   import pyaudio   # pip install pyaudio
   import numpy as np

   p = pyaudio.PyAudio()

   volume = 1.0     # range [0.0, 1.0]
   fs = 44100       # sampling rate, Hz, must be integer
   duration = 2.0   # in seconds, may be float
   f = 4*261.63        # sine frequency, Hz, may be float

   # generate samples, note conversion to float32 array
   samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

   # for paFloat32 sample values must be in range [-1.0, 1.0]
   stream = p.open(format=pyaudio.paFloat32,
                   channels=1,
                   rate=fs,
                   output=True)

   # play. May repeat with different volume values (if done interactively) 
   stream.write(volume*samples)

   stream.stop_stream()
   stream.close()

   p.terminate()

def emiteSom2():
   import math
   #sudo apt-get install python-pyaudio
   from pyaudio import PyAudio

   #See http://en.wikipedia.org/wiki/Bit_rate#Audio
   BITRATE = 16000 #number of frames per second/frameset.      

   #See http://www.phy.mtu.edu/~suits/notefreqs.html
   FREQUENCY = 261.63 #Hz, waves per second, 261.63=C4-note.
   LENGTH = 3 #1.2232 #seconds to play sound

   NUMBEROFFRAMES = int(BITRATE * LENGTH)
   RESTFRAMES = NUMBEROFFRAMES % BITRATE
   WAVEDATA = ''    

   for x in xrange(NUMBEROFFRAMES):
      WAVEDATA += chr(int(math.sin(x / ((BITRATE / FREQUENCY) / math.pi)) * 127 + 128))    

   #fill remainder of frameset with silence
   for x in xrange(RESTFRAMES): 
       WAVEDATA += chr(128)

   p = PyAudio()
   stream = p.open(
       format=p.get_format_from_width(1),
       channels=1,
       rate=BITRATE,
       output=True,
       )
   stream.write(WAVEDATA)
   stream.stop_stream()
   stream.close()
   p.terminate()

def emiteSom3():
   #from __future__ import division #Avoid division problems in Python 2
   import math
   import pyaudio
   import sys

   PyAudio = pyaudio.PyAudio
   RATE = 16000
   WAVE = 1000
   data = ''.join([chr(int(math.sin(x/((RATE/WAVE)/math.pi))*127+128)) for x in xrange(RATE)])
   p = PyAudio()

   stream = p.open(format =
                   p.get_format_from_width(1),
                   channels = 1,
                   rate = RATE,
                   output = True)
   for DISCARD in xrange(5):
       stream.write(data)
   stream.stop_stream()
   stream.close()
   p.terminate()
   
if __name__ == "__main__":
   emiteSom1()