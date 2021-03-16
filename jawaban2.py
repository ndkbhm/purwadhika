# 081122223333

def hp(a):
    if len(a) > 13:
        print('Nomor HP Hanya Maksimal 13 Digit')
    elif a[0] != '0' and a[1] != '8' :
        print('Nomor HP Harus Dimulai Dengan 08')
    else:
        print(a)

c = input('Masukkan Nomor HP : ')
hp(c)