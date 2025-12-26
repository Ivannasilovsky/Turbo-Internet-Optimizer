import subprocess # Asegúrate de que esto esté importado

def limpiar_red():
    print("\n--- LIMPIEZA DE RED INICIAL ---")
    print("Renovando IP y purgando DNS...")
    # Ejecutamos los comandos de sistema ocultando la ventana negra extra
    subprocess.run("ipconfig /release", shell=True, stdout=subprocess.DEVNULL)
    subprocess.run("ipconfig /renew", shell=True, stdout=subprocess.DEVNULL)
    subprocess.run("ipconfig /flushdns", shell=True, stdout=subprocess.DEVNULL)
    print("✅ Red purgada y lista.")

# --- LUEGO, DENTRO DE TU FUNCIÓN main(), LLAMA A ESTA FUNCIÓN AL PRINCIPIO ---
def main():
    if not es_admin():
        # ... (tu código de verificación de admin) ...
        return

    limpiar_red()  # <--- AGREGA ESTA LÍNEA AQUÍ
    
    print("================================================================")
    # ... (el resto de tu código)

import psutil
import time
import os
import sys
import ctypes

def es_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def cambiar_prioridad(nombre_objetivo):
    """
    Busca procesos por nombre y les sube la prioridad al máximo seguro (HIGH).
    No usamos REALTIME porque podría congelar el mouse/teclado.
    """
    encontrado_count = 0
    print(f"\n🔍 Buscando procesos que contengan: '{nombre_objetivo}'...")

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Info del proceso actual
            p_info = proc.info
            p_name = p_info['name'].lower()
            
            if nombre_objetivo.lower() in p_name:
                p = psutil.Process(p_info['pid'])
                
                # Verificamos la prioridad actual
                prioridad_actual = p.nice()
                
                # CAMBIO DE PRIORIDAD
                # En Windows: psutil.HIGH_PRIORITY_CLASS (Alta)
                # psutil.ABOVE_NORMAL_PRIORITY_CLASS (Por encima de lo normal)
                if prioridad_actual != psutil.HIGH_PRIORITY_CLASS:
                    p.nice(psutil.HIGH_PRIORITY_CLASS)
                    print(f"✅ [MEJORADO] {p_info['name']} (PID: {p_info['pid']}) -> Prioridad ALTA establecida.")
                    encontrado_count += 1
                else:
                    print(f"ℹ️  [YA OPTIMO] {p_info['name']} (PID: {p_info['pid']}) ya tiene prioridad Alta.")
                    encontrado_count += 1
                    
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
            
    if encontrado_count == 0:
        print(f"❌ No encontré ningún proceso activo con el nombre '{nombre_objetivo}'.")
        print("   Asegúrate de que el programa ya esté abierto.")
    else:
        print(f"\n✨ Éxito: Se optimizaron {encontrado_count} procesos.")

def main():
    if not es_admin():
        print("================================================================")
        print("⚠️  ERROR DE PERMISOS")
        print("   Necesitas ejecutar este script como ADMINISTRADOR.")
        print("   Windows no permite cambiar prioridades sin permiso.")
        print("================================================================")
        # Intentar relanzar como admin (truco avanzado)
        input("Presiona ENTER para cerrar...")
        return

    print("================================================================")
    print("🚀 OPTIMIZADOR DE PRIORIDAD DE PROCESOS")
    print("   Esto le dice al CPU que tu programa es lo más importante.")
    print("================================================================")
    
    while True:
        objetivo = input("\nEscribe el nombre del programa (ej: chrome, valorant, edge): ")
        if objetivo.strip():
            cambiar_prioridad(objetivo)
        
        continuar = input("\n¿Quieres optimizar otro programa? (s/n): ")
        if continuar.lower() != 's':
            break
            
    print("\nPrograma finalizado. La prioridad se mantiene hasta que cierres la aplicación optimizada.")
    time.sleep(3)

if __name__ == "__main__":
    main()