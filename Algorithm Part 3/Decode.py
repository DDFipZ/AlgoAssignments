import sys
import bitIO
import Encode
from Element import Element

# def huffmanTraversal(root, b, bitstreamin):
#     if len(root) > 1:
#         huffmanTraversal(root[b], bitstreamin.readbit(), bitstreamin)


if __name__ == "__main__":

    infile = open(sys.argv[1], "rb")
    outfile = open(sys.argv[2], "wb")
    bitstreamin = bitIO.BitReader(infile)

    #Regenerates a frequency list
    freqList = []
    for i in range(256):
        freq = bitstreamin.readint32bits()
        freqList.append(Element(freq, i))


    #while loop for cycling through the file
    huffmanList = Encode.HUFFMAN(freqList)    
    # while bit:
    #     print(huffmanList[0].data)
    #     dataNumber = huffmanTraversal(huffmanList[0].data, bit, huffmanList)
    #     outfile.write(bytes([dataNumber]))
    #     bit = str(bitstreamin.readbit())
    # bitstreamin.close()
    # print("Done")

    def huff(root, b):
        currentRoot = root
        while len(currentRoot) > 1:
            if b == "0":
                currentRoot = currentRoot[0]
            else:
                currentRoot = currentRoot[1]
        print("current root: " + str(currentRoot))
        return currentRoot
        # currentRoot = root

    b = bitstreamin.readbit()
    print(b)
    currentRoot = huffmanList[0].data
    while True:
        if not bitstreamin.readsucces():
            break
        root = huffmanList[0].data
        if b == 0:
            currentRoot = currentRoot[0]
        else:
            currentRoot = currentRoot[1]
        if not len(currentRoot) > 1:
            outfile.write(bytes([currentRoot[0]]))
            currentRoot = huffmanList[0].data
        b = bitstreamin.readbit()
        


    # while True:
    #     if not bitstreamin.readsucces():
    #         break

    #     leaf = huffmanTraversal(huffmanList[0].data, bit, bitstreamin)
    #     print("returned value: " + str(leaf))
    #     outfile.write(bytes([leaf[0]]))
    #     bit = bitstreamin.readbit()