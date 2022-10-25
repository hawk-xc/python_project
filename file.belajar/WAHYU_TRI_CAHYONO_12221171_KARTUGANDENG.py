    M = (
        'Zero',
        'ratu',
        'dimpil',
        'ciwir',
        'gundul',
        'babi',
        'tengkrang'
    )
    H = (
        'Zero',
        'petik',
        'plompong',
        'gunung',
        'cawang',
        'kantong',
        'kerok'
    )
    nilai = ''
    warna = ''

    while warna != 'quit':
        nilai = int(input('masukkan nilai kartu [1-6] '))
        warna = input('masukkan kode warna [H/h, M/m] ')
        if nilai in range(1, 7):
            if warna == "h" or warna == "H":
                print(H[nilai])
        
            elif warna == "m" or warna == "M":
                print(M[nilai])
        
            else:
                print ('kode warna yang anda inputkan salah, kode warna yang terdaftar ialah [H/h, M/m]')
        
        else:
            print ('angka', nilai, 'yang anda input kan salah, rentang nilai valid adalah [1-6]')