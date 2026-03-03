#Este será un script inicial muy sencillo en Python. 
#Su única función por ahora será enviar un paquete ICMP (Ping) a un destino 
#(como los DNS de Google) cada 5 segundos y mostrar el resultado. 
#Más adelante haremos que envíe estos datos a la API y a la base de datos.


import time
import subprocess

TARGET_IP = "8.8.8.8"

def ping_target(ip):
    try:
        # Ejecuta un ping de 1 paquete (-c 1). Ideal para entornos Linux/Contenedores.
        output = subprocess.check_output(["ping", "-c", "1", ip], universal_newlines=True)
        # Extraemos solo la línea con las estadísticas de tiempo
        print(f"[OK] {ip} -> {output.splitlines()[1]}")
    except subprocess.CalledProcessError:
        print(f"[FALLO] No se pudo alcanzar a {ip} o hay pérdida de paquetes.")

if __name__ == "__main__":
    print(f"Iniciando Net-Watch Prober...")
    print(f"Destino configurado: {TARGET_IP}")
    
    while True:
        ping_target(TARGET_IP)
        time.sleep(5)