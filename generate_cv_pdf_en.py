import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def generar_curriculum_en(desktop_path):
    pdf_path = os.path.join(desktop_path, "Resume_Enmanuel_Jimenez.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom colors
    c_primary = colors.HexColor("#1A365D")   # Deep Slate Blue
    c_secondary = colors.HexColor("#2B6CB0") # Medium Blue
    c_text = colors.HexColor("#2D3748")      # Dark Grey
    c_text_light = colors.HexColor("#4A5568")# Medium Grey
    
    # Custom paragraph styles
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
    
    # ------------------ HEADER / CONTACT ------------------
    header_data = [
        [
            Paragraph("ENMANUEL JIMENEZ", style_name),
            Paragraph("<b>Email:</b> enmanuelejaj@gmail.com<br/><b>Tel:</b> +351 911 151 993", style_contact)
        ],
        [
            Paragraph("JUNIOR SOFTWARE DEVELOPER / FULL STACK", style_title),
            Paragraph("<b>GitHub:</b> github.com/ejaj94/Portfolio-Proyectos<br/><b>Location:</b> Quarteira, Faro, Portugal", style_contact)
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
    
    # ------------------ PROFESSIONAL SUMMARY ------------------
    story.append(Paragraph("PROFESSIONAL SUMMARY", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    perfil_text = (
        "Junior Software Developer with a solid background in software engineering and web architecture. "
        "Specialized in the Python and JavaScript ecosystems, with hands-on experience developing full-stack web "
        "applications, handling data persistence with SQLAlchemy ORM, and managing relational databases like MySQL and SQLite. "
        "Expert at integrating complex APIs (Stripe for payment gateways, Twilio for SMS notifications) and "
        "implementing bi-directional real-time communication using WebSockets (Socket.IO). Committed to development quality "
        "through the rigorous application of SOLID principles, Clean Architecture, unit testing, and organized version control workflows with Git/Gitflow."
    )
    story.append(Paragraph(perfil_text, style_body))
    story.append(Spacer(1, 4))
    
    # ------------------ TECHNICAL SKILLS ------------------
    story.append(Paragraph("TECHNICAL SKILLS", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    
    hab_data = [
        [Paragraph("<b>Languages:</b>", style_body), Paragraph("Python, JavaScript (ES6+), SQL, HTML5, CSS3", style_body)],
        [Paragraph("<b>Frameworks & ORMs:</b>", style_body), Paragraph("Flask, SQLAlchemy, Flask-SQLAlchemy", style_body)],
        [Paragraph("<b>Databases:</b>", style_body), Paragraph("MySQL, SQLite, Relational database management", style_body)],
        [Paragraph("<b>APIs & Integrations:</b>", style_body), Paragraph("Stripe API (Payments), Twilio API (SMS), WebSockets (Flask-SocketIO), SMTP (Gmail)", style_body)],
        [Paragraph("<b>Tools & Methods:</b>", style_body), Paragraph("Git, GitHub, Gitflow, Clean Architecture, SOLID Principles, Scrum / Agile", style_body)],
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
    
    # ------------------ WORK EXPERIENCE & PORTFOLIO ------------------
    story.append(Paragraph("EXPERIENCE & KEY PROJECTS", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=8, spaceBefore=2))
    
    # Project 1: Com Cheiro de Amor
    p1_header = [
        [Paragraph("Junior Frontend Web Developer (Freelance)", style_entry_title), Paragraph("2026", style_entry_date)],
        [Paragraph("Commercial Website 'Com Cheiro de Amor' | Loule, Portugal", style_entry_subtitle), Paragraph("", style_entry_date)]
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
    story.append(Paragraph("&bull; Designed and developed from scratch an interactive, responsive showcase website for a local handmade soap and candle brand in Portugal.", style_bullet))
    story.append(Paragraph("&bull; Implemented complex frontend logic using <b>Vanilla JavaScript</b> and advanced styling with <b>HTML5</b> and <b>CSS3</b> without frameworks to ensure optimal page load times.", style_bullet))
    story.append(Paragraph("&bull; Structured the product catalog focusing on user experience (UX) and mobile-first optimization.", style_bullet))
    story.append(Spacer(1, 8))
    
    # Project 2: Plataforma de Entregas
    p2_header = [
        [Paragraph("Full Stack Developer (Portfolio Project)", style_entry_title), Paragraph("2025 - 2026", style_entry_date)],
        [Paragraph("Real-Time Delivery Platform (Delivery App)", style_entry_subtitle), Paragraph("", style_entry_date)]
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
    story.append(Paragraph("&bull; Built a robust, complete web application using **Python (Flask)** and **Flask-SQLAlchemy (SQLite)** to connect clients, restaurants, and couriers.", style_bullet))
    story.append(Paragraph("&bull; Designed a live courier tracking module with WebSockets utilizing **Flask-SocketIO** for real-time state synchronization.", style_bullet))
    story.append(Paragraph("&bull; Integrated **Stripe API** for secure and automated payment transactions.", style_bullet))
    story.append(Paragraph("&bull; Implemented automated **Twilio SMS notifications** and internationalization support with **Flask-Babel**.", style_bullet))
    story.append(Spacer(1, 15))
    
    # Page break for structured 2-page flow
    story.append(PageBreak())
    
    # PAGE 2
    story.append(Paragraph("EXPERIENCE & KEY PROJECTS (Cont.)", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=8, spaceBefore=2))
    
    # Project 3: Gestor Pro DB
    p3_header = [
        [Paragraph("Backend Developer (Portfolio Project)", style_entry_title), Paragraph("2025", style_entry_date)],
        [Paragraph("Gestor Pro DB - User Management System", style_entry_subtitle), Paragraph("", style_entry_date)]
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
    story.append(Paragraph("&bull; Designed and built a console-based backend system for user management connected to a **MySQL** database.", style_bullet))
    story.append(Paragraph("&bull; Structured the software strictly applying **SOLID principles** and a layered Clean Architecture (**Repository / Service / UI**).", style_bullet))
    story.append(Paragraph("&bull; Developed a persistence layer using **SQLAlchemy ORM** to encapsulate queries and ensure database integrity.", style_bullet))
    story.append(Paragraph("&bull; Automated the generation of audit reports in **PDF format (ReportLab)** and their delivery via **SMTP (Gmail)** after CRUD operations.", style_bullet))
    story.append(Spacer(1, 8))
    
    # Other Projects Summary
    story.append(Paragraph("Other Portfolio Projects", style_entry_title))
    story.append(Paragraph("&bull; **Crypto & Currency Price Monitor:** Python application consuming financial APIs to analyze and chart market trends.", style_bullet))
    story.append(Paragraph("&bull; **Network Security Scanner:** Python tool performing vulnerability and port scanning on local networks for diagnostics.", style_bullet))
    story.append(Paragraph("&bull; **Smart File Organizer:** OS automation script in Python to classify and clean directory structures.", style_bullet))
    story.append(Paragraph("&bull; **Web Scraping Tool:** Python scripts for automated data extraction and indexing from public web targets.", style_bullet))
    story.append(Paragraph("&bull; **Calorie & BMR Calculator:** Health application estimating metabolic indices using medical formulas.", style_bullet))
    story.append(Spacer(1, 10))
    
    # ------------------ EDUCATION ------------------
    story.append(Paragraph("EDUCATION", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    
    edu_header = [
        [Paragraph("Master's in Full Stack Software Development", style_entry_title), Paragraph("2024 - 2025", style_entry_date)],
        [Paragraph("ConquerBlocks Technology Bootcamp", style_entry_subtitle), Paragraph("", style_entry_date)]
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
    story.append(Paragraph("&bull; Intensive 600+ hours coding program focusing on software architecture, backend with Python & SQL, frontend with JavaScript, agile methodologies (Scrum), and production deployment.", style_bullet))
    story.append(Spacer(1, 10))
    
    # ------------------ LANGUAGES ------------------
    story.append(Paragraph("LANGUAGES", style_section))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_secondary, spaceAfter=6, spaceBefore=2))
    
    idiomas_data = [
        [Paragraph("&bull; <b>Spanish:</b> Native", style_body), Paragraph("&bull; <b>English:</b> Advanced (Full professional proficiency)", style_body), Paragraph("&bull; <b>Portuguese:</b> Advanced (Professional working proficiency)", style_body)]
    ]
    idiomas_table = Table(idiomas_data, colWidths=[120, 240, 160])
    idiomas_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(idiomas_table)

    doc.build(story)
    print("[OK] English CV PDF generated successfully.")

def generar_carta_presentacion_en(desktop_path):
    pdf_path = os.path.join(desktop_path, "Cover_Letter_Enmanuel_Jimenez.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Colors
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
    
    # Letter Header
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
    story.append(Paragraph("Software Developer / Junior Full Stack", style_header_title))
    story.append(HRFlowable(width="100%", thickness=1, color=c_primary, spaceAfter=20, spaceBefore=0))
    
    # Date and Recipient
    story.append(Paragraph("Quarteira, Faro, Portugal<br/>June 15, 2026", ParagraphStyle('Letter_Date', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=9, spaceAfter=15)))
    
    story.append(Paragraph("<b>To the attention of the Recruitment Team / Tech Hiring Manager</b>", style_salutation))
    
    # Letter Body
    p1 = (
        "I am writing to express my strong interest in the Software Developer (Backend / Junior Full Stack) "
        "position at your organization. Having completed the Full Stack Software Development Bootcamp at ConquerBlocks, "
        "being a resident of Portugal, and possessing advanced proficiency in English, Portuguese, and Spanish, "
        "I am prepared to join your engineering team immediately in a remote or hybrid role."
    )
    story.append(Paragraph(p1, style_body))
    
    p2 = (
        "Throughout my training and self-directed projects, I have consolidated my skills in building robust web "
        "applications using Python (Flask) and JavaScript. Among my key achievements is the development of a real-time "
        "delivery platform (Delivery App), where I implemented bi-directional communication using WebSockets (Flask-SocketIO), "
        "integrated Stripe API for payment processing, and automated user SMS alerts via Twilio. Additionally, I have strong "
        "experience managing relational databases (MySQL and SQLite) using SQLAlchemy ORM, structuring code under Clean "
        "Architecture and SOLID principles."
    )
    story.append(Paragraph(p2, style_body))
    
    p3 = (
        "Beyond my personal portfolio, I have experience working with real-world clients, such as designing and "
        "developing the commercial website 'Com Cheiro de Amor' in Portugal. This project allowed me to leverage Vanilla "
        "JavaScript, HTML5, and CSS3 to deliver a highly interactive, responsive catalog site tailored to drive user conversion."
    )
    story.append(Paragraph(p3, style_body))
    
    p4 = (
        "What sets me apart as a junior developer is my rigorous focus on code quality: I utilize Git and Gitflow "
        "workflows to maintain clean repositories, and I write unit tests to ensure stability across modules. My multilingual "
        "background enables me to integrate seamlessly into international, fast-paced teams."
    )
    story.append(Paragraph(p4, style_body))
    
    p5 = (
        "Thank you for your time and consideration of my application. I would welcome the opportunity to discuss "
        "how my technical skills and project experience can contribute to your team's goals."
    )
    story.append(Paragraph(p5, style_body))
    
    story.append(Spacer(1, 15))
    story.append(Paragraph("Sincerely,", style_body))
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Enmanuel Jimenez</b>", style_salutation))
    story.append(Paragraph("Software Developer / Full Stack", ParagraphStyle('Letter_Footer', parent=styles['Normal'], fontName='Helvetica', fontSize=9, textColor=colors.HexColor("#4A5568"))))

    doc.build(story)
    print("[OK] English Cover Letter PDF generated successfully.")

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
    
    print(f"Generating English PDFs in: {desktop}")
    
    try:
        generar_curriculum_en(desktop)
        generar_carta_presentacion_en(desktop)
        print("[SUCCESS] English PDFs generated successfully.")
    except Exception as e:
        print(f"[ERROR] Error during English PDF generation: {e}", file=sys.stderr)
        sys.exit(1)
