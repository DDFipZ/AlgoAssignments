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

def Parent(i):
    return (i - 1) // 2


def insert(A, key):
    A.append(key)
    i = len(A)
    while i > 1 and A[Parent(i)] < A[i]:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)


#Extracts the minumum value in heap
def extractMin(A):
    if len(A) < 1:
        return "Heap Underflow"
    min = A[0]
    A[0] = A[len(A) - 1]
    low_heapify(A, 1)
    return max


#Heapifies by lower integers
def low_heapify(A, i):
    l = 2 * i + 1
    r = 2 * i + 2
    length = len(A)
    smallest = None

    if l <= A[length - 1] and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= A[length - 1] and A[l] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        low_heapify(A, smallest)