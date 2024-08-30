from scapy.all import *
from colorama import init, Fore
import string

# Inicializar colorama
init(autoreset=True)

# Función para descifrar el texto utilizando el cifrado César
def descifrar_cesar(texto, corrimiento):
    resultado = ""
    for char in texto:
        if char.isupper():
            resultado += chr((ord(char) - corrimiento - 65) % 26 + 65)
        elif char.islower():
            resultado += chr((ord(char) - corrimiento - 97) % 26 + 97)
        else:
            resultado += char
    return resultado

# Función para determinar si una cadena es una palabra válida (opcional, depende del lenguaje)
def es_probable(texto):
    palabras_comunes = ["criptografia", "seguridad", "redes"]
    for palabra in palabras_comunes:
        if palabra in texto.lower():
            return True
    return False

# Función para analizar el archivo .pcapng y obtener el mensaje
def analizar_pcapng(archivo):
    paquetes = rdpcap(archivo)
    mensaje_cifrado = ""

    # Extraer datos de los paquetes ICMP
    for paquete in paquetes:
        if ICMP in paquete and paquete[ICMP].type == 8:  # Solo ICMP Echo Request
            mensaje_cifrado += bytes(paquete[ICMP].payload).decode('utf-8', errors='ignore')

    return mensaje_cifrado

# Función principal para descifrar todas las combinaciones y resaltar la más probable
def descifrar_archivo(archivo_pcapng):
    mensaje_cifrado = analizar_pcapng(archivo_pcapng)
    print(f"Mensaje cifrado extraído: {mensaje_cifrado}\n")
    
    for corrimiento in range(26):
        mensaje_descifrado = descifrar_cesar(mensaje_cifrado, corrimiento)
        
        if es_probable(mensaje_descifrado):
            print(Fore.GREEN + f"Corrimiento {corrimiento}: {mensaje_descifrado}")
        else:
            print(f"Corrimiento {corrimiento}: {mensaje_descifrado}")

if __name__ == "__main__":
    archivo_pcapng = "wireshark2.pcapng.gz"  # Reemplaza con el nombre de tu archivo
    descifrar_archivo(archivo_pcapng)
