from BinNode import BinNode


#Inserts k into T
def Insert(T, k):
    y = None
    x = None
    if len(T) >= 1:
        x = T[0]
    while x != None:
        y = x
        if k < x.key:
            x = x.left
        else:
            x = x.right
    if y == None:
        #Adds a BinNode to the list with key = k
        T.append(BinNode(k))
    elif k < y.key:
        #Adds a BinNode as the left child of y
        y.left = BinNode(k)
    else:
        #Adds a BinNode as the right child of y
        y.right = BinNode(k)


#Searches for k in T and returns a boolean
def Search(T, k):
    def TreeSearch(x, k):
        if x == None: return False
        #It has found the key in the given list
        if k == x.key: return True
        if k < x.key:
            #Value is less than x's key, so it goes to the left
            return TreeSearch(x.left, k)
        else:
            #Value is greater than or equal to x's key, so it goes to the right
            return TreeSearch(x.right, k)
    if len(T) >= 1:
        #If length is 0, return false
        return TreeSearch(T[0], k)
    else:
        return False


#Returns a list
def OrderedTraversal(T):
    list = []
    #recursive method used for cycling through the given list's values inorder 
    def InOrderTreeWalk(x):
        if x != None:
            InOrderTreeWalk(x.left)
            list.append(x.key)
            InOrderTreeWalk(x.right)

    InOrderTreeWalk(T[0])
    
    return list