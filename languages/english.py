from typing import List, Dict, Tuple, Any
from core.models import CVContentProvider

class EnglishCVContent(CVContentProvider):
    """
    Proveedor de contenido en Inglés para el CV (Resume) y Cover Letter de Enmanuel Jiménez (SRP).
    """

    def get_personal_info(self) -> Dict[str, str]:
        return {
            "name": "ENMANUEL JIMENEZ",
            "title": "SOFTWARE DEVELOPER | LOGISTICS & WAREHOUSE OPERATOR",
            "phone": "+351 911 151 993",
            "email": "enmanuelejaj@gmail.com",
            "address": "Rua 1 de Maio, Número 4, Quarteira, Portugal",
            "github": "github.com/ejaj94",
            "linkedin": "linkedin.com/in/enmanuel-jimenez-dev"
        }

    def get_profile_title(self) -> str:
        return "PROFESSIONAL SUMMARY"

    def get_profile_text(self) -> str:
        return (
            "Multidisciplinary professional with a highly versatile profile, combining 2 years of experience as a last-mile "
            "delivery driver in Portugal (working with industry leaders like DPD, GLS, Eco Scooting, and Correos Express) "
            "with a solid background in logistics and warehouse operations. In parallel, I possess strong technical training in "
            "computer science and software engineering, working as a Web Software Developer (Full Stack / Backend) with expert "
            "knowledge in administering multiple operating systems (Windows, Linux, macOS), local networking, relational databases, "
            "and system automation. Skilled at optimizing operational logistics workflows through digital conversion and custom "
            "software development."
        )

    def get_experience_section_title(self) -> str:
        return "WORK EXPERIENCE & KEY PROJECTS"

    def get_experience(self) -> List[Dict[str, Any]]:
        return [
            {
                "title": "Last Mile Logistics & Delivery Operator (Courier)",
                "subtitle": "Courier for DPD, GLS, Eco Scooting, and Correos Express | Algarve, Portugal",
                "date": "2024 - Present",
                "bullets": [
                    "Managed, sorted, and securely delivered e-commerce packages and parcels to end customers.",
                    "Provided complete delivery coverage across key Algarve routes: Quarteira, Albufeira, Guia, Faro, Vilamoura, and Almancil.",
                    "Planned and optimized daily routes using GPS and navigation software to ensure on-time deliveries and minimize fuel consumption in key residential and commercial zones.",
                    "Handled digital waybills, registered delivery incidents, and managed mobile tracking systems (PDA).",
                    "Resolved customer inquiries directly at the point of delivery, maintaining high satisfaction KPIs."
                ]
            },
            {
                "title": "Warehouse & Logistics Operator",
                "subtitle": "Inventory and Stock Management | Quarteira, Faro, Portugal",
                "date": "2023 - 2024",
                "bullets": [
                    "Received, unloaded, physical/documental inspected, and verified incoming goods and shipments, managing quality control.",
                    "Prepared customer orders (picking and packing) utilizing RF terminals and barcode scanners.",
                    "Updated stock registries and managed inventory within Warehouse Management Systems (WMS).",
                    "Organized warehouse space, loaded/unloaded trucks, and strictly adhered to safety and hygiene protocols."
                ]
            },
            {
                "title": "Web Software Developer (Freelance & Portfolio Projects)",
                "subtitle": "Full Stack Development & Automation | Quarteira, Portugal",
                "date": "2025 - 2026",
                "bullets": [
                    "<b>Com Cheiro de Amor (Commercial Website):</b> Designed and built a dynamic, fully responsive catalog website for a local handmade soap and candle brand using Vanilla JavaScript, HTML5, and advanced CSS3 without frameworks to ensure optimal load speeds.",
                    "<b>Delivery App (Real-Time Platform):</b> Built a robust Full Stack web application using Python (Flask) and SQLite. Programmed live courier tracking with WebSockets (Flask-SocketIO), integrated Stripe API for payments, and automated SMS alerts via Twilio API.",
                    "<b>Gestor Pro DB:</b> Console-based user management backend connected to a MySQL database, applying SOLID principles and layered Clean Architecture. Automated audit report generation in PDF format (ReportLab) and SMTP email delivery."
                ]
            },
            {
                "title": "Other Technical Portfolio Projects",
                "subtitle": "System Automation and Utilities | Personal Portfolio",
                "date": "2025",
                "bullets": [
                    "<b>Crypto & Currency Price Monitor:</b> Python application consuming financial APIs to analyze and chart market trends in real time.",
                    "<b>Network Security Scanner:</b> Python diagnostics tool that performs vulnerability and port scanning on local networks.",
                    "<b>Smart File Organizer:</b> OS automation script written in Python for autonomous classification and directory tidying."
                ]
            }
        ]

    def get_skills_section_title(self) -> str:
        return "TECHNICAL & COMPUTER SKILLS"

    def get_skills(self) -> List[Tuple[str, str]]:
        return [
            ("Operating Systems", "Linux/Ubuntu (proficient in terminal command-line Bash, server deployment), Windows (PowerShell scripting and OS automation), macOS."),
            ("Languages & Web", "Python, JavaScript (ES6+), SQL, HTML5, CSS3, JSON."),
            ("Databases", "MySQL, SQLite, relational modeling, and advanced data persistence using SQLAlchemy ORM."),
            ("Tools & Integration", "Git, GitHub, Gitflow, Stripe API, Twilio API, WebSockets (Flask-SocketIO), ReportLab PDF rendering, SMTP protocols.")
        ]

    def get_education_section_title(self) -> str:
        return "EDUCATION"

    def get_education(self) -> List[Dict[str, Any]]:
        return [
            {
                "title": "Master's in Full Stack Software Development",
                "subtitle": "ConquerBlocks Technology Bootcamp",
                "date": "2024 - 2025",
                "bullets": [
                    "Intensive 600+ hours coding program focusing on software architecture, backend with Python & SQL, frontend with JavaScript, agile methodologies (Scrum), and production deployment."
                ]
            }
        ]

    def get_certificates_subtitle(self) -> str:
        return "Specialized Certificates Obtained (ConquerBlocks)"

    def get_certificates(self) -> List[str]:
        return [
            "Certificate in Linux and the Terminal (Command-line administration and systems control)",
            "Certificate in Git and GitHub (Advanced version control and Gitflow workflows)",
            "Certificate in Python Inicial (Foundations of programming and algorithm development)",
            "Certificate in Python Avanzado (Complex data structures and Object-Oriented Programming)",
            "Certificate in SQL (Database design, normalization, and complex relational queries)",
            "Certificate in Uso de ORMs en Python (SQLAlchemy and data persistence layers)",
            "Certificate in Principios SOLID y Acceso a Bases de Datos (Clean Architecture)",
            "Certificate in Pseudocódigo (Algorithmic logic and pre-coding software design)"
        ]

    def get_languages_section_title(self) -> str:
        return "LANGUAGES"

    def get_languages(self) -> List[Tuple[str, str]]:
        return [
            ("Spanish", "Native"),
            ("English", "Advanced (Full professional proficiency)"),
            ("Portuguese", "Advanced (Professional working proficiency)")
        ]

    def get_filename_suffix(self) -> str:
        return "_EN"

    def has_cover_letter(self) -> bool:
        return True

    def get_cover_letter_filename(self) -> str:
        return "Cover_Letter_Enmanuel_Jimenez.pdf"

    def get_cover_letter_content(self) -> Dict[str, Any]:
        p1 = (
            "I am writing to express my strong interest in the Software Developer (Backend / Junior Full Stack) "
            "position at your organization. Having completed the Full Stack Software Development Bootcamp at ConquerBlocks, "
            "being a resident of Portugal, and possessing advanced proficiency in English, Portuguese, and Spanish, "
            "I am prepared to join your engineering team immediately in a remote or hybrid role."
        )
        p2 = (
            "Throughout my training and self-directed projects, I have consolidated my skills in building robust web "
            "applications using Python (Flask) and JavaScript. Among my key achievements is the development of a real-time "
            "delivery platform (Delivery App), where I implemented bi-directional communication using WebSockets (Flask-SocketIO), "
            "integrated Stripe API for payment processing, and automated user SMS alerts via Twilio. Additionally, I have strong "
            "experience managing relational databases (MySQL and SQLite) using SQLAlchemy ORM, structuring code under Clean "
            "Architecture and SOLID principles."
        )
        p3 = (
            "Beyond my personal portfolio, I have experience working with real-world clients, such as designing and "
            "developing the commercial website 'Com Cheiro de Amor' in Portugal. This project allowed me to leverage Vanilla "
            "JavaScript, HTML5, and CSS3 to deliver a highly interactive, responsive catalog site tailored to drive user conversion."
        )
        p4 = (
            "What sets me apart as a junior developer is my rigorous focus on code quality: I utilize Git and Gitflow "
            "workflows to maintain clean repositories, and I write unit tests to ensure stability across modules. My multilingual "
            "background enables me to integrate seamlessly into international, fast-paced teams."
        )
        p5 = (
            "Thank you for your time and consideration of my application. I would welcome the opportunity to discuss "
            "how my technical skills and project experience can contribute to your team's goals."
        )
        return {
            "date_location": "Quarteira, Faro, Portugal\nJuly 3, 2026",
            "salutation": "To the attention of the Recruitment Team / Tech Hiring Manager",
            "paragraphs": [p1, p2, p3, p4, p5],
            "farewell": "Sincerely,",
            "signature": "Enmanuel Jimenez",
            "signature_title": "Software Developer / Full Stack"
        }
