# saya manusia tidak kenal takut
def balik(a):
    b = a[::-1].split()
    b.reverse()
    b = ' '.join(b)
    return b

c = input('Masukkan Sebuah Kalimat : ')
print(balik(c))