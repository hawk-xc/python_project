# jika belum ada module tabulate
# install module tabulate dengan PIP
# pip install tabulate
# okeyy
from tabulate import tabulate
# nama Wahyu Tri Cahyono
# 12221171
# 12.1A.18 UBSI KAMPUS SURAKARTA
print ("============ GEROBAK FRIED CHICKEN ============")
print ("============ KANG  MAMAT DAN WAHYU ============")

BJENIS = int(input('masukkan banyak input '))
BJENPOT = []
BPOTONG = []
BJUMLAH = []
BTOT = []
BKODE = []
BHARGA = []
i = 0
while i < BJENIS:
    print (i+1)
    BKODE.append(input('KODE ITEM [P/D/S] : '))
    BPOTONG.append(int(input('BANYAK POTONG : ')))
    if BKODE[i] == 'D':
        BJENPOT.append('Dada')
        BHARGA.append(2500)
        BTOT.append(BPOTONG[i] * int("2500"))

    elif BKODE[i] == 'P':
        BJENPOT.append('Paha')
        BHARGA.append(2000)
        BTOT.append(BPOTONG[i] * int("2000"))
    
    elif BKODE[i] == 'S':
        BJENPOT.append('Sayap')
        BHARGA.append(1500)
        BTOT.append(BPOTONG[i] * int("1500"))
    i+=1
print ("===================================================")
print ("============== FRIED AYAM KANG MAMAT ==============")
print ("===================================================")
print ("| No  |  Kode  | Jenis Potong |  HARGA  | B Total |")
a = 0
while a < BJENIS:
    head = [['...', '......', '............', '.......', '.......'], [a+1, BKODE[a], BJENPOT[a], BHARGA[a], BTOT[a]]]
    print(tabulate(head, tablefmt='github'))

    a+=1 
total = sum(BTOT)
percent = total * 10/100
outpt = total + percent
print ("===================================================")
print ('total harga sebelum perpajak 10% ialah Rp {:0,.2f},-'.format(total))
print ('total harga yang terkait dengan pajak 10% : Rp {:0,.2f},-'.format(outpt))
