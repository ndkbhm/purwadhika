# ini adalah sebuah contoh

def kapital(a):
    b = a.split()
    b = ''.join(b)
    
    if len(b) > 202 :
        print("Batas Karakter Maksimal Hanya 200")
    elif b == '**' :
        print ("Masukkan Sebuah Inputan")
    else:
        print(b)

d = input("Masukkan Sebuah Kalimat : ")
kapital('*'+d.upper()+'*')