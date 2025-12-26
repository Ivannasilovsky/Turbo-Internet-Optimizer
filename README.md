# 🚀 Turbo Internet Optimizer

Una herramienta escrita en **Python** diseñada para reducir la latencia (lag) y optimizar el rendimiento del sistema durante sesiones de juego o descargas pesadas.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 ¿Qué hace este programa?

Este script automatiza tareas de mantenimiento de red y gestión de procesos que normalmente requieren múltiples comandos manuales:

1.  **Limpieza de Red:** Ejecuta automáticamente `ipconfig /flushdns`, `/release` y `/renew` para purgar la caché DNS y renovar la IP, eliminando conflictos de conexión.
2.  **Modo Prioridad (VIP):** Utiliza la librería `psutil` para localizar procesos específicos (ej. *Valorant, Steam, Chrome*) y elevar su prioridad de CPU a **ALTA** en tiempo real.
3.  **Prevención de Cuellos de Botella:** Al priorizar el proceso, evita que tareas en segundo plano (como actualizaciones de Windows) roben recursos del sistema mientras juegas.

## 📥 Descarga e Instalación

No necesitas instalar Python para usarlo.

1.  Ve a la sección de [**Releases**](https://github.com/Ivannasilovsky/Turbo-Internet-Optimizer/releases) de este repositorio.
2.  Descarga el archivo `TurboInternet.exe`.
3.  **Importante:** Haz clic derecho en el archivo y selecciona **"Ejecutar como administrador"** (necesario para configurar la red y prioridades).

## 🛠️ Uso para Desarrolladores

Si prefieres ejecutar el script desde el código fuente o modificarlo:

### Requisitos
* Python 3.10+
* Librería `psutil`

### Instalación
```bash
git clone [https://github.com/Ivannasilovsky/Turbo-Internet-Optimizer.git](https://github.com/Ivannasilovsky/Turbo-Internet-Optimizer.git)
cd Turbo-Internet-Optimizer
pip install psutil
