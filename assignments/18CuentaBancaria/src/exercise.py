def main():
    #escribe tu código abajo de esta línea
    saldo_prev_mes = float(input(" Defina el saldo del mes anterior : "))
    ingresos = float(input("Defina su saldo "))
    egresos = float(input(" Defina sus egresos"))
    n_chques = int(input("Cuantos chuques tienes ? : "))
    costo_chques = (n_chques + 13)

    total = (saldo_prev_mes + ingresos + egresos + costo_chques)* 0.075


    print("su total es : " + str(total))
    
    
    
    pass

if __name__ == '__main__':
    main()
