"""
Navn                        SDU Brugernavn
Marcus Møller Pedersen      marpe18
Jakob Schledermann Winkel   jwink18
Alban Dalifi                aldal18

Alban er ikke tilmeldt kursus endnu, da han venter svar fra studienævnet
"""
import math

#Heap Sort
#A is a list
#e is a number to be inserted into the A list

#Inserts key value into A list 

def Parent(i):
    return math.floor((i-1/2))

def Left(i):
    return (2 * i + 1 )

def Right(i):
    return (2 * i + 2 )


def insert(A, key):
    A.append(key)
    i = len(A) - 1

    while i > 0 and A[Parent(i)] > A[i]:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)


#Extracts the minumum value in heap
def extractMin(A):
    #lenght = len(A)
    # if len(A) < 1:
    #     return "Heap Underflow"
        
    min = A[0]
    A.pop(0)
    #A[0] = A[A[lenght]]
    #A[lenght] = [lenght - 1]
    low_heapify(A, 0)
    return min


#Heapifies by lower integers
def low_heapify(A, i):
    l = Left(i)
    r = Right(i)
    length = len(A) - 1
    smallest = i

    if l <= length and A[l] < A[i]:
        smallest = l


    if r <= length and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        low_heapify(A, smallest)
