egesz:int = 123
lebegopontos:float = 3.14
karakterlanc:str = 'cica'
logikai:bool = True

#                      0        1       2        3    
nevek:list[str] = ['András', 'Béla', 'Cecil', 'Dénes']
print(nevek)

nevek[2] = 'Csaba'
print(nevek)

nevek.append('Eszter')

print(nevek)
print(nevek[4])

# nem létező elem kiolvasása vagy írása esetén ún. "kivételt" kapunk
# (továbbiakban "hiba", ami egy pontatlan megfogalmazás, de ez most mindegy)

# print(nevek[99])
# nevek[5] = 'Ferenc'


for nev in nevek:
    print(f'A(z) {nev} egy nagyon szép név')

lista_hossza:int = len(nevek)
print(lista_hossza)

# lista elemszáma <=> utolsó elem indexe + 1

for i in range(len(nevek)):
    print(f'a lista {i + 1}. eleme: {nevek[i]}')