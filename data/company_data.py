"""
This module provides data for the company website.
In a real application, this would likely come from a database.
"""

def get_company_info():
    """Return company information for the website"""
    return {
        'name': 'AllWorks Company',
        'short_name': 'AWC',
        'slogan': 'Delivering Excellence in Projects, Courses, and Training',
        'founded': 2010,
        'mission': 'To provide innovative solutions and exceptional learning experiences that empower organizations and individuals to achieve their full potential.',
        'vision': 'To be the leading provider of professional services, education, and training solutions globally, recognized for excellence and innovation.',
        'core_values': [
            'Excellence in all we do',
            'Innovation and creativity',
            'Integrity and ethical practice',
            'Client-centered approach',
            'Continuous improvement'
        ],
        'headquarters': 'New York, NY',
        'team_size': '120+ professionals',
        'certifications': [
            'ISO 9001:2015',
            'PMI Registered Education Provider',
            'CMMI Level 5',
            'Microsoft Gold Partner'
        ]
    }

def get_projects():
    """Return list of company projects"""
    return [
        {
            'id': 1,
            'title': 'Enterprise Digital Transformation',
            'category': 'Digital Transformation',
            'client': 'Fortune 500 Financial Institution',
            'description': 'Led a comprehensive digital transformation initiative for a major financial institution, modernizing legacy systems and implementing cloud-based solutions that reduced operational costs by 35% and improved customer satisfaction scores by 28%.',
            'image': 'https://pixabay.com/get/g2fae69b487b537beacd352d99f47ea2bac6388679f41ba26d2702224bca374b8a579d4e82d65dd22cdaaa76b988d11fd191333280defcf60098bc43468c237de_1280.jpg',
            'highlights': [
                'Legacy system modernization',
                'Cloud migration',
                'Process automation',
                'Customer experience enhancement'
            ],
            'duration': '18 months',
            'year': 2022
        },
        {
            'id': 2,
            'title': 'Smart City Infrastructure Development',
            'category': 'Infrastructure',
            'client': 'Metropolitan Government',
            'description': 'Designed and implemented smart city solutions for urban mobility, environmental monitoring, and public safety, resulting in a 22% reduction in traffic congestion and 15% decrease in energy consumption across municipal facilities.',
            'image': 'https://pixabay.com/get/g340529e1ad28285d67f4c2866458b14cd72a018bf523f2ba1c11e04a639b17e30e831357a473e0a6ef398136bfd9519a02a1381ed8ce8bbe7957f555af05f476_1280.jpg',
            'highlights': [
                'IoT sensor network',
                'Integrated traffic management',
                'Energy efficiency solutions',
                'Public safety enhancements'
            ],
            'duration': '24 months',
            'year': 2021
        },
        {
            'id': 3,
            'title': 'Healthcare Data Analytics Platform',
            'category': 'Healthcare',
            'client': 'Regional Hospital Network',
            'description': 'Developed a comprehensive data analytics platform for a network of hospitals, enabling predictive patient care insights, optimized resource allocation, and improved operational efficiency, resulting in an estimated $4.2M annual cost savings.',
            'image': 'https://pixabay.com/get/g3756b124d8e210cf46530dde0fff7c1b369b8b81c7ebb933ffe576081aceca315bcfd2180acfb652f9179bd92f47168e88441f3bb9ab2586486ed48d077c82cd_1280.jpg',
            'highlights': [
                'Predictive analytics',
                'Resource optimization',
                'Patient outcome improvement',
                'HIPAA-compliant data architecture'
            ],
            'duration': '12 months',
            'year': 2022
        },
        {
            'id': 4,
            'title': 'Supply Chain Optimization',
            'category': 'Supply Chain',
            'client': 'Global Manufacturing Company',
            'description': 'Redesigned and optimized the end-to-end supply chain for a global manufacturer, implementing advanced forecasting algorithms and real-time inventory management systems that reduced lead times by 40% and inventory costs by 25%.',
            'image': 'https://pixabay.com/get/gbf53b23c587d7726850730bdd93cc867ab4caec65b6a3a5935959e3b319eaaf7dc45055aaa1cf28ddf83de9b1748917d349cee616f51ff72cdd8d40bb80e4d29_1280.jpg',
            'highlights': [
                'Demand forecasting',
                'Inventory optimization',
                'Logistics network redesign',
                'Supplier integration'
            ],
            'duration': '15 months',
            'year': 2021
        },
        {
            'id': 5,
            'title': 'Cybersecurity Enhancement Program',
            'category': 'Cybersecurity',
            'client': 'International Banking Group',
            'description': 'Implemented a comprehensive cybersecurity enhancement program for a banking group, including advanced threat detection, employee training, and secure architecture design, strengthening protection of customer data and financial assets.',
            'image': 'https://pixabay.com/get/gc088ffb5a48e7b51b39e00409635b0a4e89a9da5b725bb63c410ba3c713ba0b35194a940aa0b75e75d86846793a95e7f091e1551e4b9ab652302ca5819bd34b7_1280.jpg',
            'highlights': [
                'Advanced threat protection',
                'Security awareness training',
                'Zero-trust architecture',
                'Compliance framework implementation'
            ],
            'duration': '9 months',
            'year': 2023
        },
        {
            'id': 6,
            'title': 'Sustainable Manufacturing Initiative',
            'category': 'Sustainability',
            'client': 'Consumer Goods Manufacturer',
            'description': 'Led a sustainable manufacturing transformation, implementing energy-efficient processes, waste reduction systems, and circular economy principles that reduced carbon emissions by 30% and achieved zero-waste-to-landfill status for three production facilities.',
            'image': 'https://pixabay.com/get/ga1738581e70fda2a35bd7e0d76ffdba9fb3ed3d40ef6a9462cad9f6fd198eb86ce2bb0deae81fa75f3d1db3d1b6d3857d43769d7fa979c65d1410aacb008b7aa_1280.jpg',
            'highlights': [
                'Energy efficiency optimization',
                'Waste reduction systems',
                'Circular economy implementation',
                'Carbon footprint reduction'
            ],
            'duration': '18 months',
            'year': 2022
        }
    ]

