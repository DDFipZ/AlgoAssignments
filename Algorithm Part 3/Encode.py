import sys
import bitIO
from Element import Element
import PQHeap

# outfile = open(sys.argv[2], 'wb')
def HUFFMAN(C):
    huffman_tree = []
    for i in range(len(C)):
        first_element = Element(C[i], [i])
        PQHeap.insert(huffman_tree, first_element)

    while len(huffman_tree) > 1:
        firstmin = PQHeap.extractMin(huffman_tree)
        secondmin = PQHeap.extractMin(huffman_tree)
        
        second_element = Element(firstmin.key + secondmin.key, [firstmin.data + secondmin.data])
        PQHeap.insert(huffman_tree, second_element)

    return huffman_tree

def create_password_list(asciiList):
    passwordList = []

def OrderedTraversal(byte, passwordList):
    list = []
    #recursive method used for cycling through the given list's values inorder 
    def InOrderTreeWalk(x):
        if x != None:
            InOrderTreeWalk(x.key)
            list.append(x.key)
            InOrderTreeWalk(x.right)

    InOrderTreeWalk(T[0])
    
    return list

if __name__ == "__main__":
    infile = open(sys.argv[1], 'rb')

    asciiList = []
    #Sets up the asciiList with 0 frequency on all elements
    for x in range(256):
        asciiList.append(Element(x, 0))

    while True:
        x = infile.readbit()
        if not bitstreamin.readsucces():  # End-of-file?
            break
        bitstreamout.writebit(x)

