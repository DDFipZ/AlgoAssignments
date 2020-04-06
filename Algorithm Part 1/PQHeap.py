"""
Navn                        SDU Brugernavn
Marcus Møller Pedersen      marpe18
Jakob Schledermann Winkel   jwink18
Alban Dalifi                aldal18

Alban er ikke tilmeldt kursus endnu, da han venter svar fra studienævnet
"""

#Heap Sort
#A is a list
#e is a number to be inserted into the A list

#Inserts key value into A list 
def insert(A, key):
    A.append(int(key))
    heapSort(A)

#Extracts the minumum value in heap
def extractMin(A):
    length = len(A)
    min = A[0]
    A[0] = A[length - 1]
    A.pop()
    heapSort(A)
    return min

#Heapifies by lower integers
def low_heapify(A, n, i):
    smallest = i
    #left child 
    l = 2 * i + 1
    #Right Child
    r = 2 * i + 2

    #Checks left child
    if l < n and A[smallest] > A[l]:
        smallest = l

    #Checks Right Child
    if r < n and A[smallest] > A[r]:
        smallest = r

    #Checks if root is smallest, if not, switcharoo
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        #Heapifies
        low_heapify(A, n, smallest)

#Performs the heapsort
def heapSort(A):
    n = len(A)
    for i in range(int(n/2) -1, -1, -1):
        low_heapify(A, n, i)