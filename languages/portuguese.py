from typing import List, Dict, Tuple, Any
from core.models import CVContentProvider

class PortugueseCVContent(CVContentProvider):
    """
    Proveedor de contenido en Portugués de Portugal para el CV y Carta de Presentación de Enmanuel Jiménez (SRP).
    """

    def get_personal_info(self) -> Dict[str, str]:
        return {
            "name": "ENMANUEL JIMÉNEZ",
            "title": "SISTEMAS COMPUTACIONAIS | DISTRIBUIÇÃO E OPERADOR DE ARMAZÉM",
            "phone": "+351 911 151 993",
            "email": "enmanuelejaj@gmail.com",
            "address": "Rua 1 de Maio, Número 4, Quarteira, Portugal",
            "github": "github.com/ejaj94",
            "linkedin": "linkedin.com/in/enmanuel-jimenez-dev"
        }

    def get_profile_title(self) -> str:
        return "PERFIL PROFISSIONAL"

    def get_profile_text(self) -> str:
        return (
            "Profissional multidisciplinar com um perfil versátil que combina 2 anos de experiência como distribuidor e "
            "entregador de encomendas de última milha em Portugal (trabalhando com empresas líderes do setor como DPD, "
            "GLS, Eco Scooting e Correos Express) com uma sólida experiência em operações de armazém e logística. Em paralelo, "
            "possuo uma forte preparação técnica em computação e informática, atuando como Programador de Software Web "
            "(Full Stack / Backend) com domínio absoluto na administração de múltiplos sistemas operativos (Windows, Linux, "
            "macOS), redes, bases de dados relacionais e automatização de tarefas. Especialista em otimizar operações "
            "através da digitalização, gestão de fluxos de inventário e desenvolvimento de soluções de software à medida."
        )

    def get_experience_section_title(self) -> str:
        return "EXPERIÊNCIA PROFISSIONAL"

    def get_experience(self) -> List[Dict[str, Any]]:
        return [
            {
                "title": "Operador de Logística e Distribuição (Última Milha)",
                "subtitle": "Distribuidor / Entregador (DPD, GLS, Eco Scooting e Correos Express) | Algarve, Portugal",
                "date": "2024 - Presente",
                "bullets": [
                    "Responsável pela gestão, triagem prévia e entrega rápida e segura de mercadorias provenientes do comércio eletrónico (e-commerce).",
                    "Distribuição de encomendas com cobertura nas rotas do Algarve: Quarteira, Albufeira, Guia, Faro, Vilamoura e Almancil.",
                    "Planeamento inteligente e otimização de rotas diárias de entrega através de GPS e software de navegação para maximizar a produtividade e pontualidade.",
                    "Gestão digital de guias de transporte (alvarás), registo de incidentes e uso de sistemas eletrónicos de rastreamento (PDA).",
                    "Atendimento direto ao cliente, assegurando altos padrões de satisfação e resolução de dúvidas no ato de entrega."
                ]
            },
            {
                "title": "Operador de Armazém e Logística",
                "subtitle": "Gestão de Fluxos Logísticos | Quarteira, Faro, Portugal",
                "date": "2023 - 2024",
                "bullets": [
                    "Receção, descarga e conferência física e documental de mercadoria de entrada, assegurando o controlo de qualidade e a identificação de danos.",
                    "Preparação de encomendas (picking e packing) com o auxílio de leitores de código de barras e terminais de radiofrequência.",
                    "Introdução de dados e controlo contínuo de stock nos sistemas informáticos de gestão de armazém (WMS).",
                    "Organização física do armazém, carga/descarga de camiões e cumprimento rigoroso das normas de higiene e segurança no trabalho."
                ]
            },
            {
                "title": "Programador de Software Web (Freelance e Portfólio)",
                "subtitle": "Desenvolvimento Full Stack e Soluções Tecnológicas | Quarteira, Portugal",
                "date": "2025 - 2026",
                "bullets": [
                    "<b>Com Cheiro de Amor (Website Comercial):</b> Concebi e programei uma montra online interativa e totalmente responsiva para uma marca local de velas e sabonetes, aplicando JavaScript nativo (Vanilla JS), HTML5 e CSS3 sem frameworks, otimizando o SEO e o desempenho.",
                    "<b>Delivery App (Plataforma de Entregas):</b> Desenvolvi uma aplicação web completa com Python (Flask) e SQLite. Programei o rastreamento em tempo real dos entregadores com WebSockets (Flask-SocketIO), integrei a API do Stripe para pagamentos e a API do Twilio para alertas por SMS automático.",
                    "<b>Gestor Pro DB:</b> Criei uma ferramenta backend em consola ligada a uma base de dados relacional MySQL. Desenvolvi a lógica utilizando SQLAlchemy ORM, arquitetura limpa (Repository/Service) e princípios SOLID, incluindo relatórios PDF (ReportLab) enviados por email via protocolo SMTP (Gmail)."
                ]
            },
            {
                "title": "Outros Projetos de Portfólio Técnico",
                "subtitle": "Automação de Sistemas e Utilitários | Portfólio Pessoal",
                "date": "2025",
                "bullets": [
                    "<b>Monitor de Preços de Cripto e Divisas:</b> Aplicação em Python que consome APIs financeiras para exibir gráficos de tendências em tempo real.",
                    "<b>Network Security Scanner:</b> Script em Python para diagnóstico e varrimento básico de portas e vulnerabilidades em redes locais.",
                    "<b>Organizador de Ficheiros Inteligente:</b> Script de automação em Python para classificação autónoma de pastas e documentos no SO."
                ]
            }
        ]

    def get_skills_section_title(self) -> str:
        return "COMPETÊNCIAS INFORMÁTICAS E DE COMPUTAÇÃO"

    def get_skills(self) -> List[Tuple[str, str]]:
        return [
            ("Sistemas Operativos", "Linux/Ubuntu (uso profundo da consola Bash e comandos, gestão de servidores), Windows (PowerShell scripting e automatização de SO) e macOS."),
            ("Linguagens & Web", "Python, JavaScript (ES6+), SQL, HTML5, CSS3, JSON."),
            ("Bases de Dados", "MySQL, SQLite, gestão relacional e mapeamento avançado com SQLAlchemy ORM."),
            ("Ferramentas & APIs", "Git, GitHub, Gitflow, Stripe API, Twilio API, WebSockets (Flask-SocketIO), ReportLab PDF, envio SMTP.")
        ]

    def get_education_section_title(self) -> str:
        return "EDUCAÇÃO E CERTIFICADOS"

    def get_education(self) -> List[Dict[str, Any]]:
        return [
            {
                "title": "Mestrado em Desenvolvimento de Software Full Stack",
                "subtitle": "Bootcamp Tecnológico ConquerBlocks",
                "date": "2024 - 2025",
                "bullets": [
                    "Programa intensivo com mais de 600 horas de código abrangendo arquitetura de software, bases de dados relacionais, desenvolvimento web, metodologias ágeis (Scrum) e boas práticas (Clean Code)."
                ]
            }
        ]

    def get_certificates_subtitle(self) -> str:
        return "Certificados de Formação Profissional (ConquerBlocks)"

    def get_certificates(self) -> List[str]:
        return [
            "Certificado em Linux e a Terminal (Gestão por consola)",
            "Certificado em Git e GitHub (Controlo de versões avançado e Gitflow)",
            "Certificado em Python Inicial (Lógica e algoritmos)",
            "Certificado em Python Avanzado (Estruturas complexas e POO)",
            "Certificado em SQL (Modelação e consultas relacionais)",
            "Certificado em Uso de ORMs en Python (SQLAlchemy e persistência)",
            "Certificado em Princípios SOLID e Acesso a Bases de Dados (Clean Architecture)",
            "Certificado em Pseudocódigo (Lógica algorítmica)"
        ]

    def get_languages_section_title(self) -> str:
        return "IDIOMAS"

    def get_languages(self) -> List[Tuple[str, str]]:
        return [
            ("Espanhol", "Nativo"),
            ("Inglês", "Avançado (Fluência profissional)"),
            ("Português", "Avançado (Fluência conversacional e escrita)")
        ]

    def get_filename_suffix(self) -> str:
        return "_PT"

    def has_cover_letter(self) -> bool:
        return True

    def get_cover_letter_filename(self) -> str:
        return "Carta_Apresentacao_Enmanuel_Jimenez.pdf"

    def get_cover_letter_content(self) -> Dict[str, Any]:
        p1 = (
            "Escrevo-vos com grande entusiasmo para apresentar a minha candidatura à posição de Programador de Software "
            "(Backend / Full Stack Junior) na vossa organização. Como programador graduado do Bootcamp Full Stack da "
            "ConquerBlocks, residente em Portugal e com domínio avançado de inglês, português e espanhol, estou preparado "
            "para me integrar de imediato na vossa equipa tecnológica de forma remota ou híbrida."
        )
        p2 = (
            "Ao longo da minha formação e desenvolvimento autónomo, consolidei competências na criação de aplicações "
            "web robustas utilizando Python (Flask) e JavaScript. Entre as minhas conquistas mais destacadas encontra-se o "
            "desenvolvimento completo de uma plataforma de entregas em tempo real (Delivery App), onde implementei comunicação "
            "bidirecional através de WebSockets (Flask-SocketIO), integrei gateways de pagamento seguros com a API do Stripe e "
            "automatizei alertas por SMS com a Twilio. Além disso, possuo um forte domínio de bases de dados relacionais "
            "(MySQL e SQLite) geridas através de SQLAlchemy ORM, estruturadas sob arquiteturas limpas (padrão Repository/Service) "
            "e princípios SOLID."
        )
        p3 = (
            "Para além dos meus projetos pessoais, conto com experiência de trabalho com clientes reais, como a conceção e "
            "desenvolvimento do website comercial 'Com Cheiro de Amor' em Portugal. Este projeto permitiu-me dominar JavaScript "
            "nativo, HTML5 e CSS3 para construir uma interface altamente responsiva e interativa focada na conversão do utilizador."
        )
        p4 = (
            "O que me distingue como programador júnior é o meu rigor com a qualidade do código: utilizo Git e fluxos "
            "de trabalho Gitflow para manter repositórios limpos e seguros, e desenho testes unitários para garantir o "
            "correto funcionamento de cada módulo. A minha capacidade multilingue permite-me ainda integrar-me perfeitamente em "
            "equipas internacionais e dinâmicas."
        )
        p5 = (
            "Agradeço desde já o tempo dedicado a avaliar o meu currículo em anexo. Estaria encantado em manter uma "
            "entrevista para aprofundar como o meu perfil e projetos podem contribuir para o sucesso dos vossos próximos desenvolvimentos."
        )
        return {
            "date_location": "Quarteira, Faro, Portugal\n03 de julho de 2026",
            "salutation": "À atenção da Equipa de Seleção / Responsável de Tecnologia",
            "paragraphs": [p1, p2, p3, p4, p5],
            "farewell": "Atentamente,",
            "signature": "Enmanuel Jiménez",
            "signature_title": "Programador de Software / Full Stack"
        }
