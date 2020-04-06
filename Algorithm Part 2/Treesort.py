"""
Navn                        SDU Brugernavn
Marcus Møller Pedersen      marpe18
Jakob Schledermann Winkel   jwink18
Alban Dalifi                aldal18
"""
import sys
import DictBinTree

ts = []

for line in sys.stdin:
    DictBinTree.Insert(ts, int(line))

print(DictBinTree.OrderedTraversal(ts))