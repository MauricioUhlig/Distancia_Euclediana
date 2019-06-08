#distancia euclediana 

# v1 = [1.2, 2, 3.8, 4.5]
# v2 = [0.5, 4.5, 9.6, 3.4]

# def dist_euclidiana(v1, v2):
# 	dim, soma = len(v1), 0
# 	for i in range(dim):
# 		soma += math.pow(v1[i] - v2[i], 2)
# 	return math.sqrt(soma)

# print('%.2f' % dist_euclidiana(v1, v2))

# print("teste de python")

import math

m = [[8, 9],[1, 3], [7, 8], [9, 2], [3, 10], [10, 1], [2, 4], [6, 6], [11, 12], [4, 5], [12, 11], [5, 7]]

print "antes"
print m

print "depois"
def sort(array):
    for p in range(0, len(array)):
        current_elementX = array[p][0]
        current_elementY = array[p][1]

        while p > 0 and array[p -1][0] > current_elementX:
            array[p][0] = array[p -1][0]
            array[p][1] = array[p -1][1]
            p -= 1

        array[p][0] = current_elementX
        array[p][1] = current_elementY

sort(m)
print m

def dist(a,b):
    return math.sqrt(math.pow(a[0] - b[0],2) + math.pow(a[1]-b[1],2))

def minDistBrute(array):
    return min(dist(array[0],array[1]),dist(array[1],array[2]),dist(array[2],array[0]))

def minDist(array, n):
    if n <= 3:
        return minDistBrute(array)

    m = n/2
    dl = minDist(array, m)
    dr = minDist(array+m, n-m)
    d = min(dr,dl)
    s = []
    midx = array[m][0]
    j = 0

    for i in range(0, n):
        if math.sqrt(math.pow(array[i][0]-midx,2)) < d:
            s.append(array[i][0])
            j = j+1
    mf = minDistFront(s, j, d)
    return min(d, mf)





resp = minDistBrute(m)
print resp
