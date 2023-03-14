from random import *

#ZPTM
pakli:list[str] = [
    'ZAs', 'ZKi', 'ZFe', 'ZAl', 'Z10', 'Z09', 'Z08', 'Z07',
    'PAs', 'PKi', 'PFe', 'PAl', 'P10', 'P09', 'P08', 'P07',
    'TAs', 'TKi', 'TFe', 'TAl', 'T10', 'T09', 'T08', 'T07',
    'MAs', 'MKi', 'MFe', 'MAl', 'M10', 'M09', 'M08', 'M07', ]

shuffle(pakli)

esz:int = 1
for kartya in pakli:
    print(kartya, end=' ')
    if esz % 8 == 0: print(end='\n')
    esz+=1

