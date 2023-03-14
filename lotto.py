from random import shuffle

tippek:list[int] = []

print('töltsd ki a szelvényt:')
for x in range(7):
    tipp:int = int(input(f'{x+1}. tipp: '))
    tippek.append(tipp)

teljes:list[int] = []
for x in range(1, 36):
    teljes.append(x)

shuffle(teljes)

nyeroszamok:list[int] = teljes[0:7]

talalatok_szama:int = 0
for tipp in tippek:
    if tipp in nyeroszamok:
        talalatok_szama += 1

tippek.sort()
nyeroszamok.sort()

print(f'tippek: {tippek}')
print(f'nyrőszámok: {nyeroszamok}')

print(f'összesen {talalatok_szama} találatod volt')
if (talalatok_szama > 1):
    print('gratulálok a nyereményhez!')