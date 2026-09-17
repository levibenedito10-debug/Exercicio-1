def contar_primos(lista, valor):
    contador = 0


    for primo in lista:
        if primo < valor:
            contador += 1
        else:
            break

    return contador

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
resultado = contar_primos(primos, 67)
print(primos)
print("O total de numeros primos é: ", resultado)
