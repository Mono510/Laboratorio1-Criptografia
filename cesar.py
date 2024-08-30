def cifrado_cesar(texto, corrimiento):
    resultado = ""

    # Iterar sobre cada carácter en el texto
    for char in texto:
        # Verificar si el carácter es una letra mayúscula
        if char.isupper():
            # Encontrar la posición del carácter en el alfabeto y aplicar el corrimiento
            resultado += chr((ord(char) + corrimiento - 65) % 26 + 65)
        # Verificar si el carácter es una letra minúscula
        elif char.islower():
            # Encontrar la posición del carácter en el alfabeto y aplicar el corrimiento
            resultado += chr((ord(char) + corrimiento - 97) % 26 + 97)
        else:
            # Mantener los caracteres no alfabéticos sin cambios
            resultado += char

    return resultado

# Solicitar al usuario el texto a cifrar y el corrimiento
texto = input("Ingrese el texto a cifrar: ")
corrimiento = int(input("Ingrese el corrimiento: "))

# Aplicar el cifrado César
texto_cifrado = cifrado_cesar(texto, corrimiento)

# Mostrar el texto cifrado
print("Texto cifrado:", texto_cifrado)
