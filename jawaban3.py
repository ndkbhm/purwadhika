def ganjilGenap(a):
    ganjil = []
    genap = []
    for b in a:
        if b % 2 == 0:
            genap.append(b)
        else:
            ganjil.append(b)
    ganjil.sort()
    genap.sort()
    genap.reverse()
    return ganjil + genap

c = [1,3,2,2,1,5,1,24,12,124,12,21,32,15]
print(ganjilGenap(c))