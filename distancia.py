#distancia euclediana 

import math

#   [x,  y]
m = [[16, 18],
    [2, 6], 
    [14, 16], 
    [18, 4], 
    [6, 20], 
    [20, 2], 
    [4, 8], 
    [12, 12], 
    [22, 24], 
    [6, 8], 
    [24, 22], 
    [10, 14]]


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
    print('Resultado parcial de fronteira: ', lower)
    return lower

def minDist(array, start, end):
    print('Chamada recursiva: start->  ',start,' end-> ',end-1)
    if (end - start) <= 3:
        new = []
        for i in range(start, end):
            new.append(array[i])
        print(new,'| Resultado Parcial: ', minDistBrute(new))
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

x = 'x: '
y = 'y: '
for i in range(0, len(m)):
    x += '\t'+str(m[i][0])
    y += '\t'+str(m[i][1])

print('Entrada de dados:')
print(x)
print(y)

sort(m, "x")

x = 'x: '
y = 'y: '
for i in range(0, len(m)):
    x += '\t'+str(m[i][0])
    y += '\t'+str(m[i][1])

print('Vetor de pontos ordenado em x:')
print(x)
print(y)

resp = minDist(m, 0, len(m))
print('\n\n Resultado: ',resp)
