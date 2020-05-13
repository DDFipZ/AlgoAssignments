import sys
import bitIO
from Element import Element
import PQHeap

# outfile = open(sys.argv[2], 'wb')
def HUFFMAN(C):
    n = len(C)
    Q = C

    #Steps to build the tree
    for i in range(n):
        x = PQHeap.extractMin(Q)
        y = PQHeap.extractMin(Q)
        freq = x.key + y.key
        element = Element(freq, [x, y])
        PQHeap.insert(Q, element)







    #     huffman_tree = []
    #     first_element = Element(C[i], [i])
    #     PQHeap.insert(huffman_tree, first_element)

    # while len(huffman_tree) > 1:
    #     firstmin = PQHeap.extractMin(huffman_tree)
    #     secondmin = PQHeap.extractMin(huffman_tree)
        
    #     second_element = Element([firstmin.key, secondmin.key], firstmin.data + secondmin.data)
    #     PQHeap.insert(huffman_tree, second_element)

    return PQHeap.extractMin(Q)


def codeList(asciiList):
    codeList = []
    for n in range(len(asciiList)): codeList.append(0)
    huffmanTree = HUFFMAN(asciiList)
    OrderedTraversal(huffmanTree[0].data, "", codeList)

def OrderedTraversal(byte, bitstring, codeList):
    #recursive method used for cycling through the given list's values inorder 
    if len(byte) > 1: 
        OrderedTraversal(x[0], bitstring + "0", codeList)
        OrderedTraversal(x[0], bitstring + "1", codeList)
    elif len(byte) == 1 and len(bitstring) != 0:
        codeList[x[0]] = bitstring


if __name__ == "__main__":
    infile = open(sys.argv[1], 'rb')
    bitstreamin = bitIO.BitReader(infile)

    # outfile = open(sys.argv[2], "wb")
    # bitstreamout = bitIO.BitWriter(outfile)

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

    

