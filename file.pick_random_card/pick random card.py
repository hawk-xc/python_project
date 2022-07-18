from random import choice

for i in range(0, 10):
    while i:
        name_card = ['Jobin', 'Waru', 'Krentil', 'Hati']
        number_card = [2, 4, 5, 8, 10, 'J', 'K', 'Q', 'A']
        datanam = choice(name_card)
        numnam = choice(number_card)
        data = datanam, numnam
        print (data)

        #break