def get_courses():
    """Return list of company courses"""
    return [
        {
            'id': 1,
            'title': 'Advanced Project Management',
            'category': 'Project Management',
            'level': 'Advanced',
            'description': 'A comprehensive course designed for experienced project managers looking to enhance their skills in managing complex, high-stakes projects across diverse industries. Participants will master advanced risk management techniques, stakeholder engagement strategies, and agile-waterfall hybrid methodologies.',
            'image': 'https://pixabay.com/get/ge41b4332fbeabbe9f9cc752d2d1527c901271793a85b249689183c0fd1977ce1c7c937c26a42ae8cd5c00b7c6426d8b6ddf7dcffa98df032611249f03d02cefa_1280.jpg',
            'duration': '12 weeks',
            'format': 'Online with live sessions',
            'certification': 'Yes - PMI PDUs available',
            'modules': [
                'Strategic Project Leadership',
                'Advanced Risk Management',
                'Complex Stakeholder Engagement',
                'Agile-Waterfall Hybrid Methodologies',
                'Project Recovery Strategies',
                'Portfolio Optimization Techniques'
            ],
            'price': '$1,995'
        },
        {
            'id': 2,
            'title': 'Data Science and Analytics Fundamentals',
            'category': 'Data Science',
            'level': 'Beginner to Intermediate',
            'description': 'An introduction to the world of data science and analytics, focusing on practical skills and real-world applications. Participants will learn the entire data science workflow from data collection and cleaning to analysis and visualization, with hands-on projects using industry-standard tools.',
            'image': 'https://pixabay.com/get/g2813771833417bbab9e0ee759ee133738f5ca853b18f3541ba521007e7582791c3a4a09119ab3f2b4b436652a3ef2e3c86406f135542ca44db03dbec9348b4cb_1280.jpg',
            'duration': '10 weeks',
            'format': 'Hybrid (online and in-person options)',
            'certification': 'Yes',
            'modules': [
                'Introduction to Data Science',
                'Statistical Analysis Fundamentals',
                'Data Collection and Cleaning',
                'Exploratory Data Analysis',
                'Data Visualization Best Practices',
                'Introduction to Machine Learning',
                'Communicating Data Insights'
            ],
            'price': '$1,495'
        },
        {
            'id': 3,
            'title': 'Leadership Excellence Program',
            'category': 'Leadership',
            'level': 'Intermediate to Advanced',
            'description': 'A transformative leadership development program designed for mid to senior-level managers. This course combines cutting-edge leadership theory with practical application, enabling participants to enhance their leadership effectiveness and drive organizational performance.',
            'image': 'https://pixabay.com/get/gfe112c1622958c53c49fc6130c045dbd7fd5e2e28c0e675a6267974876e71d61b6feb03afb8e841e9d8e63d5755745b2b25afb5fb11e86cf208a04c6e0c26e63_1280.jpg',
            'duration': '8 weeks',
            'format': 'In-person intensive with executive coaching',
            'certification': 'Yes',
            'modules': [
                'Strategic Leadership Vision',
                'Emotional Intelligence for Leaders',
                'Building High-Performance Teams',
                'Change Management Excellence',
                'Inclusive Leadership Practices',
                'Conflict Resolution and Negotiation',
                'Leadership Communication'
            ],
            'price': '$2,495'
        },
        {
            'id': 4,
            'title': 'Digital Marketing Mastery',
            'category': 'Marketing',
            'level': 'All Levels',
            'description': 'A comprehensive digital marketing course covering the latest strategies, tools, and platforms. Participants will develop practical skills in SEO, content marketing, social media, email campaigns, and analytics, learning to create integrated marketing strategies that drive measurable results.',
            'image': 'https://pixabay.com/get/g921dddd95c9163712cc896a43b0ade029d8711efa856401f27121dec89a221a0e49688bb19fd39c31b7d94176dd27f0911cd046a90c7b2cfc5a802615720c4f4_1280.jpg',
            'duration': '8 weeks',
            'format': 'Online with interactive workshops',
            'certification': 'Yes',
            'modules': [
                'Digital Marketing Strategy Development',
                'Search Engine Optimization (SEO)',
                'Content Marketing Excellence',
                'Social Media Marketing',
                'Email Marketing Campaigns',
                'Pay-Per-Click Advertising',
                'Analytics and Performance Measurement'
            ],
            'price': '$1,295'
        }
    ]

