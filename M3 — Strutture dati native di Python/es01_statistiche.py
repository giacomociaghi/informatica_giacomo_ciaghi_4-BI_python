voti = [7, 5, 8, 6, 9, 4, 7, 10]

numero_voti = len(voti)
somma_voti = sum(voti)
media_voti = somma_voti / numero_voti
voto_minimo = min(voti)
voto_massimo = max(voti)

sufficienti = 0
for voto in voti:
    if voto >= 6:
        sufficienti += 1


print(f"Voti registrati: {numero_voti}")
print(f"Somma: {somma_voti}")
print(f"Media: {media_voti:.2f}")
print(f"Voto minimo: {voto_minimo}")
print(f"Voto massimo: {voto_massimo}")
print(f"Sufficienti: {sufficienti} su {numero_voti}")
 

#output
#Voti registrati: 8
#Somma: 56
#Media: 7.00
#Voto minimo: 4
#Voto massimo: 10
#Sufficienti: 6 su 8

