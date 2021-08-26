costo_pagina = 54
num_palabras= 475
pagina = num_palabras

palabras = int(input("Dme el numero de palabras " ))

               
total = palabras / num_palabras
cobro = total * costo_pagina

print("El costo sera de:  " + str(cobro))