def get_training_programs():
    """Return list of company training programs"""
    return [
        {
            'id': 1,
            'title': 'Corporate Leadership Accelerator',
            'target_audience': 'Emerging and mid-level leaders',
            'description': 'A comprehensive leadership development program designed to accelerate the growth of high-potential talent within organizations. This immersive program combines interactive workshops, personalized coaching, practical applications, and peer learning to develop well-rounded leaders ready to navigate complex business challenges.',
            'image': 'https://pixabay.com/get/ge98175a17db8e08fb59b9cac70f9eda5f708bdcfdd3c1a37946e5884ff2bcf4b2cac5fb11b6788167d802cd236b7ce21530b10c75046fae4c92ff22281e903fd_1280.jpg',
            'duration': '6 months',
            'delivery_method': 'Blended (in-person and virtual)',
            'key_outcomes': [
                'Enhanced strategic thinking and decision-making capabilities',
                'Strengthened emotional intelligence and team leadership skills',
                'Improved change management and organizational transformation abilities',
                'Developed resilience and adaptability in complex environments',
                'Refined communication and influence across diverse stakeholders'
            ],
            'customizable': True
        },
        {
            'id': 2,
            'title': 'Agile Transformation Workshop',
            'target_audience': 'Cross-functional teams and management',
            'description': 'An intensive training program designed to help organizations transition to agile methodologies and mindsets. Participants will learn how to implement agile frameworks, overcome common challenges, and create a sustainable agile culture that drives innovation and adaptability throughout the organization.',
            'image': 'https://pixabay.com/get/g41ad65aa4067a75c98967c94e34345623179c3d1577846a3f8ced765849a1acec499d2d3b99bee526e45b5b81882476f3b4ae689d00f48bd28fc55fa8cd37294_1280.jpg',
            'duration': '2-4 weeks',
            'delivery_method': 'On-site immersive training',
            'key_outcomes': [
                'Practical understanding of agile methodologies (Scrum, Kanban, SAFe)',
                'Ability to implement agile practices appropriate to organizational context',
                'Skills to facilitate effective agile ceremonies and collaborative processes',
                'Strategies to overcome common agile transformation challenges',
                'Frameworks for measuring agile success and continuous improvement'
            ],
            'customizable': True
        },
        {
            'id': 3,
            'title': 'Cybersecurity Essentials for Business',
            'target_audience': 'All employees, with specialized tracks for IT and leadership',
            'description': 'A comprehensive cybersecurity awareness and skills program designed to strengthen an organization\'s human firewall. This program builds a security-conscious culture while providing practical skills to identify, prevent, and respond to common cybersecurity threats facing businesses today.',
            'image': 'https://pixabay.com/get/g50cb62f085b9b4ac5de3fb18edc0586978747e4d11ef2f2037749aaa995cd718f9ea9e09e5a1acbcbcad88ef772d6e1aa0f6dcded286873e707d716ae51278dd_1280.jpg',
            'duration': '4 weeks',
            'delivery_method': 'Virtual interactive sessions',
            'key_outcomes': [
                'Enhanced ability to recognize and avoid phishing and social engineering attacks',
                'Understanding of secure data handling practices and compliance requirements',
                'Practical password security and multi-factor authentication implementation',
                'Knowledge of incident reporting procedures and response protocols',
                'Leadership track: Strategic cybersecurity governance and risk management'
            ],
            'customizable': True
        }
    ]

