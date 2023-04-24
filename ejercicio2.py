print("--------------------------------")
print("--------------------------------")
print("--------------------------------")

#definiicon de la funcion 
def ultimo_digito_es_cuatro(numero):
    if numero % 10 == 4 :
        print(f"es ultimo digito de {numero } si es 4")
    else :
        print(f"es ultimo digito de {numero} si es 4")
    return numero  
#entrada

numero = int(input("ingrese un numero entero: "))    

#propcesing

ultimo_digito_es_cuatro(numero)

#salida
print("\nEso era...")