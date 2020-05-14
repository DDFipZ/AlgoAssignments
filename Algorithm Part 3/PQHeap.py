"""
Navn                        SDU Brugernavn
Marcus Møller Pedersen      marpe18
Jakob Schledermann Winkel   jwink18
Alban Dalifi                aldal18
"""
import math
import Element


def Parent(i):
    return math.floor((i - 1) / 2)


def Left(i):
    return (2 * i + 1 )


def Right(i):
    return (2 * i + 2 )


#Inserts element into A
def insert(A, e):
    A.append(e)
    i = len(A) - 1

    #Switches parent and child if child is lower value
    while i > 0 and A[Parent(i)].key > A[i].key:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)


#Extracts the minumum value in heap
def extractMin(A):
    min = A[0]
    
    #Sets last value as first, then removes the last index
    A[0] = A[len(A) - 1]
    A.pop()
    low_heapify(A, 0)
    return min


#Heapifies by lower integers
def low_heapify(A, i):
    l = Left(i)
    r = Right(i)
    length = len(A) - 1
    smallest = i

    #Makes the lowest value parent
    if l <= length and A[l] < A[i]:
        smallest = l

    if r <= length and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        low_heapify(A, smallest)