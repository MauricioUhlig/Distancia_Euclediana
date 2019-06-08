#distancia euclediana 

# import math

# v1 = [1.2, 2, 3.8, 4.5]
# v2 = [0.5, 4.5, 9.6, 3.4]

# def dist_euclidiana(v1, v2):
# 	dim, soma = len(v1), 0
# 	for i in range(dim):
# 		soma += math.pow(v1[i] - v2[i], 2)
# 	return math.sqrt(soma)

# print('%.2f' % dist_euclidiana(v1, v2))

# print("teste de python")


m = [[8, 1, 7, 9, 3, 10, 2, 6,11, 4, 12, 5],[9, 3, 8, 2, 10, 1, 4, 6, 12, 5, 11, 7]]

print "antes"
print m[0]
print m[1]

print "depois"
def sort(array):
    for p in range(0, len(array[0])):
        current_elementX = array[0][p]
        current_elementY = array[1][p]

        while p > 0 and array[0][p - 1] > current_elementX:
            array[0][p] = array[0][p - 1]
            array[1][p] = array[1][p - 1]
            p -= 1

        array[0][p] = current_elementX
        array[1][p] = current_elementY

sort(m)
print m[0]
print m[1]

def minDist(array, n):
    if n <= 3:
        return minDistBrute(array)

    m = n/2
    dl = minDist(array, m)
    dr = minDist(array+m, n-m)
    d = min(dr,dl)
    s = []
    midx = array[0][m]
    j = 0

    for i in range(0, n):
        if math.sqrt(math.pow(array[0][i]-midx)) < d:
            s.append(array[0][i])
            j = j+1
    mf = minDistFront(s, j, d)
    return min(d, mf)