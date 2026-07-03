import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def generar_curriculum(desktop_path):
    pdf_path = os.path.join(desktop_path, "CV_Enmanuel_Jimenez.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Colores personalizados
    c_primary = colors.HexColor("#1A365D")   # Azul Marino
    c_secondary = colors.HexColor("#2B6CB0") # Azul Medio
    c_text = colors.HexColor("#2D3748")      # Gris Oscuro
    c_text_light = colors.HexColor("#4A5568")# Gris Medio
    
    # Estilos de párrafo personalizados
    style_name = ParagraphStyle(
        'CV_Name',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=c_primary,
        spaceAfter=4
    )
    
    style_title = ParagraphStyle(
        'CV_Title',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=c_secondary,
        spaceAfter=8
    )
    
    style_contact = ParagraphStyle(
        'CV_Contact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=c_text_light
    )
    
    style_section = ParagraphStyle(
        'CV_Section',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=c_primary,
        spaceBefore=10,
        spaceAfter=4
    )
    
    style_body = ParagraphStyle(
        'CV_Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=c_text,
        alignment=TA_JUSTIFY,
        spaceAfter=6
    )
    
    style_entry_title = ParagraphStyle(
        'CV_EntryTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=c_primary
    )
    
    style_entry_subtitle = ParagraphStyle(
        'CV_EntrySubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=13,
        textColor=c_secondary
    )
    
    style_entry_date = ParagraphStyle(
        'CV_EntryDate',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=c_text_light,
        alignment=TA_RIGHT
    )
    
    style_bullet = ParagraphStyle(
        'CV_Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=c_text,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3
    )

    story = []
    
    # ------------------ ENCABEZADO / CONTACTO ------------------
    header_data = [
        [
            Paragraph("ENMANUEL JIMENEZ", style_name),
            Paragraph("<b>Email:</b> enmanuelejaj@gmail.com<br/><b>Tel:</b> +351 911 151 993", style_contact)
        ],
        [
            Paragraph("DESARROLLADOR SOFTWARE / FULL STACK JUNIOR", style_title),
            Paragraph("<b>GitHub:</b> github.com/ejaj94/Portfolio-Proyectos<br/><b>Ubicación:</b> Quarteira, Faro, Portugal", style_contact)
        ]
    ]
    
    header_table = Table(header_data, colWidths=[320, 200])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8, spaceBefore=4))
    
    # ------------------ PERFIL PROFESIONAL ------------------
    story.append(Paragraph("PERFIL PROFESIONAL", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    perfil_text = (
        "Desarrollador de Software Junior con sólida formación en ingeniería de software y arquitectura web. "
        "Especializado en el ecosistema de Python y JavaScript, con experiencia en el desarrollo de aplicaciones web "
        "completas, persistencia de datos con SQLAlchemy ORM y administración de bases de datos relacionales como MySQL y SQLite. "
        "Experto en la integración de APIs complejas (Stripe para pasarelas de pago, Twilio para notificaciones por SMS) y "
        "comunicación bidireccional en tiempo real con WebSockets (Socket.IO). Comprometido con la calidad del desarrollo mediante "
        "la aplicación rigurosa de principios SOLID, Clean Architecture, pruebas unitarias y flujos de trabajo organizados con Git/Gitflow."
    )
    story.append(Paragraph(perfil_text, style_body))
    story.append(Spacer(1, 4))
    
    # ------------------ HABILIDADES TÉCNICAS ------------------
    story.append(Paragraph("HABILIDADES TÉCNICAS", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    
    hab_data = [
        [Paragraph("<b>Lenguajes:</b>", style_body), Paragraph("Python, JavaScript (ES6+), SQL, HTML5, CSS3", style_body)],
        [Paragraph("<b>Frameworks y ORMs:</b>", style_body), Paragraph("Flask, SQLAlchemy, Flask-SQLAlchemy", style_body)],
        [Paragraph("<b>Bases de Datos:</b>", style_body), Paragraph("MySQL, SQLite, Gestión de bases de datos relacionales", style_body)],
        [Paragraph("<b>APIs e Integraciones:</b>", style_body), Paragraph("Stripe API (Pagos), Twilio API (SMS), WebSockets (Flask-SocketIO), SMTP (Gmail)", style_body)],
        [Paragraph("<b>Herramientas y Métodos:</b>", style_body), Paragraph("Git, GitHub, Gitflow, Arquitectura Limpia, Principios SOLID, Scrum / Ágil", style_body)],
    ]
    hab_table = Table(hab_data, colWidths=[130, 390])
    hab_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(hab_table)
    story.append(Spacer(1, 8))
    
    # ------------------ EXPERIENCIA LABORAL / PROYECTOS DESTACADOS ------------------
    story.append(Paragraph("EXPERIENCIA Y PROYECTOS DESTACADOS", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=8, spaceBefore=2))
    
    # Proyecto 1: Com Cheiro de Amor
    p1_header = [
        [Paragraph("Desarrollador Web Frontend (Freelance)", style_entry_title), Paragraph("2026", style_entry_date)],
        [Paragraph("Sitio Web Comercial 'Com Cheiro de Amor' | Loulé, Portugal", style_entry_subtitle), Paragraph("", style_entry_date)]
    ]
    p1_table = Table(p1_header, colWidths=[370, 150])
    p1_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(p1_table)
    story.append(Spacer(1, 3))
    story.append(Paragraph("&bull; Diseñé y desarrolló desde cero el sitio web comercial interactivo y responsivo para una marca local de productos artesanales (velas y jabones) en Portugal.", style_bullet))
    story.append(Paragraph("&bull; Implementé lógica compleja en frontend usando <b>JavaScript nativo (Vanilla JS)</b> y maquetación avanzada con <b>HTML5</b> y <b>CSS3</b> sin frameworks para asegurar tiempos de carga óptimos.", style_bullet))
    story.append(Paragraph("&bull; Estructuré el catálogo de productos enfocado en la experiencia de usuario (UX) y optimización móvil (Mobile-First).", style_bullet))
    story.append(Spacer(1, 8))
    
    # Proyecto 2: Plataforma de Entregas
    p2_header = [
        [Paragraph("Desarrollador Full Stack (Proyecto de Portafolio)", style_entry_title), Paragraph("2025 - 2026", style_entry_date)],
        [Paragraph("Plataforma de Entregas en Tiempo Real (Delivery App)", style_entry_subtitle), Paragraph("", style_entry_date)]
    ]
    p2_table = Table(p2_header, colWidths=[370, 150])
    p2_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(p2_table)
    story.append(Spacer(1, 3))
    story.append(Paragraph("&bull; Creé una aplicación web robusta y completa usando **Python (Flask)** y **Flask-SQLAlchemy (SQLite)** para conectar clientes, restaurantes y repartidores.", style_bullet))
    story.append(Paragraph("&bull; Diseñé un módulo de seguimiento en tiempo real de los repartidores mediante WebSockets utilizando **Flask-SocketIO**.", style_bullet))
    story.append(Paragraph("&bull; Integré la pasarela de pagos seguros **Stripe API** para la gestión de transacciones de compra.", style_bullet))
    story.append(Paragraph("&bull; Implementé notificaciones automáticas por SMS a través de la API de **Twilio** y soporte internacional con **Flask-Babel**.", style_bullet))
    story.append(Spacer(1, 15))
    
    # Forzamos salto de página para mantener la estructura limpia en 2 páginas
    story.append(PageBreak())
    
    # PÁGINA 2
    story.append(Paragraph("EXPERIENCIA Y PROYECTOS DESTACADOS (Cont.)", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=8, spaceBefore=2))
    
    # Proyecto 3: Gestor Pro DB
    p3_header = [
        [Paragraph("Desarrollador Backend (Proyecto de Portafolio)", style_entry_title), Paragraph("2025", style_entry_date)],
        [Paragraph("Gestor Pro DB - Sistema de Gestión de Usuarios", style_entry_subtitle), Paragraph("", style_entry_date)]
    ]
    p3_table = Table(p3_header, colWidths=[370, 150])
    p3_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(p3_table)
    story.append(Spacer(1, 3))
    story.append(Paragraph("&bull; Diseñé y construí un sistema de backend en consola para la gestión de usuarios conectado a una base de datos relacional **MySQL**.", style_bullet))
    story.append(Paragraph("&bull; Estructuré el software aplicando rigurosamente los principios **SOLID** y una arquitectura limpia por capas (**Repository / Service / UI**).", style_bullet))
    story.append(Paragraph("&bull; Desarrollé un servicio de persistencia mediante **SQLAlchemy ORM** para encapsular consultas y asegurar la integridad de los datos.", style_bullet))
    story.append(Paragraph("&bull; Automaticé la generación de reportes de auditoría en formato **PDF (ReportLab)** con el estado de la base de datos y su envío por correo mediante el protocolo **SMTP (Gmail)**.", style_bullet))
    story.append(Spacer(1, 8))
    
    # Otros Proyectos de Desarrollo
    story.append(Paragraph("Otros Proyectos del Portafolio Personal", style_entry_title))
    story.append(Paragraph("&bull; **Monitor de Precios de Cripto y Divisas:** Aplicación en Python que consume APIs de mercados financieros para analizar y graficar tendencias de precios.", style_bullet))
    story.append(Paragraph("&bull; **Network Security Scanner:** Script en Python para escaneo básico de vulnerabilidades y puertos en redes locales para tareas de diagnóstico.", style_bullet))
    story.append(Paragraph("&bull; **Organizador de Archivos Inteligente:** Herramienta de automatización de sistema operativo en Python para clasificación y ordenación de ficheros.", style_bullet))
    story.append(Paragraph("&bull; **Web Scraping Tool:** Desarrollo de scripts para extracción e indexación automatizada de información de sitios web públicos.", style_bullet))
    story.append(Paragraph("&bull; **Calculadora de Calorías / TMB:** Aplicación de salud y fitness para la estimación de tasa metabólica basal según parámetros médicos.", style_bullet))
    story.append(Spacer(1, 10))
    
    # ------------------ FORMACIÓN ACADÉMICA ------------------
    story.append(Paragraph("FORMACIÓN ACADÉMICA", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    
    edu_header = [
        [Paragraph("Máster en Desarrollo de Software Full Stack", style_entry_title), Paragraph("2024 - 2025", style_entry_date)],
        [Paragraph("Bootcamp Tecnológico ConquerBlocks", style_entry_subtitle), Paragraph("", style_entry_date)]
    ]
    edu_table = Table(edu_header, colWidths=[370, 150])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(edu_table)
    story.append(Spacer(1, 3))
    story.append(Paragraph("&bull; Programa intensivo de más de 600 horas de código enfocado en arquitectura de software, backend con Python y SQL, desarrollo frontend con JavaScript, metodologías ágiles (Scrum) y despliegue en producción.", style_bullet))
    story.append(Spacer(1, 10))
    
    # ------------------ IDIOMAS ------------------
    story.append(Paragraph("IDIOMAS", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    
    idiomas_data = [
        [Paragraph("&bull; <b>Español:</b> Nativo", style_body), Paragraph("&bull; <b>Inglés:</b> Avanzado (Competencia profesional completa)", style_body), Paragraph("&bull; <b>Portugués:</b> Avanzado (Competencia conversacional y escrita)", style_body)]
    ]
    idiomas_table = Table(idiomas_data, colWidths=[120, 240, 160])
    idiomas_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(idiomas_table)

    doc.build(story)
    print("[OK] CV PDF generado exitosamente.")

def generar_carta_presentacion(desktop_path):
    pdf_path = os.path.join(desktop_path, "Carta_Presentacion_Enmanuel_Jimenez.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Colores
    c_primary = colors.HexColor("#1A365D")
    c_secondary = colors.HexColor("#2B6CB0")
    c_text = colors.HexColor("#2D3748")
    
    style_header_name = ParagraphStyle(
        'Letter_Name',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=c_primary,
        spaceAfter=2
    )
    
    style_header_title = ParagraphStyle(
        'Letter_Title',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=c_secondary,
        spaceAfter=15
    )
    
    style_contact = ParagraphStyle(
        'Letter_Contact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#4A5568"),
        alignment=TA_RIGHT
    )
    
    style_body = ParagraphStyle(
        'Letter_Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=15,
        textColor=c_text,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    )
    
    style_salutation = ParagraphStyle(
        'Letter_Salutation',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=c_primary,
        spaceAfter=10
    )

    story = []
    
    # Encabezado de la Carta
    header_data = [
        [
            Paragraph("<b>ENMANUEL JIMENEZ</b>", style_header_name),
            Paragraph("Avenida Francisco Sa Carneiro<br/>Quarteira, Portugal<br/>+351 911 151 993<br/>enmanuelejaj@gmail.com", style_contact)
        ]
    ]
    header_table = Table(header_data, colWidths=[240, 240])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Paragraph("Desarrollador Software / Full Stack Junior", style_header_title))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceAfter=20, spaceBefore=0))
    
    # Fecha y destinatario
    story.append(Paragraph("Quarteira, Faro, Portugal<br/>15 de junio de 2026", ParagraphStyle('Letter_Date', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=9, spaceAfter=15)))
    
    story.append(Paragraph("<b>A la atención del Equipo de Selección / Responsable de Tecnología</b>", style_salutation))
    
    # Cuerpo de la carta
    p1 = (
        "Les escribo con gran entusiasmo para presentar mi candidatura a la posición de Desarrollador Software "
        "(Backend / Full Stack Junior) en su organización. Como desarrollador graduado del Bootcamp Full Stack de "
        "ConquerBlocks, residente en Portugal y con dominio avanzado de inglés, portugués y español, estoy preparado "
        "para incorporarme de inmediato a su equipo tecnológico de forma remota o híbrida."
    )
    story.append(Paragraph(p1, style_body))
    
    p2 = (
        "A lo largo de mi formación y desarrollo autónomo, he consolidado habilidades en la creación de aplicaciones "
        "web robustas utilizando Python (Flask) y JavaScript. Entre mis logros más destacados se encuentra el desarrollo "
        "completo de una plataforma de entregas en tiempo real (Delivery App), donde implementé comunicación bidireccional "
        "mediante WebSockets (Flask-SocketIO), integré pasarelas de pago seguras con la API de Stripe y automaticé avisos "
        "por SMS con Twilio. Asimismo, poseo un fuerte dominio de bases de datos relacionales (MySQL y SQLite) gestionadas "
        "a través de SQLAlchemy ORM, estructuradas bajo arquitecturas limpias (patrón Repository/Service) y principios SOLID."
    )
    story.append(Paragraph(p2, style_body))
    
    p3 = (
        "Además de mis proyectos personales, cuento con experiencia trabajando para clientes reales, como el diseño y "
        "desarrollo del sitio web comercial 'Com Cheiro de Amor' en Portugal. Este proyecto me permitió dominar JavaScript "
        "nativo, HTML5 y CSS3 para construir una interfaz altamente responsiva e interactiva enfocada en la conversión del usuario."
    )
    story.append(Paragraph(p3, style_body))
    
    p4 = (
        "Lo que me distingue como desarrollador junior es mi rigurosidad con la calidad del código: utilizo Git y flujos "
        "de trabajo Gitflow para mantener repositorios limpios y seguros, y diseño pruebas unitarias para garantizar el "
        "correcto funcionamiento de cada módulo. Mi capacidad multilingüe me permite además encajar perfectamente en equipos "
        "internacionales y dinámicos."
    )
    story.append(Paragraph(p4, style_body))
    
    p5 = (
        "Agradezco de antemano el tiempo dedicado a evaluar mi currículum adjunto. Estaría encantado de mantener una "
        "entrevista para profundizar en cómo mi perfil y proyectos pueden contribuir al éxito de sus próximos desarrollos."
    )
    story.append(Paragraph(p5, style_body))
    
    story.append(Spacer(1, 15))
    story.append(Paragraph("Atentamente,", style_body))
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Enmanuel Jiménez</b>", style_salutation))
    story.append(Paragraph("Desarrollador Software / Full Stack", ParagraphStyle('Letter_Footer', parent=styles['Normal'], fontName='Helvetica', fontSize=9, textColor=colors.HexColor("#4A5568"))))

    doc.build(story)
    print("[OK] Carta de presentacion PDF generada exitosamente.")

def load_env(env_path=".env"):
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip()

if __name__ == "__main__":
    # Cargar variables de entorno del archivo .env
    script_dir = os.path.dirname(os.path.abspath(__file__))
    load_env(os.path.join(script_dir, ".env"))
    
    desktop = os.environ.get("OUTPUT_DIR", r"C:\Users\ANGEL RAFAEL\Desktop")
    if not os.path.exists(desktop):
        desktop = os.path.expanduser("~/Desktop")
    
    print(f"Generando PDFs en: {desktop}")
    
    try:
        generar_curriculum(desktop)
        generar_carta_presentacion(desktop)
        print("[SUCCESS] Proceso finalizado con exito.")
    except Exception as e:
        print(f"[ERROR] Error durante la generacion: {e}", file=sys.stderr)
        sys.exit(1)
