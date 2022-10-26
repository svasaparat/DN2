spodnja_meja = 1

zgornja_meja = 50



for cifra in range(spodnja_meja, zgornja_meja + 1):
   if cifra > 1:
       for i in range(2, cifra):
           if (cifra % i) == 0:
               break
       else:
           print(cifra)