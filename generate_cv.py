import os
import argparse
import sys
import shutil

# Asegurar que el directorio core y languages puedan ser importados
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core import config
from core.styles import get_cv_styles, C_SECONDARY
from core.builders import CVStoryBuilder, LetterStoryBuilder
from core.pdf_writer import PDFWriter
from core.merger import PDFMerger
from languages.spanish import SpanishCVContent
from languages.english import EnglishCVContent
from languages.portuguese import PortugueseCVContent

def generate_for_language(lang: str):
    """
    Genera el CV (y opcionalmente la carta y certificados unificados) para un idioma específico (SRP).
    """
    print(f"\n--- Iniciando generación en idioma: {lang.upper()} ---")
    
    # 1. Resolver el proveedor de contenidos (LSP/DIP)
    if lang == 'es':
        provider = SpanishCVContent()
    elif lang == 'en':
        provider = EnglishCVContent()
    elif lang == 'pt':
        provider = PortugueseCVContent()
    else:
        print(f"[ERROR] Idioma no soportado: {lang}", file=sys.stderr)
        return
        
    styles = get_cv_styles()
    suffix = provider.get_filename_suffix()
    
    # Rutas finales de salida
    temp_pdf_name = f"CV_Enmanuel_Jimenez{suffix}_Temp.pdf"
    final_pdf_name = f"CV_Enmanuel_Jimenez{suffix}.pdf"
    
    temp_pdf_path = os.path.join(config.OUTPUT_DIR, temp_pdf_name)
    final_pdf_path = os.path.join(config.OUTPUT_DIR, final_pdf_name)
    
    # 2. Construir la historia del CV
    # Pasamos la foto de perfil al constructor
    story = CVStoryBuilder.build_cv_story(provider, styles, config.PROFILE_PHOTO_PATH)
    
    # Caso especial para portugués: Anexar la imagen del certificado de Python Avanzado (PNG)
    if lang == 'pt':
        python_adv_img_path = os.path.join(config.CERTIFICATES_DIR, "Certificado de python avanzado..png")
        if os.path.exists(python_adv_img_path):
            try:
                from reportlab.platypus import PageBreak, Spacer, Paragraph, Image as RLImage, HRFlowable
                story.append(PageBreak())
                story.append(Paragraph("ANEXO: CERTIFICADOS DE PORTFÓLIO", styles['section']))
                story.append(HRFlowable(width="100%", thickness=0.5, color=C_SECONDARY, spaceAfter=12, spaceBefore=2))
                story.append(Paragraph("<b>Certificado de Python Avançado - ConquerBlocks:</b>", styles['body']))
                story.append(Spacer(1, 8))
                
                cert_img = RLImage(python_adv_img_path, width=480, height=340)
                cert_img.hAlign = 'CENTER'
                story.append(cert_img)
                print("[OK] Certificado de Python Avanzado (PNG) incorporado a la historia del PDF.")
            except Exception as e:
                print(f"[WARN] No se pudo añadir el certificado PNG: {e}")
                
    # 3. Compilar el PDF base del CV
    # Si requiere fusión posterior (Portugués con certificados), generamos un temporal primero
    target_pdf_path = temp_pdf_path if lang == 'pt' else final_pdf_path
    success = PDFWriter.compile_pdf(target_pdf_path, story)
    
    if not success:
        print(f"[ERROR] Error al generar el CV para {lang.upper()}", file=sys.stderr)
        return
        
    # 4. Caso especial para portugués: Fusionar con los otros certificados PDF
    if lang == 'pt':
        certificados_pdf = [
            "Certificado linux y la terminal..pdf",
            "Certificado de git y github..pdf",
            "Certificado de Python Inicial..pdf",
            "Certficado de SQL.pdf",
            "Certificado uso de orms en python.pdf",
            "Certificado principios solid y acceso a bases de datos ..pdf",
            "Cerificado pseudocodigo.pdf"
        ]
        print("[INFO] Iniciando fusión de certificados PDF...")
        merge_success = PDFMerger.merge_cv_with_certificates(
            temp_pdf_path, 
            config.CERTIFICATES_DIR, 
            certificados_pdf, 
            final_pdf_path
        )
        
        # Eliminar archivo temporal
        try:
            if os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)
                print("[OK] Fichero temporal del CV de portugués eliminado.")
        except Exception as e:
            print(f"[WARN] No se pudo borrar el temporal: {e}")
            
        if not merge_success:
            print(f"[ERROR] Falló la fusión de certificados para {lang.upper()}", file=sys.stderr)
            return

    # 5. Copiar el PDF final generado a la carpeta de CV del Portafolio si existe
    if os.path.exists(config.PORTFOLIO_CV_DIR):
        final_portfolio_pdf = os.path.join(config.PORTFOLIO_CV_DIR, final_pdf_name)
        try:
            shutil.copy(final_pdf_path, final_portfolio_pdf)
            print(f"[SUCCESS] Copiado PDF final al portafolio: {final_portfolio_pdf}")
        except Exception as e:
            print(f"[WARN] No se pudo copiar el PDF al portafolio: {e}")

    # 6. Generar Carta de Presentación si corresponde
    if provider.has_cover_letter():
        letter_filename = provider.get_cover_letter_filename()
        letter_output_path = os.path.join(config.OUTPUT_DIR, letter_filename)
        
        print(f"[INFO] Generando Carta de Presentación para {lang.upper()}...")
        letter_story = LetterStoryBuilder.build_letter_story(provider, styles)
        
        # Las cartas de presentación usan márgenes de 54 ptos para aspecto más formal
        letter_success = PDFWriter.compile_pdf(
            letter_output_path, 
            letter_story, 
            margins=(54, 54, 54, 54)
        )
        
        # Copiar al portafolio si fue exitoso
        if letter_success and os.path.exists(config.PORTFOLIO_CV_DIR):
            portfolio_letter_path = os.path.join(config.PORTFOLIO_CV_DIR, letter_filename)
            try:
                shutil.copy(letter_output_path, portfolio_letter_path)
                print(f"[SUCCESS] Copiada Carta al portafolio: {portfolio_letter_path}")
            except Exception as e:
                print(f"[WARN] No se pudo copiar la carta al portafolio: {e}")

def main():
    parser = argparse.ArgumentParser(description="Generador SOLID de Currículums para Enmanuel Jiménez.")
    parser.add_argument(
        "--lang", 
        choices=["es", "en", "pt"], 
        help="Idioma específico a generar: 'es' (Español), 'en' (Inglés), 'pt' (Português)."
    )
    parser.add_argument(
        "--all", 
        action="store_true", 
        help="Generar todos los idiomas disponibles (por defecto si no se especifica --lang)."
    )
    
    args = parser.parse_args()
    
    # Si no se especifica idioma o se pide --all, se generan todos
    if args.all or not args.lang:
        languages = ["es", "en", "pt"]
    else:
        languages = [args.lang]
        
    for lang in languages:
        generate_for_language(lang)
        
    print("\n[FINISHED] Todo el proceso ha finalizado correctamente.")

if __name__ == "__main__":
    main()
