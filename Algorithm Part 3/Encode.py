"""
Navn                        SDU Brugernavn
Marcus Møller Pedersen      marpe18
Jakob Schledermann Winkel   jwink18
Alban Dalifi                aldal18
"""
import sys
import bitIO
from Element import Element
import PQHeap

def HUFFMAN(C):
    n = len(C)
    Q = []
    
    #inserts elements into Q
    for i in range(n):
        e1 = Element(C[i].key, [i])
        PQHeap.insert(Q, e1)

    #Steps to build the tree from pseudocode
    for i in range(n - 1):
        x = PQHeap.extractMin(Q)
        y = PQHeap.extractMin(Q)
        freq = x.key + y.key
        element = Element(freq, [x.data, y.data])
        PQHeap.insert(Q, element)

    return Q


#Creates the codeList with the Huffman algorithm and in order
def codeList(asciiList):
    codeList = []
    for n in range(len(asciiList)): codeList.append(0)
    huffmanTree = HUFFMAN(asciiList)
    string = ""
    OrderedTraversal(huffmanTree[0].data, string, codeList)

    return codeList

#Method used for ordering the codeList
def OrderedTraversal(byte, bitstring, codeList):
    #recursive method used for cycling through the given list's values inorder 
    if len(byte) > 1: 
        OrderedTraversal(byte[0], bitstring + "0", codeList)
        OrderedTraversal(byte[1], bitstring + "1", codeList)
    elif len(byte) == 1 and len(bitstring) != 0:
        codeList[byte[0]] = bitstring


if __name__ == "__main__":
    infile = open(sys.argv[1], 'rb')
    asciiList = []
    #Sets up the asciiList with 0 frequency on all elements
    for x in range(256): asciiList.append(Element(0, x))

    #Reads bytes and adds the frequency to list
    byte = infile.read(1)
    while byte:
        asciiList[ord(byte)].key += 1
        byte = infile.read(1)

    #sets ordered codeList
    codeList = codeList(asciiList)

    newinfile = open(sys.argv[1], "rb")
    outfile = open(sys.argv[2], "wb")
    bitstreamout = bitIO.BitWriter(outfile)

    #Writes frequencies
    for i in range(len(asciiList)): bitstreamout.writeint32bits(asciiList[i].key)

    #Writes the bits from the codeList
    byte = newinfile.read(1)
    while byte:
        bits = codeList[int.from_bytes(byte, "little")]
        for bit in bits: bitstreamout.writebit(int(bit))
        byte = newinfile.read(1)

    bitstreamout.close()
    print("Done")
    