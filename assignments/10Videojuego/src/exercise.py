def main():
    #escribe tu código abajo de esta línea
    cantidad_juegos_nuevos = int(input("Dame la cantidad de juegos nuevos : "))
    cantidad_juegos_usados = int(input("Dame la cantida de juegos usados : "))

    precios_nuevos = 1000
    precios_usados = 350

    total_nuevos = precios_nuevos*cantidad_juegos_nuevos
    total_viejos = precios_usados*cantidad_juegos_usados
        
    compra = total_nuevos + total_viejos

    print(compra)
   pass



if __name__ == '__main__':
    main()
