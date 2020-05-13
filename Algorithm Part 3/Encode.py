import sys
import bitIO
from Element import Element
import PQHeap

# outfile = open(sys.argv[2], 'wb')
def HUFFMAN(C):
    n = len(C)
    Q = []
    
    for i in range(n):

        e1 = Element(C[i].key, [i])
        PQHeap.insert(Q, e1)

    #Steps to build the tree
    for i in range(n - 1):
        x = PQHeap.extractMin(Q)
        y = PQHeap.extractMin(Q)
        freq = x.key + y.key
        element = Element(freq, [x.data, y.data])
        PQHeap.insert(Q, element)

    return Q


def codeList(asciiList):
    codeList = []
    for n in range(len(asciiList)): codeList.append(0)
    huffmanTree = HUFFMAN(asciiList)
    string = ""
    OrderedTraversal(huffmanTree[0].data, string, codeList)

    return codeList

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
    
    index = 0
    for freq in asciiList:
        index += 1 
        print("index: " + str(index) + " frequency: " + str(freq.key))
    codeList = codeList(asciiList)
    print(codeList)

    newinfile = open(sys.argv[1], "rb")
    outfile = open(sys.argv[2], "wb")
    bitstreamout = bitIO.BitWriter(outfile)

    for i in range(len(asciiList)): bitstreamout.writeint32bits(asciiList[i].key)

    byte = newinfile.read(1)
    while byte:
        bits = codeList[int.from_bytes(byte, "little")]
        for bit in bits: bitstreamout.writebit(int(bit))
        byte = newinfile.read(1)
    bitstreamout.close()
    print("Done")
    

