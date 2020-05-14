"""
Navn                        SDU Brugernavn
Marcus Møller Pedersen      marpe18
Jakob Schledermann Winkel   jwink18
Alban Dalifi                aldal18
"""
import sys
import bitIO
import Encode
from Element import Element

if __name__ == "__main__":

    infile = open(sys.argv[1], "rb")
    outfile = open(sys.argv[2], "wb")
    bitstreamin = bitIO.BitReader(infile)

    #Generates a frequency list
    freqList = []
    for i in range(256):
        freq = bitstreamin.readint32bits()
        freqList.append(Element(freq, i))

    huffmanList = Encode.HUFFMAN(freqList)    

    #First read bit, setting up the while loop to read the rest
    b = bitstreamin.readbit()
    #Creates the currentRoot based off of main root
    currentRoot = huffmanList[0].data
    while True:
        if not bitstreamin.readsucces():
            break
        #Checks if bit is either 1 or 0
        if b == 0:
            currentRoot = currentRoot[0]
        else:
            currentRoot = currentRoot[1]

        #if it hits this if statement, it has found the leaf in the huffman tree
        if not len(currentRoot) > 1:
            outfile.write(bytes([currentRoot[0]]))
            #Resets the currentRoot
            currentRoot = huffmanList[0].data
        #Reads new bit for next runthrough of while loop
        b = bitstreamin.readbit()