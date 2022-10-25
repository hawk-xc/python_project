from textwrap import indent
import pandas as pd

data = ['satu', 'dua', 'tiga', 'empat', 'lima', 1, 2, 3, 4, 5]

sec = pd.Series(data)

print (sec[[2, 9]])