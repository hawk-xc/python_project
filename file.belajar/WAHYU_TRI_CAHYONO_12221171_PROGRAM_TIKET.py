# input
pembeli = input('Input Nama Pembeli : ')
no_hp = input('Input No. Handphone : ')
jurusan = input('Input Jurusan [SBY/BL/LMP] : ')

# proses
if jurusan == "SBY":
    namajurusan='Surabaya'
    harga=300000

elif jurusan== "BL":
    namajurusan='Bali'
    harga=350000

else:
    namajurusan="Lampung"
    harga=500000

# Input jumlah beli
jumlah = int(input('Masukkan Jumlah beli : '))

# Proses potongan
if jumlah >= 3:
    potongan=(jumlah*harga)*0.1
else:
    potongan=0

total =(jumlah*harga-potongan)

#cetak hasil
print("------------------------------")
print("     PENJUALAN TIKET BUS      ")
print("             XYE              ")
print("Nama Pembeli    : "+str(pembeli))
print("NO. Handphone   : "+str(no_hp))
print("Kode Jurusan    : "+str(jurusan))
print("Kota Tujuan     : "+str(namajurusan))
print("Harga           : ", +(harga))
print("Jumlah beli     : ", +(jumlah))
print("-------------------------------")
print("potongan yang didapat : ",+(potongan))
print("total bayar           : ",+(total))
ubay=int(input("Masukkan uang bayar : "))
uangkembali=ubay-total
print("Uang Kembali : ",+uangkembali)