from typing import List, Dict, Tuple, Any
from core.models import CVContentProvider

class SpanishCVContent(CVContentProvider):
    """
    Proveedor de contenido en Español para el CV y Carta de Presentación de Enmanuel Jiménez (SRP).
    """

    def get_personal_info(self) -> Dict[str, str]:
        return {
            "name": "ENMANUEL JIMÉNEZ",
            "title": "DESARROLLADOR SOFTWARE | OPERADOR DE REPARTO Y ALMACÉN",
            "phone": "+351 911 151 993",
            "email": "enmanuelejaj@gmail.com",
            "address": "Rua 1 de Maio, Número 4, Quarteira, Portugal",
            "github": "github.com/ejaj94",
            "linkedin": "linkedin.com/in/enmanuel-jimenez-dev"
        }

    def get_profile_title(self) -> str:
        return "PERFIL PROFESIONAL"

    def get_profile_text(self) -> str:
        return (
            "Profesional multidisciplinario con un perfil versátil que combina 2 años de experiencia como repartidor y "
            "entregador de encomiendas de última milla en Portugal (trabajando con empresas líderes del sector como DPD, "
            "GLS, Eco Scooting y Correos Express) con sólida experiencia en operaciones de almacén y logística. En paralelo, "
            "poseo una fuerte preparación técnica en computación e informática, desempeñándome como Desarrollador de Software Web "
            "(Full Stack / Backend) con dominio absoluto en la administración de múltiples sistemas operativos (Windows, Linux, "
            "macOS), redes, bases de datos relacionales y automatización. Experto en optimizar operaciones mediante la digitalización "
            "y el desarrollo de soluciones de software a medida."
        )

    def get_experience_section_title(self) -> str:
        return "EXPERIENCIA LABORAL"

    def get_experience(self) -> List[Dict[str, Any]]:
        return [
            {
                "title": "Operador de Logística y Reparto (Última Milla)",
                "subtitle": "Entregador para DPD, GLS, Eco Scooting y Correos Express | Algarve, Portugal",
                "date": "2024 - Presente",
                "bullets": [
                    "Gestión, clasificación previa y entrega segura de paquetes y encomiendas procedentes de comercio electrónico (e-commerce).",
                    "Reparto y distribución en la ruta geográfica del Algarve: Quarteira, Albufeira, Guia, Faro, Vilamoura y Almancil.",
                    "Planificación y optimización diaria de rutas mediante GPS y software de navegación para garantizar entregas puntuales y reducción de consumo en zonas residenciales y comerciales clave.",
                    "Control digital de albaranes, reportes de incidencias y manejo de aplicaciones de seguimiento de envíos (PDA).",
                    "Atención directa y resolución ágil de dudas con el cliente final para asegurar la excelencia en el servicio."
                ]
            },
            {
                "title": "Operador de Almacén y Logística",
                "subtitle": "Gestión de Stock y Operaciones | Quarteira, Faro, Portugal",
                "date": "2023 - 2024",
                "bullets": [
                    "Recepción, verificación física y documental de mercancía entrante y control de daños.",
                    "Preparación de pedidos (picking y packing) mediante terminales de radiofrecuencia y lectores de código de barras.",
                    "Actualización e ingreso de stock en los sistemas informáticos de gestión de almacén (WMS).",
                    "Clasificación interna, carga/descarga de camiones y mantenimiento del orden del almacén bajo normativas de higiene y seguridad laboral."
                ]
            },
            {
                "title": "Desarrollador de Software Web (Freelance y Portafolio)",
                "subtitle": "Desarrollo Full Stack y Automatización | Quarteira, Portugal",
                "date": "2025 - 2026",
                "bullets": [
                    "<b>Com Cheiro de Amor (Sitio Web Comercial):</b> Diseñé y desarrollé un catálogo web responsivo y dinámico para una marca local de productos artesanales utilizando JavaScript nativo (Vanilla JS), HTML5 y CSS3 avanzados para carga ultrarrápida.",
                    "<b>Delivery App (Plataforma de Entregas):</b> Aplicación Full Stack robusta programada en Python (Flask) y SQLite. Integra pagos con Stripe, alertas por SMS con Twilio, geolocalización en tiempo real vía WebSockets (Flask-SocketIO) y soporte multi-idioma.",
                    "<b>Gestor Pro DB:</b> Sistema backend para la administración y auditoría de bases de datos relacionales MySQL estructurado con SQLAlchemy ORM, principios SOLID y Clean Architecture por capas. Genera reportes PDF automatizados (ReportLab) enviados por email (SMTP)."
                ]
            },
            {
                "title": "Otros Proyectos de Portafolio Técnico",
                "subtitle": "Automatización y Desarrollo de Utilidades | Portafolio Personal",
                "date": "2025",
                "bullets": [
                    "<b>Monitor de Precios de Cripto y Divisas:</b> Aplicación en Python que consome APIs financieras para graficar tendencias en tiempo real.",
                    "<b>Network Security Scanner:</b> Script en Python para diagnóstico y escaneo básico de vulnerabilidades y puertos en redes locales.",
                    "<b>Organizador de Archivos Inteligente:</b> Script de automatización en Python para clasificación y ordenación autónoma de directorios en el SO."
                ]
            }
        ]

    def get_skills_section_title(self) -> str:
        return "HABILIDADES TÉCNICAS E INFORMÁTICA"

    def get_skills(self) -> List[Tuple[str, str]]:
        return [
            ("Sistemas Operativos", "Linux/Ubuntu (línea de comandos Bash, administración de servidores), Windows (PowerShell scripting y automatización del sistema), macOS."),
            ("Lenguajes y Web", "Python, JavaScript (ES6+), SQL, HTML5, CSS3, JSON."),
            ("Bases de Datos", "MySQL, SQLite, modelado relacional y acceso a datos avanzado mediante SQLAlchemy ORM."),
            ("Herramientas e Integración", "Git, GitHub, Gitflow, Stripe API, Twilio API, WebSockets (Flask-SocketIO), ReportLab, envío SMTP.")
        ]

    def get_education_section_title(self) -> str:
        return "FORMACIÓN ACADÉMICA"

    def get_education(self) -> List[Dict[str, Any]]:
        return [
            {
                "title": "Máster en Desarrollo de Software Full Stack",
                "subtitle": "Bootcamp Tecnológico ConquerBlocks",
                "date": "2024 - 2025",
                "bullets": [
                    "Programa intensivo de más de 600 horas de código enfocado en arquitectura de software, backend con Python y SQL, desarrollo frontend con JavaScript, metodologías ágiles (Scrum) y despliegue en producción."
                ]
            }
        ]

    def get_certificates_subtitle(self) -> str:
        return "Certificados de Especialización Obtenidos (ConquerBlocks)"

    def get_certificates(self) -> List[str]:
        return [
            "Certificado en Linux y la Terminal (Administración y control por consola)",
            "Certificado en Git y GitHub (Control de versiones avanzado y flujos Gitflow)",
            "Certificado en Python Inicial (Lógica de programación y desarrollo de algoritmos)",
            "Certificado en Python Avanzado (Estructuras complejas y Programación Orientada a Objetos)",
            "Certificado en SQL (Diseño, normalización y consultas complejas de bases de datos)",
            "Certificado en Uso de ORMs en Python (SQLAlchemy y persistencia de datos)",
            "Certificado en Principios SOLID y Acceso a Bases de Datos (Arquitectura limpia)",
            "Certificado en Pseudocódigo (Lógica y diseño algorítmico previo)"
        ]

    def get_languages_section_title(self) -> str:
        return "IDIOMAS"

    def get_languages(self) -> List[Tuple[str, str]]:
        return [
            ("Español", "Nativo"),
            ("Inglés", "Avanzado (Competencia profesional completa)"),
            ("Portugués", "Avanzado (Fluidez conversacional y escrita)")
        ]

    def get_filename_suffix(self) -> str:
        return ""

    def has_cover_letter(self) -> bool:
        return True

    def get_cover_letter_filename(self) -> str:
        return "Carta_Presentacion_Enmanuel_Jimenez.pdf"

    def get_cover_letter_content(self) -> Dict[str, Any]:
        p1 = (
            "Les escribo con gran entusiasmo para presentar mi candidatura a la posición de Desarrollador Software "
            "(Backend / Full Stack Junior) en su organización. Como desarrollador graduado del Bootcamp Full Stack de "
            "ConquerBlocks, residente en Portugal y con dominio avanzado de inglés, portugués y español, estoy preparado "
            "para incorporarme de inmediato a su equipo tecnológico de forma remota o híbrida."
        )
        p2 = (
            "A lo largo de mi formación y desarrollo autónomo, he consolidado habilidades en la creación de aplicaciones "
            "web robustas utilizando Python (Flask) y JavaScript. Entre mis logros más destacados se encuentra el desarrollo "
            "completo de una plataforma de entregas en tiempo real (Delivery App), donde implementé comunicación bidireccional "
            "mediante WebSockets (Flask-SocketIO), integré pasarelas de pago seguras con la API de Stripe y automaticé avisos "
            "por SMS con Twilio. Asimismo, poseo un fuerte dominio de bases de datos relacionales (MySQL y SQLite) gestionadas "
            "a través de SQLAlchemy ORM, estructuradas bajo arquitecturas limpias (patrón Repository/Service) y principios SOLID."
        )
        p3 = (
            "Además de mis proyectos personales, cuento con experiencia trabajando para clientes reales, como el diseño y "
            "desarrollo del sitio web comercial 'Com Cheiro de Amor' en Portugal. Este proyecto me permitió dominar JavaScript "
            "nativo, HTML5 y CSS3 para construir una interfaz altamente responsiva e interactiva enfocada en la conversión del usuario."
        )
        p4 = (
            "Lo que me distingue como desarrollador junior es mi rigurosidad con la calidad del código: utilizo Git y flujos "
            "de trabajo Gitflow para mantener repositorios limpios y seguros, y diseño pruebas unitarias para garantizar el "
            "correcto funcionamiento de cada módulo. Mi capacidad multilingüe me permite además encajar perfectamente en equipos "
            "internacionales y dinámicos."
        )
        p5 = (
            "Agradezco de antemano el tiempo dedicado a evaluar mi currículum adjunto. Estaría encantado de mantener una "
            "entrevista para profundizar en cómo mi perfil y proyectos pueden contribuir al éxito de sus próximos desarrollos."
        )
        return {
            "date_location": "Quarteira, Faro, Portugal\n03 de julio de 2026",
            "salutation": "A la atención del Equipo de Selección / Responsable de Tecnología",
            "paragraphs": [p1, p2, p3, p4, p5],
            "farewell": "Atentamente,",
            "signature": "Enmanuel Jiménez",
            "signature_title": "Desarrollador Software / Full Stack"
        }
