#distancia euclediana 

import math

m = [[8, 9],[1, 3], [7, 8], [9, 2], [3, 10], [10, 1], [2, 4], [6, 6], [11, 12], [4, 5], [12, 11], [5, 7]]

# print "antes"
# print m

def sort(array, axis):
    for p in range(0, len(array)):
        current_elementX = array[p][0]
        current_elementY = array[p][1]

        if(axis == "X" or axis == "x"):
            while p > 0 and array[p -1][0] > current_elementX:
                array[p][0] = array[p -1][0]
                array[p][1] = array[p -1][1]
                p -= 1
        elif(axis == "Y" or axis == "y"):
            while p > 0 and array[p -1][1] > current_elementY:
                array[p][0] = array[p -1][0]
                array[p][1] = array[p -1][1]
                p -= 1
        array[p][0] = current_elementX
        array[p][1] = current_elementY

sort(m, "x")

# print "depois"
# print m

def dist(a,b):
    return math.sqrt(math.pow(a[0] - b[0],2) + math.pow(a[1]-b[1],2))

def minDistBrute(array):
    if(len(array)) == 3:
        return min(dist(array[0],array[1]),dist(array[1],array[2]),dist(array[2],array[0]))
    else: 
        return dist(array[0],array[1])

def minDistFront(s, end, lower):
    sort(s,"y")
    
    for i in range(0, len(s)-1):
        j = i+1
        while (j < end) and (s[j][1]-s[i][1] < lower):
            aux = dist(s[i],s[j])
            j += 1
            if( aux < lower):
                lower = aux
    return lower

def minDist(array, start, end):
    print "Chamada recursiva: start->  "+ str(start)+ " end-> " + str(end)
    if (end - start) <= 3:
        new = []
        for i in range(start, end):
            new.append(array[i])
        print new, minDistBrute(new)
        return minDistBrute(new)

    middle = int((start + end)/2)
    dl = minDist(array, start, middle)
    dr = minDist(array, middle, end)
    d = min(dr,dl)
    s = []
    midx = array[middle][0]
    j = 0

    for i in range(start, end):
        if math.sqrt(math.pow(array[i][0]-midx,2)) < d:
            s.append(array[i])
            j = j+1
    mf = minDistFront(s, j, d)
    return min(d, mf)


print m
resp = minDist(m, 0, len(m)-1)
print resp
