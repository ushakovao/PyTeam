#needs nb operations
def factorialIteration(nb):
    res=1
    if nb ==0:
        res=1
    else:
        for i in range (1,nb+1):
            res=res*i
    return res

print(factorialIteration(5))




#needs nb operations
def factorialRecursion(nb):
    if nb ==0:
        return 1
    else:
        return factorialRecursion(nb-1)*nb

print(factorialRecursion(5))





#needs nb operations
def fiboIteration(nb):
    listFibo=[0,1]
    for i in range(2,nb+1):
        temp=listFibo[i-1] + listFibo[i-2]
        listFibo.append(temp)

    return listFibo[nb]

print('fiboIteration gives {0} for nb = {1}.'.format(fiboIteration(7), 7))


#needs 2**n operations
def fiboRecursion(nb):
    if nb==0:
        return 0
    elif nb==1:
        return 1
    else:
        return fiboRecursion(nb-1)+fiboRecursion(nb-2)

print('fiboRecursion gives {0} for nb = {1}.'.format(fiboRecursion(7), 7))






#needs nb operations
def fiboRecursionOptimizedERROR1(nb):
    fiboList1 = list()
    if nb in fiboList1:
        return fiboList1[nb]
    #new if's
    if nb==0:
        fiboList1.append(0)
        return 0
    elif nb==1:
        fiboList1.append(1)
        return 1
    else:
        temp=fiboRecursionOptimizedERROR1(nb-1) + fiboRecursionOptimizedERROR1(nb-2)
        fiboList1.append(temp)
        print(fiboList1)
    return temp

print('fiboRecursionOptimizedERROR1 gives {0} for nb = {1}.'.format(fiboRecursionOptimizedERROR1(7), 7))

fiboList2 = list()
def fiboRecursionOptimizedERROR2(nb):

    if nb in fiboList2:
        return fiboList2[nb]
    #new if's

    if nb==0:
        fiboList2.append(0)
        return 0
    elif nb==1:
        fiboList2.append(1)
        return 1
    else:
        temp=fiboRecursionOptimizedERROR2(nb-2) + fiboRecursionOptimizedERROR2(nb-1)
        fiboList2.append(temp)
        print(fiboList2)
    return temp

print('fiboRecursionOptimizedERROR2 gives {0} for nb = {1}.'.format(fiboRecursionOptimizedERROR2(7), 7))




fiboDict= dict()
def fiboRecursionOptimized(nb):

    if nb in fiboDict:
        return fiboDict[nb]
    #new if's
    if nb==0:
        fiboDict[0]=0
        return 0
    elif nb==1:
        fiboDict[1]=1
        return 1
    else:
        temp=fiboRecursionOptimized(nb-1) + fiboRecursionOptimized(nb-2)
        fiboDict[nb]=temp
        print(fiboDict)
    return temp


print('fiboRecursionOptimized gives {0} for nb = {1}.'.format(fiboRecursionOptimized(7), 7))





