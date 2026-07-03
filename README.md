# Generador de Currículum Vítae Profesional (Multilingüe) - Enmanuel Jiménez

Este proyecto contiene las herramientas y scripts automáticos en Python para compilar y generar las distintas versiones del Currículum Vítae de **Enmanuel Jiménez** en formato PDF de alta definición y listos para imprimir.

La versión en portugués destaca por integrar dinámicamente una foto de perfil y combinar de forma secuencial una lista de certificados de desarrollo de software (PDF/PNG) procedentes de su portafolio.

---

## 🚀 Características y Estructura

* **`generate_cv_pdf.py`**: Generador del CV tradicional en **Español** usando la librería ReportLab.
* **`generate_cv_pdf_en.py`**: Generador de la versión en **Inglés** (Resume).
* **`generate_cv_pt.py`**: Generador avanzado del CV en **Português de Portugal**. Realiza las siguientes acciones automáticas:
  1. Inserta la foto de perfil en el encabezado.
  2. Compila el CV con ReportLab (2 páginas).
  3. Convierte el certificado de Python Avanzado (imagen PNG) y lo integra en la página 3.
  4. Utiliza `pypdf` para unir los otros 7 certificados en formato PDF (Linux, SQL, Git, SOLID, ORMs, Pseudocódigo) en un único documento de salida unificado.
* **`assets/profile.jpg`**: Foto de perfil oficial para incluir en el diseño del documento.

---

## 🛠️ Instalación de Dependencias

Para poder ejecutar los scripts y generar tus PDFs, debes instalar las siguientes librerías de Python:

```bash
pip install -r requirements.txt
```

*Las dependencias requeridas son:*
* `reportlab`: Creación de la estructura del PDF mediante flowables y canvas.
* `pillow`: Carga y manipulación de la imagen de perfil y certificados PNG.
* `pypdf`: Unión y ensamblado final de los certificados en PDF.

---

## ⚙️ Configuración (.env)

El proyecto utiliza un archivo `.env` para gestionar de manera local las rutas de los certificados y carpetas de salida. Copia el archivo `.env.example` y renómbralo a `.env`:

```ini
PROFILE_PHOTO_PATH=assets/profile.jpg
CERTIFICATES_DIR=C:/Users/TU_USUARIO/Desktop/Portfolio de programacion/Certificados
OUTPUT_DIR=C:/Users/TU_USUARIO/Desktop
PORTFOLIO_CV_DIR=C:/Users/TU_USUARIO/Desktop/Portfolio de programacion/CV
```

---

## 🏃 Ejecución

Ejecuta cualquiera de los generadores desde la consola:

```bash
# Para generar el CV en Portugués con fotos y certificados unificados:
python generate_cv_pt.py

# Para generar el CV básico en Español:
python generate_cv_pdf.py

# Para generar la versión en Inglés:
python generate_cv_pdf_en.py
```

El resultado final se compilará y guardará directamente en las rutas especificadas en tu configuración (`OUTPUT_DIR` y `PORTFOLIO_CV_DIR`).
