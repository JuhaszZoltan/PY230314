nevek:list[str] = []
jegyek:list[int] = []

nev:str = '---'
while nev != '':
    nev = input('írd be az új nevet: ')
    if nev != '':
        nevek.append(nev)
        jegy:int = int(input(f'írd be {nev} matekjegyét: '))
        jegyek.append(jegy)

# [2, 3, 5] => 3.33333

jegyek_osszege:int = 0
for j in jegyek:
    jegyek_osszege += j

avg:float = jegyek_osszege / len(jegyek)
print(f'osztályátlag: {avg}')

maxindex:int = 0
for i in range(len(jegyek)):
    if jegyek[i] > jegyek[maxindex]:
        maxindex = i
print(f'a legjobb jegyet ({jegyek[maxindex]}) {nevek[maxindex]} tanulója szerezte')

af:int = 0
for j in jegyek:
    if j > avg: af += 1
print(f'átlag felett teljesító tanulók száma: {af}')

print('itt a vége')