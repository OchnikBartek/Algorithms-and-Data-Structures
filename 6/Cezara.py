import string
def cezara(text, key):
    alfabet_polski = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
    alfabet_polski_duze = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"
    zaszyfrowane = ""
    for element in text:
        if element in alfabet_polski:
            index = alfabet_polski.index(element)
            nowy_index = (index + key) % len(alfabet_polski)
            zaszyfrowane += alfabet_polski[nowy_index]
        elif element in alfabet_polski_duze:
            index = alfabet_polski_duze.index(element)
            nowy_index = (index + key) % len(alfabet_polski_duze)
            zaszyfrowane += alfabet_polski_duze[nowy_index]
        else:
            zaszyfrowane += element
    return zaszyfrowane

tekst = "piEcZarką"
klucz = 39048948
print(cezara(tekst, klucz))
