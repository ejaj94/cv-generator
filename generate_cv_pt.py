import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Image, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from pypdf import PdfReader, PdfWriter

def generar_curriculum_pt(output_dir, photo_path, cert_dir):
    temp_pdf_path = os.path.join(output_dir, "CV_Enmanuel_Jimenez_PT_Temp.pdf")
    final_pdf_path = os.path.join(output_dir, "CV_Enmanuel_Jimenez_PT.pdf")
    
    # Configuración del documento ReportLab
    doc = SimpleDocTemplate(
        temp_pdf_path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Cores personalizadas (Esquema de azul marinho e cinzas profissionais)
    c_primary = colors.HexColor("#0F2042")   # Azul Escuro / Slate Blue
    c_secondary = colors.HexColor("#2A6F97") # Azul Médio
    c_text = colors.HexColor("#2B2D42")      # Gris / Cinza Escuro
    c_text_light = colors.HexColor("#5C677D")# Cinza Médio
    
    # Estilos de parágrafo personalizados
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
        fontSize=11.5,
        leading=15,
        textColor=c_secondary,
        spaceAfter=6
    )
    
    style_contact = ParagraphStyle(
        'CV_Contact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=c_text_light
    )
    
    style_section = ParagraphStyle(
        'CV_Section',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=16,
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
        spaceAfter=5
    )
    
    style_entry_title = ParagraphStyle(
        'CV_EntryTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13.5,
        textColor=c_primary
    )
    
    style_entry_subtitle = ParagraphStyle(
        'CV_EntrySubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=12.5,
        textColor=c_secondary
    )
    
    style_entry_date = ParagraphStyle(
        'CV_EntryDate',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12.5,
        textColor=c_text_light,
        alignment=TA_RIGHT
    )
    
    style_bullet = ParagraphStyle(
        'CV_Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=c_text,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3
    )

    story = []
    
    # ------------------ ENCABEZADO CON FOTO ------------------
    # Preparar datos de contacto
    contact_text = (
        "<b>Telemóvel:</b> +351 911 151 993<br/>"
        "<b>E-mail:</b> enmanuelejaj@gmail.com<br/>"
        "<b>Morada:</b> Rua 1 de Maio, Número 4, Quarteira, Portugal<br/>"
        "<b>GitHub:</b> github.com/ejaj94<br/>"
        "<b>LinkedIn:</b> linkedin.com/in/enmanuel-jimenez-dev"
    )
    
    header_left = [
        Paragraph("ENMANUEL JIMÉNEZ", style_name),
        Paragraph("SISTEMAS COMPUTACIONAIS | DISTRIBUIÇÃO E OPERADOR DE ARMAZÉM", style_title),
        Paragraph(contact_text, style_contact)
    ]
    
    # Insertar foto de perfil
    try:
        profile_img = Image(photo_path, width=80, height=96)
        # Borda para a imagem
        profile_img.hAlign = 'RIGHT'
    except Exception as e:
        print(f"[WARN] Não foi possível carregar a imagem de perfil: {e}")
        profile_img = Paragraph("[FOTO]", style_contact)
        
    header_data = [
        [header_left, profile_img]
    ]
    
    # Tabela de cabeçalho (esquerda: dados, direita: foto)
    header_table = Table(header_data, colWidths=[420, 100])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=8, spaceBefore=4))
    
    # ------------------ PERFIL PROFISSIONAL ------------------
    story.append(Paragraph("PERFIL PROFISSIONAL", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    perfil_text = (
        "Profissional multidisciplinar com um perfil versátil que combina 2 anos de experiência como distribuidor e "
        "entregador de encomendas de última milha em Portugal (trabalhando com empresas líderes do setor como DPD, "
        "GLS, Eco Scooting e Correos Express) com uma sólida experiência em operações de armazém e logística. Em paralelo, "
        "possuo uma forte preparação técnica em computação e informática, atuando como Programador de Software Web "
        "(Full Stack / Backend) com domínio absoluto na administração de múltiplos sistemas operativos (Windows, Linux, "
        "macOS), redes, bases de dados relacionais e automatização de tarefas. Especialista em otimizar operações "
        "através da digitalização, gestão de fluxos de inventário e desenvolvimento de soluções de software à medida."
    )
    story.append(Paragraph(perfil_text, style_body))
    story.append(Spacer(1, 4))
    
    # ------------------ EXPERIÊNCIA PROFISSIONAL ------------------
    story.append(Paragraph("EXPERIÊNCIA PROFISSIONAL", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    
    # Trabalho 1: Entregador / Courier
    t1_header = [
        [Paragraph("Operador de Logística e Distribuição (Última Milha)", style_entry_title), Paragraph("2024 - Presente", style_entry_date)],
        [Paragraph("Distribuidor / Entregador (DPD, GLS, Eco Scooting e Correos Express) | Algarve, Portugal", style_entry_subtitle), Paragraph("", style_entry_date)]
    ]
    t1_table = Table(t1_header, colWidths=[400, 120])
    t1_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t1_table)
    story.append(Spacer(1, 3))
    story.append(Paragraph("&bull; Responsável pela gestão, triagem prévia e entrega rápida e segura de mercadorias provenientes do comércio eletrónico (e-commerce).", style_bullet))
    story.append(Paragraph("&bull; Distribuição de encomendas com cobertura nas rotas do Algarve: <b>Quarteira, Albufeira, Guia, Faro, Vilamoura e Almancil</b>.", style_bullet))
    story.append(Paragraph("&bull; Planeamento inteligente e otimização de rotas diárias de entrega através de GPS e software de navegação para maximizar a produtividade e pontualidade.", style_bullet))
    story.append(Paragraph("&bull; Gestão digital de guias de transporte (alvarás), registo de incidentes e uso de sistemas eletrónicos de rastreamento (PDA).", style_bullet))
    story.append(Paragraph("&bull; Atendimento direto ao cliente, assegurando altos padrões de satisfação e resolução de dúvidas no ato de entrega.", style_bullet))
    story.append(Spacer(1, 6))
    
    # Trabalho 2: Operador de Armazém
    t2_header = [
        [Paragraph("Operador de Armazém e Logística", style_entry_title), Paragraph("2023 - 2024", style_entry_date)],
        [Paragraph("Gestão de Fluxos Logísticos | Quarteira, Faro, Portugal", style_entry_subtitle), Paragraph("", style_entry_date)]
    ]
    t2_table = Table(t2_header, colWidths=[400, 120])
    t2_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t2_table)
    story.append(Spacer(1, 3))
    story.append(Paragraph("&bull; Receção, descarga e conferência física e documental de mercadoria de entrada, assegurando o controlo de qualidade e a identificação de danos.", style_bullet))
    story.append(Paragraph("&bull; Preparação de encomendas (<i>picking</i> e <i>packing</i>) com o auxílio de leitores de código de barras e terminais de radiofrequência.", style_bullet))
    story.append(Paragraph("&bull; Introdução de dados e controlo contínuo de stock nos sistemas informáticos de gestão de armazém (WMS).", style_bullet))
    story.append(Paragraph("&bull; Organização e arrumação física do armazém, carga/descarga de camiões e cumprimento rigoroso das normas de higiene e segurança no trabalho.", style_bullet))
    story.append(Spacer(1, 10))
    
    story.append(PageBreak()) # Salto para manter as 2 páginas estruturadas de forma limpa
    
    # PÁGINA 2
    story.append(Paragraph("EXPERIÊNCIA PROFISSIONAL (Cont.)", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    
    # Trabalho 3: Programador Web (Projetos / Freelance)
    t3_header = [
        [Paragraph("Programador de Software Web (Freelance e Portfólio)", style_entry_title), Paragraph("2025 - 2026", style_entry_date)],
        [Paragraph("Desenvolvimento Full Stack e Soluções Tecnológicas | Quarteira, Portugal", style_entry_subtitle), Paragraph("", style_entry_date)]
    ]
    t3_table = Table(t3_header, colWidths=[400, 120])
    t3_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t3_table)
    story.append(Spacer(1, 3))
    story.append(Paragraph("&bull; <b>Com Cheiro de Amor (Website Comercial):</b> Concebi e programei uma montra online interativa e totalmente responsiva para uma marca local de velas e sabonetes, aplicando <b>JavaScript nativo (Vanilla JS)</b>, HTML5 e CSS3 sem frameworks, otimizando o SEO e o desempenho.", style_bullet))
    story.append(Paragraph("&bull; <b>Delivery App (Plataforma de Entregas):</b> Desenvolvi uma aplicação web completa com **Python (Flask)** e **SQLite**. Programei o rastreamento em tempo real dos entregadores com WebSockets (**Flask-SocketIO**), integrei a API do **Stripe** para pagamentos e a API do **Twilio** para alertas por SMS automático.", style_bullet))
    story.append(Paragraph("&bull; <b>Gestor Pro DB:</b> Criei uma ferramenta backend em consola ligada a uma base de dados relacional **MySQL**. Desenvolvi a lógica utilizando **SQLAlchemy ORM**, arquitetura limpa (Repository/Service) e princípios **SOLID**, incluindo relatórios **PDF (ReportLab)** enviados por email via protocolo **SMTP (Gmail)**.", style_bullet))
    story.append(Spacer(1, 6))
    
    # Outros Projetos
    story.append(Paragraph("Outros Projetos de Portfólio Técnico", style_entry_title))
    story.append(Paragraph("&bull; **Monitor de Preços de Cripto e Divisas:** Aplicação em Python que consome APIs financeiras para exibir gráficos de tendências em tempo real.", style_bullet))
    story.append(Paragraph("&bull; **Network Security Scanner:** Script em Python para diagnóstico e varrimento básico de portas e vulnerabilidades em redes locais.", style_bullet))
    story.append(Paragraph("&bull; **Organizador de Ficheiros Inteligente:** Script de automação em Python para classificação autónoma de pastas e documentos no SO.", style_bullet))
    story.append(Spacer(1, 6))

    # ------------------ COMPETÊNCIAS INFORMÁTICAS E DE HARDWARE ------------------
    story.append(Paragraph("COMPETÊNCIAS INFORMÁTICAS E DE COMPUTAÇÃO", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    
    comp_data = [
        [Paragraph("<b>Sistemas Operativos:</b>", style_body), Paragraph("Linux/Ubuntu (uso profundo da consola Bash e comandos, gestão de servidores), Windows (PowerShell scripting e automatização de SO) e macOS.", style_body)],
        [Paragraph("<b>Linguagens & Web:</b>", style_body), Paragraph("Python, JavaScript (ES6+), SQL, HTML5, CSS3, JSON.", style_body)],
        [Paragraph("<b>Bases de Dados:</b>", style_body), Paragraph("MySQL, SQLite, gestão relacional e mapeamento avançado com SQLAlchemy ORM.", style_body)],
        [Paragraph("<b>Ferramentas & APIs:</b>", style_body), Paragraph("Git, GitHub, Gitflow, Stripe API, Twilio API, WebSockets (SocketIO), SMTP, ReportLab.", style_body)]
    ]
    comp_table = Table(comp_data, colWidths=[130, 390])
    comp_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(comp_table)
    story.append(Spacer(1, 6))

    # ------------------ EDUCAÇÃO E CERTIFICADOS ------------------
    story.append(Paragraph("EDUCAÇÃO E CERTIFICADOS", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    
    edu_header = [
        [Paragraph("Mestrado em Desenvolvimento de Software Full Stack", style_entry_title), Paragraph("2024 - 2025", style_entry_date)],
        [Paragraph("Bootcamp Tecnológico ConquerBlocks", style_entry_subtitle), Paragraph("", style_entry_date)]
    ]
    edu_table = Table(edu_header, colWidths=[400, 120])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(edu_table)
    story.append(Spacer(1, 3))
    story.append(Paragraph("&bull; Programa intensivo com mais de 600 horas de código abrangendo arquitetura, bases de dados relacionais, desenvolvimento web, metodologias ágeis e boas práticas (Clean Code).", style_bullet))
    story.append(Spacer(1, 4))
    
    # Lista de Certificados
    story.append(Paragraph("<b>Certificados de Formação Profissional (ConquerBlocks):</b>", style_body))
    cert_list = [
        "1. Certificado em Linux e a Terminal (Gestão por consola)",
        "2. Certificado em Git e GitHub (Controlo de versões avançado e Gitflow)",
        "3. Certificado em Python Inicial (Lógica e algoritmos)",
        "4. Certificado em Python Avançado (Estruturas complexas e POO)",
        "5. Certificado em SQL (Modelação e consultas relacionais)",
        "6. Certificado em Uso de ORMs em Python (SQLAlchemy e persistência)",
        "7. Certificado em Princípios SOLID e Acesso a Bases de Dados (Clean Architecture)",
        "8. Certificado em Pseudocódigo (Lógica algorítmica)"
    ]
    for c in cert_list:
        story.append(Paragraph(f"&bull; {c}", style_bullet))
    story.append(Spacer(1, 6))

    # ------------------ IDIOMAS ------------------
    story.append(Paragraph("IDIOMAS", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=4, spaceBefore=2))
    
    idiomas_data = [
        [Paragraph("&bull; <b>Espanhol:</b> Nativo", style_body), Paragraph("&bull; <b>Inglês:</b> Avançado (Fluência profissional)", style_body), Paragraph("&bull; <b>Português:</b> Avançado (Fluência conversacional e escrita)", style_body)]
    ]
    idiomas_table = Table(idiomas_data, colWidths=[120, 220, 180])
    idiomas_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(idiomas_table)
    
    # ------------------ CERTIFICADO EN IMAGEN (PÁGINA 3) ------------------
    # Añadimos el certificado de python avanzado que es una imagen (.png)
    story.append(PageBreak())
    story.append(Paragraph("ANEXO: CERTIFICADOS DE PORTFÓLIO", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=12, spaceBefore=2))
    
    python_adv_img_path = os.path.join(cert_dir, "Certificado de python avanzado..png")
    if os.path.exists(python_adv_img_path):
        try:
            # Escalamos el certificado para que quepa bien en la página A4 manteniendo proporción
            cert_img = Image(python_adv_img_path, width=480, height=340)
            cert_img.hAlign = 'CENTER'
            story.append(Paragraph("<b>Certificado de Python Avançado - ConquerBlocks:</b>", style_body))
            story.append(Spacer(1, 8))
            story.append(cert_img)
        except Exception as e:
            print(f"[WARN] Erro ao carregar imagem de certificado: {e}")
            story.append(Paragraph(f"[Imagem do Certificado de Python Avançado: {python_adv_img_path}]", style_body))
    else:
        print(f"[WARN] Não encontrado: {python_adv_img_path}")
        story.append(Paragraph("[Certificado de Python Avançado - Imagem não encontrada]", style_body))
        
    doc.build(story)
    print("[OK] PDF base gerado com ReportLab.")

def merge_cv_with_certificates(temp_pdf, cert_dir, final_pdf):
    writer = PdfWriter()
    
    # Añadir las páginas del CV base (CV + certificado de python avanzado)
    reader_cv = PdfReader(temp_pdf)
    for page in reader_cv.pages:
        writer.add_page(page)
        
    # Lista de los otros certificados en formato PDF
    certificados_pdf = [
        "Certificado linux y la terminal..pdf",
        "Certificado de git y github..pdf",
        "Certificado de Python Inicial..pdf",
        "Certficado de SQL.pdf",
        "Certificado uso de orms en python.pdf",
        "Certificado principios solid y acceso a bases de datos ..pdf",
        "Cerificado pseudocodigo.pdf"
    ]
    
    for filename in certificados_pdf:
        filepath = os.path.join(cert_dir, filename)
        if os.path.exists(filepath):
            try:
                reader_cert = PdfReader(filepath)
                # Añadimos todas las páginas de cada certificado (normalmente es 1 página)
                for page in reader_cert.pages:
                    writer.add_page(page)
                print(f"[OK] Certificado adicionado ao PDF final: {filename}")
            except Exception as e:
                print(f"[ERROR] Erro ao ler certificado {filename}: {e}")
        else:
            print(f"[WARN] Ficheiro de certificado não encontrado: {filepath}")
            
    with open(final_pdf, "wb") as f_out:
        writer.write(f_out)
    print(f"[SUCCESS] PDF completo gerado em: {final_pdf}")

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
    
    # Resolver rutas
    photo = os.environ.get("PROFILE_PHOTO_PATH", os.path.join(script_dir, "assets", "profile.jpg"))
    certs = os.environ.get("CERTIFICATES_DIR", r"C:\Users\ANGEL RAFAEL\Desktop\Portfolio de programacion\Certificados")
    desktop = os.environ.get("OUTPUT_DIR", r"C:\Users\ANGEL RAFAEL\Desktop")
    portfolio_cv_dir = os.environ.get("PORTFOLIO_CV_DIR", r"C:\Users\ANGEL RAFAEL\Desktop\Portfolio de programacion\CV")
    
    if not os.path.exists(desktop):
        desktop = os.path.expanduser("~/Desktop")
        
    # 1. Generar PDF temporal
    generar_curriculum_pt(desktop, photo, certs)
    
    # 2. Combinar con los otros certificados
    temp_pdf = os.path.join(desktop, "CV_Enmanuel_Jimenez_PT_Temp.pdf")
    final_pdf_desktop = os.path.join(desktop, "CV_Enmanuel_Jimenez_PT.pdf")
    
    merge_cv_with_certificates(temp_pdf, certs, final_pdf_desktop)
    
    # 3. Copiar el PDF final al directorio de portafolio CV
    if os.path.exists(portfolio_cv_dir):
        final_pdf_portfolio = os.path.join(portfolio_cv_dir, "CV_Enmanuel_Jimenez_PT.pdf")
        try:
            import shutil
            shutil.copy(final_pdf_desktop, final_pdf_portfolio)
            print(f"[SUCCESS] Copiado PDF final ao portfólio em: {final_pdf_portfolio}")
        except Exception as e:
            print(f"[ERROR] Não foi possível copiar para a pasta de portfólio: {e}")
            
    # Eliminar PDF temporal
    try:
        if os.path.exists(temp_pdf):
            os.remove(temp_pdf)
            print("[OK] Ficheiro temporal removido.")
    except Exception as e:
        print(f"[WARN] Erro ao remover ficheiro temporal: {e}")
