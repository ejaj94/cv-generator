import os

def load_env(env_path=".env"):
    """
    Carga variables de entorno desde un archivo .env si existe.
    Esta implementación personalizada evita dependencias de librerías externas.
    """
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    # Quitar comillas si existen
                    val_str = val.strip().strip('"').strip("'")
                    os.environ[key.strip()] = val_str

# Cargar variables del .env local al iniciar el módulo
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_env(os.path.join(script_dir, ".env"))

# Resolver rutas configuradas con valores por defecto consistentes
PROFILE_PHOTO_PATH = os.environ.get("PROFILE_PHOTO_PATH", os.path.join(script_dir, "assets", "profile.jpg"))
CERTIFICATES_DIR = os.environ.get("CERTIFICATES_DIR", r"C:\Users\ANGEL RAFAEL\Desktop\Portfolio de programacion\Certificados")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", r"C:\Users\ANGEL RAFAEL\Desktop")
PORTFOLIO_CV_DIR = os.environ.get("PORTFOLIO_CV_DIR", r"C:\Users\ANGEL RAFAEL\Desktop\Portfolio de programacion\CV")

# Asegurarse de que el directorio de salida por defecto se resuelva a ~/Desktop si no existe
if not os.path.exists(OUTPUT_DIR):
    OUTPUT_DIR = os.path.expanduser("~/Desktop")
