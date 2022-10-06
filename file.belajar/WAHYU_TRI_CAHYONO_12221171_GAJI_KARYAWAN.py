# progam tentukan gaji karyawan
# tugas pemrograman dasar
# wahyu tri cahyono
# 12221171
# 12.1A.18
# UBSI KAMPUS SURAKARTA

# DECLARE DATA
name = input('namamu ')
gol = input('golongan ')
pen = input('pendidikan ')
jam = int(input('jam kerja '))

# DATA DICTIONARY
data = {
  'pendSMA': 2.5/100,
  'pendD1': 5/100,
  'pendD3': 20/100,
  'pendS1': 30/100,
  'goll': 5/100,
  'golll': 10/100,
  'gollll': 15/100,
  'origval': 300000
}

# PROGRAM
if jam > 8:
  dtjam = jam - 7
  dtprc = dtjam * 3500

  if pen == 'SMA' or pen == 'sma':
    if gol == '1':
      cent = data['pendSMA'] + data['goll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc

    elif gol == '2':
      cent = data['pendSMA'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc
    
    elif gol == '3':
      cent = data['pendSMA'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc
    
    print ("------------------------------")
    print ("------ PT. DINGIN DAMAI ------")
    print ("------------------------------")
    print ("hallo tuan/mrs         : ", name)
    print ("golongan               : ", gol)
    print ("Pendidikan Tuan/Mrs    : ", pen)
    print ("jam kerja              : ", jam)
    print ("gaji yang diperoleh    : ", res)
    
  elif pen == 'D1' or pen == 'd1':
    if gol == '1':
      cent = data['pendD1'] + data['goll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc
    elif gol == '2':
      cent = data['pendD1'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc
    elif gol == '3':
      cent = data['pendD1'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc

    print ("------------------------------")
    print ("------ PT. DINGIN DAMAI ------")
    print ("------------------------------")
    print ("hallo tuan/mrs         : ", name)
    print ("golongan               : ", gol)
    print ("Pendidikan Tuan/Mrs    : ", pen)
    print ("jam kerja              : ", jam)
    print ("gaji yang diperoleh    : ", res)

  elif pen == 'D3' or pen == 'd3':
    if gol == '1':
      cent = data['pendD3'] + data['goll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc
    elif gol == '2':
      cent = data['pendD3'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc
    elif gol == '3':
      cent = data['pendD3'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc
    
    print ("------------------------------")
    print ("------ PT. DINGIN DAMAI ------")
    print ("------------------------------")
    print ("hallo tuan/mrs         : ", name)
    print ("golongan               : ", gol)
    print ("Pendidikan Tuan/Mrs    : ", pen)
    print ("jam kerja              : ", jam)
    print ("gaji yang diperoleh    : ", res)

  elif pen == 'S1' or pen == 's1':
    if gol == '1':
      cent = data['pendS1'] + data['goll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc
    elif gol == '2':
      cent = data['pendS1'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc
    elif gol == '3':
      cent = data['pendS1'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval'] + dtprc
    
    print ("------------------------------")
    print ("------ PT. DINGIN DAMAI ------")
    print ("------------------------------")
    print ("hallo tuan/mrs         : ", name)
    print ("golongan               : ", gol)
    print ("Pendidikan Tuan/Mrs    : ", pen)
    print ("jam kerja              : ", jam)
    print ("gaji yang diperoleh    : ", res)

else:
  if pen == 'SMA' or pen == 'sma':
    if gol == '1':
      cent = data['pendSMA'] + data['goll']
      per = data['origval'] * cent
      res = per + data['origval']
    elif gol == '2':
      cent = data['pendSMA'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval']
    elif gol == '3':
      cent = data['pendSMA'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval']
    
    print ("------------------------------")
    print ("------ PT. DINGIN DAMAI ------")
    print ("------------------------------")
    print ("hallo tuan/mrs         : ", name)
    print ("golongan               : ", gol)
    print ("Pendidikan Tuan/Mrs    : ", pen)
    print ("jam kerja              : ", jam)
    print ("gaji yang diperoleh    : ", res)
  elif pen == 'D1' or pen == 'd1':
    if gol == '1':
      cent = data['pendD1'] + data['goll']
      per = data['origval'] * cent
      res = per + data['origval']
    elif gol == '2':
      cent = data['pendD1'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval']
    elif gol == '3':
      cent = data['pendD1'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval']

    print ("------------------------------")
    print ("------ PT. DINGIN DAMAI ------")
    print ("------------------------------")
    print ("hallo tuan/mrs         : ", name)
    print ("golongan               : ", gol)
    print ("Pendidikan Tuan/Mrs    : ", pen)
    print ("jam kerja              : ", jam)
    print ("gaji yang diperoleh    : ", res)
  
  elif pen == 'D3' or pen == 'd3':
    if gol == '1':
      cent = data['pendD3'] + data['goll']
      per = data['origval'] * cent
      res = per + data['origval']
    elif gol == '2':
      cent = data['pendD3'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval']
    elif gol == '3':
      cent = data['pendD3'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval']
    
    print ("------------------------------")
    print ("------ PT. DINGIN DAMAI ------")
    print ("------------------------------")
    print ("hallo tuan/mrs         : ", name)
    print ("golongan               : ", gol)
    print ("Pendidikan Tuan/Mrs    : ", pen)
    print ("jam kerja              : ", jam)
    print ("gaji yang diperoleh    : Rp.", res)

  elif pen == 'S1' or pen == 's1':
    if gol == '1':
      cent = data['pendS1'] + data['goll']
      per = data['origval'] * cent
      res = per + data['origval']
    elif gol == '2':
      cent = data['pendS1'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval']
    elif gol == '3':
      cent = data['pendS1'] + data['golll']
      per = data['origval'] * cent
      res = per + data['origval']

    print ("------------------------------")
    print ("------ PT. DINGIN DAMAI ------")
    print ("------------------------------")
    print ("hallo tuan/mrs         : ", name)
    print ("golongan               : ", gol)
    print ("Pendidikan Tuan/Mrs    : ", pen)
    print ("jam kerja              : ", jam)
    print ("gaji yang diperoleh    : ", res)