def get_publications():
    """Return list of company publications"""
    return [
        {
            'id': 1,
            'title': 'The Future of Work: Navigating Digital Transformation',
            'type': 'White Paper',
            'author': 'Dr. Sarah Chen, Chief Innovation Officer',
            'description': 'An in-depth analysis of how digital transformation is reshaping workplace dynamics, organizational structures, and career pathways. This white paper provides strategic insights and practical frameworks to help organizations thrive in the rapidly evolving digital landscape.',
            'topics': [
                'AI and automation impact on workforce',
                'Remote and hybrid work best practices',
                'Digital skills development strategies',
                'Organizational change management',
                'Future-ready leadership approaches'
            ],
            'publication_date': 'March 2023',
            'pages': 42,
            'download_format': 'PDF'
        },
        {
            'id': 2,
            'title': 'Project Management Excellence: Lessons from Global Leaders',
            'type': 'Research Report',
            'author': 'James Wilson, Director of Project Management',
            'description': 'A comprehensive study of project management practices across 150+ organizations in 25 countries, identifying key differentiators between high-performing and average project teams. The report offers evidence-based recommendations for enhancing project success rates and organizational project management maturity.',
            'topics': [
                'Critical success factors in complex projects',
                'Agile-traditional hybrid methodologies',
                'Project leadership competency frameworks',
                'Cross-cultural project management',
                'Technology enablement in project delivery'
            ],
            'publication_date': 'November 2022',
            'pages': 78,
            'download_format': 'PDF and Interactive Dashboard'
        },
        {
            'id': 3,
            'title': 'Sustainable Business Transformation Playbook',
            'type': 'Guide',
            'author': 'Elena Rodriguez, Head of Sustainability Practice',
            'description': 'A practical guide to implementing sustainable business practices that drive both environmental impact and business value. This playbook offers step-by-step frameworks, case studies, and implementation tools for organizations at any stage of their sustainability journey.',
            'topics': [
                'ESG strategy development',
                'Carbon footprint reduction roadmaps',
                'Circular economy business models',
                'Sustainable supply chain management',
                'Stakeholder engagement and reporting'
            ],
            'publication_date': 'June 2023',
            'pages': 65,
            'download_format': 'PDF and Editable Templates'
        },
        {
            'id': 4,
            'title': 'Cybersecurity in the Age of Interconnected Systems',
            'type': 'Technical Report',
            'author': 'Michael Chang, Chief Security Officer',
            'description': 'An extensive technical analysis of emerging cybersecurity threats and defensive strategies in increasingly interconnected business environments. The report provides both technical specifications and management frameworks for building robust security architectures.',
            'topics': [
                'Zero-trust security architecture',
                'IoT and operational technology security',
                'Cloud security governance',
                'AI-powered threat detection',
                'Security skills development'
            ],
            'publication_date': 'August 2022',
            'pages': 56,
            'download_format': 'PDF'
        }
    ]
