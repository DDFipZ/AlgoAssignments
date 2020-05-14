import sys
import bitIO
import Encode

infile = open(sys.argv[1], "rb")
outfile = open(sys.argv[2], "wb")
bistreamin = bitIO.BitReader(infile)

#Regenerates a frequency list
freqList = []
for i in range(256):
    freq = bistreamin.readint32bits()
    freqList.append(freq)

#Regenerates the codes
codeList = Encode.codeList(freqList)