from scapy.all import *
import os

# Función para cifrar texto utilizando el cifrado César
def cifrado_cesar(texto, corrimiento):
    resultado = ""
    for char in texto:
        if char.isupper():
            resultado += chr((ord(char) + corrimiento - 65) % 26 + 65)
        elif char.islower():
            resultado += chr((ord(char) + corrimiento - 97) % 26 + 97)
        else:
            resultado += char
    return resultado


def enviar_paquetes_icmp(texto):
    print("Ping previo:")
    os.system("ping -c 3 8.8.8.8")
    
    print("\nEnviando caracteres en paquetes ICMP...")
    for char in texto:
        paquete = IP(dst="8.8.8.8")/ICMP()/char.encode()  
        send(paquete)  
        print("Sent 1 packet.")
    
    print("\nPing posterior:")
    os.system("ping -c 3 8.8.8.8")

if __name__ == "__main__":

    texto = input("Ingrese el texto a cifrar: ")
    corrimiento = int(input("Ingrese el corrimiento: "))
    
    # Aplicar el cifrado César
    texto_cifrado = cifrado_cesar(texto, corrimiento)
    print("Texto cifrado:", texto_cifrado)
    
    # Enviar los caracteres cifrados en paquetes ICMP
    enviar_paquetes_icmp(texto_cifrado)
    
    print("Paquetes ICMP enviados.")
