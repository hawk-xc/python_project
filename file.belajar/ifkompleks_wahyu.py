M = (
    'ratu',
    'dimpil',
    'ciwir',
    'gundul',
    'babi',
    'tengkrang'
)
H = (
    'petik',
    'plompong',
    'gunung',
    'cawang',
    'kantong',
    'kerok'
)

nilai = ''
warna = ''
try:
    while nilai != 'quit':
        nilai = int(input('masukkan nilai kartu [1-6] '))
        warna = input('masukkan kode warna [H/h, M/m] ')
        if nilai in range(1, 7):
            if warna == "h" or warna == "H":
                if nilai == 1:
                    print (H[0])
                elif nilai == 2:
                    print (H[1])
                elif nilai == 3:
                    print (H[2])
                elif nilai == 4:
                    print (H[3])
                elif nilai == 5:
                    print (H[4])
                elif nilai == 6:
                    print (H[5])

            elif warna == "m" or warna == "M":
                if nilai == 1:
                    print (M[0])
                elif nilai == 2:
                    print (M[1])
                elif nilai == 3:
                    print (M[2])
                elif nilai == 4:
                    print (M[3])
                elif nilai == 5:
                    print (M[4])
                elif nilai == 6:
                    print (M[5])

            else:
                print ('kode warna', warna, 'yang anda inputkan salah, kode warna yang terdaftar ialah [H/h, M/m]')
        else:
            print ('angka', nilai, 'yang anda input kan salah, rentang nilai valid adalah [1-6]')

except ValueError:
    print ('program exit')
    