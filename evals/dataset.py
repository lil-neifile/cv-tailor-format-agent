from langsmith import Client
from dotenv import load_dotenv
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

api_key = os.getenv("LANGSMITH_API_KEY")
if not api_key:
    raise RuntimeError(f"LANGSMITH_API_KEY not found in {ROOT / '.env'}")

client = Client(api_key=api_key)


DATASET_NAME = "tailored_cv_dataset"

if client.has_dataset(dataset_name=DATASET_NAME):
    dataset = client.read_dataset(dataset_name=DATASET_NAME)
else:
    dataset = client.create_dataset(dataset_name=DATASET_NAME)

base_cv = """Liliia Shrainer
Valencia, Spain
linkedin.com/in/liliia-shrainer
Summary
Residence and Work Permit (Autorizacion de Residencia y Trabajo). AI Engineer with 2 years of experience in Python, AI, and LLM Engineering. Proven track record in multimodal LLM pipelines, AI API integration, and system stability improvement. Skilled in Python, FastAPI, LangChain, and LangGraph with expertise in building comprehensive test suites and automated LLM extraction pipelines. Successfully saved clients approximately $1,000,000 USD through custom analytical scoring algorithm and enhanced company-wide AI literacy by delivering lectures and workshops.

Professional Experience
AI Software Engineer / LLM Developer
May 2025 – Present
Trinetix
Valencia, Spain
Engineered multimodal LLM pipelines and automated agent workflows (20+ autonomous agents) using LangGraph, Python, and vision models to process, enrich, and summarize unstructured data.

Built comprehensive test suites using pytest to validate LLM output schemas, API integrations, and backend pipeline execution, improving overall system stability.

Architected an automated LLM extraction pipeline with structured Pydantic schemas and evaluation benchmarks, achieving 99% data extraction accuracy while communicating technical progress directly to Big Four consulting stakeholders.

Engineered a custom analytical scoring algorithm that matched legacy vendor performance, saving the client approximately $1,000,000 USD annually.

Delivered prompt engineering lectures and workshops to over 200 non-technical employees, enhancing company-wide AI literacy and adoption.

Data Analyst
Mar 2023 – Feb 2025
Self-Employed
Data Analyst Services for clients in Finance (Prague) and Energy (Qatar). Consulting startup for a Y Combinator pitch.

Cleaned and preprocessed large volumes of data by implementing multiprocessing, threading techniques, and data normalization. Improved data accuracy by 15%.

Developed and maintained dashboards using Tableau to visualize key performance indicators for stakeholders.

Analyzed complex datasets to identify trends and provide actionable insights for financial decision-making

Optimized the Engineering Design Register system using Linear Algebra principles, reducing data retrieval time by 30% and improving engineering data management accuracy.

Automated delay tracking workflows using JavaScript and Excel VBA, reducing manual tracking time by 40%.

Developed and maintained a real-time cryptocurrency trading data tracking system using Python, Pandas, SQL, and WebSockets.

Automated data collection and enrichment through advanced web scraping pipelines using Selenium and BeautifulSoup.

Advised startup leadership on machine learning pipelines and data analytics strategies in preparation for a Y Combinator pitch.

Project Manager / AI Specialist
Sep 2022 – Mar 2023
Legend Has It
Prague, Czechia
Managed a team of 5 delivering early-stage AI-driven projects utilizing GPT-3 for persona creation and interactive workflows.

Contributed prompt architecture and persona modeling for the Sophia Humanoid Robot project.

Tracked project progress and communicated status updates to stakeholders, fostering transparency.

Sales Manager/Coach
Aug 2018 – Mar 2021
Skyeng
Remote
Within 2 years 8 months, grew from a leading Sales Manager to Training Specialists Team Lead and an architect of training programs.

Conducted lectures, workshops, and examinations to onboard new hires onto the sales process to 30 people

Achieved a rate 20% above the target for sales.

Managed a team of 10 training specialists, including performance reviews, coaching, scheduling, and planning.

Developed and implemented new sales training materials, resulting in a 10% increase in team productivity.

Analyzed sales data to identify trends and opportunities, contributing to a 5% growth in quarterly revenue.

Education
Kharkiv Polytechnic University
Sep 2016
Dec 2018
Computer Science
Bachelor of Science (BS)
Minors:
AI Data Analysis"""




golden_standard = [
    {
        "inputs": {
            "job_description": """Your mission at Mercanis

At Mercanis, we are building the Agentic AI Procurement Suite that powers the procurement of tomorrow: digital, transparent, and intelligent.


We are looking for an experienced Agentic AI Engineer to join our growing AI team. In this role, you will design, build, and optimize agentic AI systems that automate complex procurement workflows and power intelligent decision-making across our platform.


You will work with cutting-edge technologies in Python, LangGraph, and AWS, integrating and fine-tuning models from leading providers such as OpenAI, Anthropic, and AWS Bedrock.


Your work will have a direct impact on how organizations streamline their procurement processes and leverage AI for strategic advantage.


Your responsibilities in this role

Strong professional experience in Python software development
Proven experience building AI-driven or agentic systems, preferably with LangGraph or similar frameworks
Solid understanding of Large Language Models (LLMs) and their integration with external APIs or structured data
Hands-on experience working with LLM providers such as OpenAI, Anthropic, or AWS Bedrock
Familiarity with cloud-based deployment and scaling, ideally using AWS services
Strong problem-solving skills with a focus on maintainable, efficient, and scalable code
A collaborative mindset and comfort working remotely with distributed teams
Curiosity, adaptability, and a passion for staying ahead in the evolving world of AI
Bonus: Experience with semantic search technologies (vector databases, embeddings, RAG systems)
Bonus: Strong background in measuring, evaluating, and optimizing AI system performance with clear metrics and benchmarking
Bonus: Experience implementing observability and monitoring solutions for AI systems to track quality and iterate on improvements
Bonus: Experience building or integrating MCP (Model Context Protocol) servers for extending AI capabilities
Bonus: Knowledge of agent-to-agent (A2A) communication patterns and multi-agent system architectures


Role requirements

Tech stack you will work with:

Languages: Python
Frameworks & Tools: LangGraph & related LLM orchestration tools, Docling, LiteLLM, Phoenix
Infrastructure: AWS (Lambda, S3, ECS, and more)
Models: OpenAI, Anthropic, AWS Bedrock, and other foundation model providers""",


            "cv": base_cv,
        },
        "outputs": {
            "tailored_content": """{
  "header": {
    "name": "Liliia Shrainer",
    "title": "AI Engineer",
    "email": "",
    "phone": "",
    "location": "Valencia, Spain",
    "linkedin": "linkedin.com/in/liliia-shrainer",
    "website": ""
  },
  "summary": "Residence and Work Permit (Autorizacion de Residencia y Trabajo). AI Engineer with 2 years of experience in Python, AI, and LLM engineering, building multimodal pipelines and agentic workflows using LangChain and LangGraph. Proven track record integrating LLMs with external APIs, designing evaluation benchmarks and automated extraction pipelines, and delivering analytical vendor-scoring algorithms that saved clients approximately $1,000,000 USD. Skilled in Python, FastAPI, pytest and production-quality software development; experienced in cloud-enabled deployments and performance benchmarking.",
  "experience": [
    {
      "title": "AI Software Engineer / LLM Developer",
      "company": "Trinetix",
      "location": "Valencia, Spain",
      "dates": "May 2025 – Present",
      "bullets": [
        "Engineered multimodal LLM pipelines and automated agent workflows (20+ autonomous agents) using LangGraph, Python, and vision models to process, enrich, and summarize unstructured data.",
        "Refactored core Python codebase to resolve critical AI API integration issues; implemented robust retry handling, rate limiting, and structured error handling for external model endpoints to improve reliability.",
        "Built comprehensive pytest suites and evaluation benchmarks to validate LLM output schemas, API integrations, and backend pipeline execution—improving system stability and enabling ongoing performance benchmarking.",
        "Architected an automated LLM extraction pipeline with structured Pydantic schemas and evaluation metrics, achieving 99% data extraction accuracy while communicating technical progress directly to Big Four consulting stakeholders.",
        "Engineered a custom analytical vendor-scoring algorithm that matched legacy vendor performance, saving the client approximately $1,000,000 USD annually.",
        "Delivered prompt-engineering lectures and workshops to over 200 non-technical employees, increasing company-wide AI literacy and adoption.",
        "Participated in code reviews and testing cycles, ensuring the quality and reliability of AI components and supporting production deployments."
      ]
    },
    {
      "title": "Data Analyst",
      "company": "Self-Employed",
      "location": "",
      "dates": "Mar 2023 – Feb 2025",
      "bullets": [
        "Cleaned and preprocessed large volumes of data, improving data accuracy by 15%.",
        "Collaborated with cross-functional teams to define data requirements and ensure data integrity.",
        "Developed and maintained dashboards using Tableau to visualize key performance indicators for stakeholders.",
        "Analyzed complex datasets to identify trends and provide actionable insights for financial decision-making.",
        "Optimized the Engineering Design Register system using linear algebra principles, reducing data retrieval time by 30% and improving engineering data management accuracy.",
        "Automated delay-tracking workflows using JavaScript and Excel VBA, reducing manual tracking time by 40%.",
        "Developed and maintained a real-time cryptocurrency trading data tracking system using Python, Pandas, SQL, and WebSockets.",
        "Automated data collection and enrichment through advanced web scraping pipelines using Selenium and BeautifulSoup.",
        "Optimized data processing throughput by implementing multiprocessing, threading techniques, and data normalization.",
        "Advised startup leadership on machine learning pipelines and data analytics strategies in preparation for a Y Combinator pitch."
      ]
    },
    {
      "title": "Project Manager / AI Specialist",
      "company": "Legend Has It",
      "location": "Prague, Czechia",
      "dates": "Sep 2022 – Mar 2023",
      "bullets": [
        "Managed a team of 5 delivering early-stage AI-driven projects utilizing GPT-3 for persona creation and interactive workflows.",
        "Contributed prompt architecture and persona modeling for the Sophia Humanoid Robot project.",
        "Tracked project progress and communicated status updates to stakeholders, fostering transparency."
      ]
    },
    {
      "title": "Sales Manager/Coach",
      "company": "Skyeng",
      "location": "Remote",
      "dates": "Aug 2018 – Mar 2021",
      "bullets": [
        "Conducted lectures, workshops, and examinations to onboard new hires onto the sales process for 30 people.",
        "Achieved a rate 20% above the target for sales.",
        "Managed a team of 10 training specialists, including performance reviews, coaching, scheduling, and planning.",
        "Developed and implemented new sales training materials, resulting in a 10% increase in team productivity.",
        "Analyzed sales data to identify trends and opportunities, contributing to a 5% growth in quarterly revenue."
      ]
    },
    {
      "title": "Backend Developer",
      "company": "Big Johnsons Burger Joint: Full-Stack Web Application",
      "location": "",
      "dates": "Jan 2026 – Present",
      "bullets": [
        "Designed and implemented a full-stack restaurant ordering web application using FastAPI and React, integrated with SQL database storage on a self-managed Linux VPS.",
        "Handled Redsys payment gateway integration, managing secure redirects, payment callbacks, and transaction verification in FastAPI."
      ]
    },
    {
      "title": "AI Software Developer",
      "company": "Spanish Etymology Application",
      "location": "",
      "dates": "Oct 2025 – Present",
      "bullets": [
        "Developed an interactive language learning application that decomposes Spanish vocabulary into Latin and Greek root components to generate contextual mnemonics.",
        "Orchestrated multi-step agentic reasoning chains using LangGraph, deployed Groq API for ultra-low latency inference, and integrated LangSmith for LLM tracing and evaluation with a Streamlit interface."
      ]
    },
    {
      "title": "AI Engineer",
      "company": "LLM as a Judge: Evaluation & Feedback Pipeline",
      "location": "",
      "dates": "Dec 2025 – Jan 2026",
      "bullets": [
        "Built a multi-model evaluation pipeline combining an LLM-as-a-Teacher and an LLM-as-a-Judge to grade and correct homework responses deterministically.",
        "Utilized LangChain and Pinecone vector search for RAG-based lookup of grammar rules and ethics guidelines, triggering automatic regenerations when scores fall below thresholds."
      ]
    }
  ],
  "skills": [
    "Slack",
    "Problem Solving",
    "Version Control (Git)",
    "Sales",
    "Analytics",
    "Communication",
    "Teamwork",
    "Collaboration",
    "Cross-Functional Communication",
    "Adaptability",
    "Continuous Learning",
    "Ethical Judgement",
    "Python",
    "FastAPI",
    "AsyncIO",
    "pytest",
    "Multiprocessing",
    "PostgreSQL",
    "Pydantic",
    "Git",
    "REST APIs",
    "Linux VPS Deployment",
    "Streamlit",
    "Threading",
    "AWS",
    "System Building",
    "Software Systems",
    "S3",
    "Software Development",
    "Data Engineering",
    "LangChain",
    "LangGraph",
    "LangSmith",
    "RAG",
    "Multimodal LLMs (Vision)",
    "Groq API",
    "Prompt Optimization",
    "Guardrails",
    "Agentic Workflows",
    "Structured Outputs",
    "Model Evaluation",
    "GenAI",
    "AI Evaluation",
    "Regulation (EU) 2024/1689",
    "Large Language Models",
    "Weaviate",
    "Pinecone",
    "SQL",
    "Redis",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "Machine Learning Foundations",
    "PyTorch",
    "Web Scraping (Selenium, BeautifulSoup)",
    "Linear Algebra",
    "Data Analysis",
    "Tableau",
    "Model Training",
    "PowerBI",
    "English (Fluent C1)",
    "Spanish (Intermediate B1)",
    "Ukrainian (Native)",
    "Chinese (Beginner)"
  ],
  "education": [
    {
      "degree": "Bachelor of Science (BS) in Computer Science",
      "school": "Kharkiv Polytechnic University",
      "dates": "Sep 2016 – Dec 2018",
      "details": "Minors: AI Data Analysis"
    }
  ]
}""",
        },
    },

    {
        "inputs": {
            "job_description": """If you're this person, we'd love to talk to you.

The Role

We are looking for applied AI engineers to build AI-native systems for BJAK's AI Finance Agent.



This is not a research-only role. We need builders who can use AI to automate real workflows, improve products, reduce manual work and make financial services easier for users and teams.



What You'll Own

Build AI-powered workflows, assistants, agents and automation systems.
Apply AI across customer support, CRM, onboarding, claims, renewals, payments, operations and internal tools.
Work with product and engineering teams to turn manual processes into scalable AI-native systems.
Build integrations with LLMs, internal data, APIs, documents, knowledge bases and business systems.
Design evaluation, monitoring and fallback flows so AI outputs are useful, safe and reliable.
Prototype quickly, test with users or operators, then productionize what works.
Improve speed, quality and consistency across workflows using AI where it creates real business value.


What We're Looking For

Strong software engineering foundation, preferably with Python and backend systems.
Hands-on experience building with LLM APIs, agents, RAG, workflow automation or AI tools.
Able to connect AI systems with real product, data and operational workflows.
Good judgement on where AI helps and where rule-based systems or human review are better.
Understands evaluation, accuracy, latency, cost, privacy and failure modes.
Fast builder who can prototype, test and ship practical systems.
Experience in fintech, insurance, support automation, CRM or operations automation is a strong advantage.


The Kind of Builder We Want

Practical AI builder, not just a prompt experimenter.
Thinks in workflows, systems and measurable quality.
Can build quickly but still cares about guardrails and reliability.
Comfortable working with messy real-world data and processes.
Honest about what AI can and cannot do.""",
            "cv": base_cv,
        },
        "outputs": {
            "tailored_content": """{
  "header": {
    "name": "Liliia Shrainer",
    "title": "AI Engineer",
    "email": "",
    "phone": "",
    "location": "Valencia, Spain",
    "linkedin": "linkedin.com/in/liliia-shrainer",
    "website": ""
  },
  "summary": "AI Engineer with a strong software engineering foundation in Python and backend systems. Proven track record in building AI-native systems, multimodal LLM pipelines, and automated agent workflows that drive real business value. Expert in FastAPI, LangChain, and LangGraph, with a focus on creating reliable automation for financial services and internal tools. Successfully saved clients approximately $1,000,000 USD through custom analytical scoring algorithms and enhanced organizational AI literacy through technical workshops.",
  "experience": [
    {
      "title": "AI Software Engineer / LLM Developer",
      "company": "Trinetix",
      "location": "Valencia, Spain",
      "dates": "May 2025 – Present",
      "bullets": [
        "Engineered multimodal LLM pipelines and automated agent workflows (20+ autonomous agents) using LangGraph and Python to automate complex business processes and unstructured data workflows.",
        "Refactored core Python codebase to resolve critical AI API integration bugs, implementing robust retry handling, rate-limiting, and fallback flows to ensure system reliability.",
        "Built comprehensive test suites using pytest to validate LLM output schemas and backend pipeline execution, identifying failure modes and improving overall system stability.",
        "Architected an automated LLM extraction pipeline with structured Pydantic schemas and evaluation benchmarks, achieving 99% accuracy for Big Four consulting stakeholders.",
        "Engineered a custom analytical scoring algorithm that matched legacy vendor performance, delivering $1,000,000 USD in annual business value.",
        "Delivered prompt engineering lectures and workshops to over 200 employees, enhancing company-wide AI literacy and adoption of internal tools.",
        "Participated in code reviews and testing cycles, ensuring the quality and reliability of AI-native components.",
        "Collaborated with product teams to integrate Large Language Models (LLMs) into existing software applications and business systems."
      ]
    },
    {
      "title": "Analytics & ML Consultant",
      "company": "Xyara",
      "location": "Prague, Czechia",
      "dates": "Jan 2025 – Feb 2025",
      "bullets": [
        "Advised startup leadership on machine learning pipelines and data analytics strategies in preparation for a Y Combinator pitch.",
        "Presented findings and research-backed recommendations to stakeholders, influencing data-driven decision-making across departments."
      ]
    },
    {
      "title": "Data Analyst",
      "company": "Qatar Energy COEC",
      "location": "Shanghai, China",
      "dates": "Jan 2024 – May 2024",
      "bullets": [
        "Optimized the Engineering Design Register system using Linear Algebra principles, reducing data retrieval time by 30% and improving business system accuracy.",
        "Automated delay tracking workflows using JavaScript and Excel VBA, reducing manual tracking time by 40% through process automation.",
        "Developed and maintained dashboards using Tableau to visualize key performance indicators and operational metrics for stakeholders."
      ]
    },
    {
      "title": "Data Analyst & Engineer",
      "company": "Oxygen Biotech",
      "location": "Prague, Czechia",
      "dates": "Mar 2023 – Oct 2023",
      "bullets": [
        "Developed and maintained a real-time cryptocurrency trading data tracking system using Python, Pandas, SQL, and WebSockets.",
        "Automated data collection and enrichment through advanced web scraping pipelines using Selenium and BeautifulSoup to feed internal data tools.",
        "Optimized data processing throughput by implementing multiprocessing, threading techniques, and data normalization for scalable backend systems.",
        "Developed and maintained ETL pipelines, ensuring data accuracy and accessibility for reporting needs.",
        "Assisted in data cleaning and preprocessing, improving data quality for analytical models and financial services research."
      ]
    },
    {
      "title": "Project Manager / AI Specialist",
      "company": "Legend Has It",
      "location": "Prague, Czechia",
      "dates": "Sep 2022 – Mar 2023",
      "bullets": [
        "Managed a team of 5 delivering early-stage AI-driven projects utilizing GPT-3 for persona creation and interactive workflows.",
        "Contributed prompt architecture and persona modeling for the Sophia Humanoid Robot project, focusing on conversational AI and LLM integration.",
        "Tracked project progress and communicated status updates to stakeholders, fostering transparency and alignment on business value."
      ]
    },
    {
      "title": "Sales Manager/Coach",
      "company": "Skyeng",
      "location": "Remote",
      "dates": "Aug 2018 – Mar 2021",
      "bullets": [
        "Conducted lectures, workshops, and examinations to onboard new hires onto the sales process and CRM workflows for 30 people.",
        "Achieved a sales rate 20% above target, consistently delivering high performance in a fast-paced environment.",
        "Managed a team of 10 training specialists, including performance reviews, coaching, scheduling, and planning.",
        "Developed and implemented new sales training materials, resulting in a 10% increase in team productivity.",
        "Analyzed sales data to identify trends and opportunities, contributing to a 5% growth in quarterly revenue."
      ]
    },
    {
      "title": "Backend Developer",
      "company": "Big Johnsons Burger Joint: Full-Stack Web Application",
      "location": "",
      "dates": "Jan 2026 – Present",
      "bullets": [
        "Designed and implemented a full-stack restaurant ordering web application using FastAPI and React, integrated with SQL database storage on a self-managed Linux VPS.",
        "Handled Redsys payment gateway integration, managing secure redirects, payment callbacks, and transaction verification in FastAPI."
      ]
    },
    {
      "title": "Project Developer",
      "company": "Spanish Etymology Application",
      "location": "",
      "dates": "Oct 2025 – Present",
      "bullets": [
        "Developed an interactive language learning application that decomposes Spanish vocabulary into Latin and Greek root components to generate contextual mnemonics.",
        "Orchestrated multi-step agentic reasoning chains using LangGraph, deployed Groq API for ultra-low latency inference, and integrated LangSmith for LLM tracing and evaluation."
      ]
    },
    {
      "title": "AI Engineer",
      "company": "LLM as a Judge: Evaluation & Feedback Pipeline",
      "location": "",
      "dates": "Dec 2025 – Jan 2026",
      "bullets": [
        "Built a multi-model evaluation pipeline combining an LLM-as-a-Teacher and an LLM-as-a-Judge to grade and correct responses deterministically.",
        "Utilized LangChain and Pinecone vector search for RAG-based lookup of grammar rules and ethics guidelines, triggering automatic regenerations when scores fall below thresholds."
      ]
    }
  ],
  "skills": [
    "Python",
    "FastAPI",
    "AsyncIO",
    "pytest",
    "Multiprocessing",
    "PostgreSQL",
    "Pydantic",
    "Git",
    "REST APIs",
    "Linux VPS Deployment",
    "Streamlit",
    "Threading",
    "AWS",
    "System Building",
    "Software Systems",
    "LangChain",
    "LangGraph",
    "LangSmith",
    "RAG",
    "Multimodal LLMs (Vision)",
    "Groq API",
    "Prompt Optimization",
    "Guardrails",
    "Agentic Workflows",
    "Structured Outputs",
    "Model Evaluation",
    "GenAI",
    "AI Evaluation",
    "Weaviate",
    "Pinecone",
    "SQL",
    "Redis",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "Machine Learning Foundations",
    "PyTorch",
    "Web Scraping (Selenium, BeautifulSoup)",
    "Linear Algebra",
    "Data Analysis",
    "Tableau",
    "Model Training",
    "PowerBI",
    "CS50: Introduction to Computer Science (Harvard University / edX)",
    "Introduction to FastAPI and Backend Development Fundamentals",
    "Advanced Learning Algorithms (DeepLearning.AI)",
    "Basic Image Classification with TensorFlow",
    "English (Fluent (C1))",
    "Spanish (Intermediate (B1))",
    "Ukrainian (Native)",
    "Chinese (Beginner)"
  ],
  "education": [
    {
      "degree": "Bachelor of Science (BS) in Computer Science",
      "school": "Kharkiv Polytechnic University",
      "dates": "Sep 2016 – Dec 2018",
      "details": "Minors: AI Data Analysis"
    }
  ]
}""",
        },
    },
    {
        "inputs": {
            "job_description": """We are looking for an AI Solutions Engineer with at least 4 years of experience in software development and hands-on experience building and deploying Generative AI solutions in production environments.


You will join a strategic initiative focused on designing, developing, and operating AI-powered solutions that improve operational efficiency, automate processes, and unlock business value through technologies such as Azure AI, Azure OpenAI, Microsoft Copilot, and intelligent agents.


Responsibilities



Design, develop, and deploy AI-powered applications and intelligent agents.
Build solutions using Large Language Models (LLMs), prompt engineering, and Retrieval-Augmented Generation (RAG).
Integrate AI solutions with enterprise applications, Microsoft 365 services, and internal knowledge sources.
Develop reusable components, integration patterns, and implementation standards.
Collaborate closely with operational teams and business stakeholders to transform use cases into production-ready solutions.
Ensure security, scalability, maintainability, and alignment with the wider AI technology ecosystem.
Monitor, support, and continuously improve deployed AI solutions.
Measure and track productivity gains and business outcomes enabled by AI.


Required Skills

4+ years of experience in software development.
Proven experience developing and deploying AI solutions in production environments.
Strong understanding of Generative AI, LLMs, prompt engineering, and RAG architectures.
Experience with Azure AI, Azure OpenAI, Microsoft Copilot Studio, or similar AI platforms.
Strong Python development skills.
Experience designing and consuming REST APIs.
Experience integrating solutions with Microsoft 365 and enterprise applications.
Knowledge of workflow automation platforms and process automation.
Experience with GitHub, testing, monitoring, and technical documentation.
Good understanding of AI security, access management, logging, and lifecycle management.
High level of English (C1 or above).


Nice to Have

Experience building AI Agents or multi-agent systems.
Experience with Azure AI Foundry, Azure AI Studio, or Azure Cognitive Services.
Knowledge of LangChain, LlamaIndex, Semantic Kernel, CrewAI, or similar frameworks.
Experience with Power Platform and Power Automate.
Familiarity with Docker, CI/CD pipelines, and cloud-native environments.
Experience working in enterprise-scale environments.""",
            "cv": base_cv,
        },
        "outputs": {
            "tailored_content": """{
  "header": {
    "name": "Liliia Shrainer",
    "title": "AI Solutions Engineer",
    "email": "lilischreiner3@gmail.com",
    "phone": "+34627512910",
    "location": "Valencia, Spain",
    "linkedin": "linkedin.com/in/liliia-shrainer",
    "website": ""
  },
  "summary": "AI Solutions Engineer with over 4 years of experience in software development and a proven track record in building and deploying Generative AI solutions in production environments. Expert in designing multimodal LLM pipelines, RAG architectures, and automated agent workflows using Python, LangChain, and LangGraph. Skilled in integrating AI solutions with enterprise applications and REST APIs to drive operational efficiency and business value. Successfully saved clients approximately $1,000,000 USD through custom analytical scoring algorithms and enhanced company-wide AI literacy through technical workshops.",
  "experience": [
    {
      "title": "AI Software Engineer / LLM Developer",
      "company": "Trinetix",
      "location": "Valencia, Spain",
      "dates": "May 2025 – Present",
      "bullets": [
        "Engineered multimodal LLM pipelines and automated agent workflows (20+ autonomous agents) using LangGraph, Python, and vision models to process, enrich, and summarize unstructured data for enterprise applications.",
        "Refactored core Python codebase to resolve critical AI API integration bugs, implementing robust retry handling, rate-limiting logic, and error handling for external model endpoints to ensure scalability.",
        "Built comprehensive test suites using pytest to validate LLM output schemas, REST API integrations, and backend pipeline execution, improving overall system stability and maintainability.",
        "Architected an automated LLM extraction pipeline with structured Pydantic schemas and evaluation benchmarks, achieving 99% data extraction accuracy while communicating technical progress and business value to Big Four consulting stakeholders.",
        "Engineered a custom analytical scoring algorithm that matched legacy vendor performance, saving the client approximately $1,000,000 USD annually through improved operational efficiency.",
        "Delivered prompt engineering lectures and workshops to over 200 non-technical employees, enhancing company-wide AI literacy and adoption of intelligent agents.",
        "Participated in code reviews and testing cycles, ensuring the quality, security, and reliability of AI components within the GitHub ecosystem.",
        "Collaborated with senior engineers to integrate Large Language Models (LLMs) into existing software applications and Microsoft 365 services."
      ]
    },
    {
      "title": "Analytics & ML Consultant",
      "company": "Xyara",
      "location": "Prague, Czechia",
      "dates": "Jan 2025 – Feb 2025",
      "bullets": [
        "Advised startup leadership on machine learning pipelines and data analytics strategies in preparation for a Y Combinator pitch, focusing on scalability and technical documentation.",
        "Presented findings and recommendations to stakeholders, influencing data-driven decision-making and process automation across departments."
      ]
    },
    {
      "title": "Data Analyst",
      "company": "Qatar Energy COEC",
      "location": "Shanghai, China",
      "dates": "Jan 2024 – May 2024",
      "bullets": [
        "Optimized the Engineering Design Register system using Linear Algebra principles, reducing data retrieval time by 30% and improving engineering data management accuracy.",
        "Automated delay tracking workflows using JavaScript and Excel VBA, reducing manual tracking time by 40% and enhancing operational efficiency.",
        "Developed and maintained dashboards using Tableau to visualize key performance indicators and business outcomes for stakeholders."
      ]
    },
    {
      "title": "Data Analyst & Engineer",
      "company": "Oxygen Biotech",
      "location": "Prague, Czechia",
      "dates": "Mar 2023 – Oct 2023",
      "bullets": [
        "Developed and maintained a real-time cryptocurrency trading data tracking system using Python, Pandas, SQL, and WebSockets.",
        "Automated data collection and enrichment through advanced web scraping pipelines using Selenium and BeautifulSoup, ensuring data accessibility for reporting.",
        "Optimized data processing throughput by implementing multiprocessing, threading techniques, and data normalization for enterprise-scale environments.",
        "Developed and maintained ETL pipelines, ensuring data accuracy, security, and accessibility for reporting needs.",
        "Assisted in data cleaning and preprocessing, improving data quality for analytical models and workflow automation."
      ]
    },
    {
      "title": "Project Manager / AI Specialist",
      "company": "Legend Has It",
      "location": "Prague, Czechia",
      "dates": "Sep 2022 – Mar 2023",
      "bullets": [
        "Managed a team of 5 delivering early-stage AI-driven projects utilizing GPT-3 for persona creation and interactive agentic workflows.",
        "Contributed prompt architecture and persona modeling for the Sophia Humanoid Robot project, focusing on LLM integration patterns.",
        "Tracked project progress and communicated status updates to stakeholders, fostering transparency and alignment with business value."
      ]
    },
    {
      "title": "Sales Manager/Coach",
      "company": "Skyeng",
      "location": "Remote",
      "dates": "Aug 2018 – Mar 2021",
      "bullets": [
        "Conducted lectures, workshops, and examinations to onboard new hires onto the sales process to 30 people, improving team operational efficiency.",
        "Achieved a rate 20% above the target for sales through strategic communication and process optimization.",
        "Managed a team of 10 training specialists, including performance reviews, coaching, scheduling, and planning.",
        "Developed and implemented new sales training materials, resulting in a 10% increase in team productivity.",
        "Analyzed sales data to identify trends and opportunities, contributing to a 5% growth in quarterly revenue."
      ]
    },
    {
      "title": "Backend Developer",
      "company": "Big Johnsons Burger Joint: Full-Stack Web Application",
      "location": "",
      "dates": "Jan 2026 – Present",
      "bullets": [
        "Designed and implemented a full-stack restaurant ordering web application using FastAPI and React, integrated with SQL database storage on a self-managed Linux VPS.",
        "Handled Redsys payment gateway integration, managing secure redirects, payment callbacks, and transaction verification in FastAPI."
      ]
    },
    {
      "title": "Project Lead / Developer",
      "company": "Spanish Etymology Application",
      "location": "",
      "dates": "Oct 2025 – Present",
      "bullets": [
        "Developed an interactive language learning application that decomposes Spanish vocabulary into Latin and Greek root components to generate contextual mnemonics.",
        "Orchestrated multi-step agentic reasoning chains using LangGraph, deployed Groq API for ultra-low latency inference, and integrated LangSmith for LLM tracing and evaluation with a Streamlit interface."
      ]
    },
    {
      "title": "AI Engineer",
      "company": "LLM as a Judge: Evaluation & Feedback Pipeline",
      "location": "",
      "dates": "Dec 2025 – Jan 2026",
      "bullets": [
        "Built a multi-model evaluation pipeline combining an LLM-as-a-Teacher and an LLM-as-a-Judge to grade and correct homework responses deterministically.",
        "Utilized LangChain and Pinecone vector search for RAG-based lookup of grammar rules and ethics guidelines, triggering automatic regenerations when scores fall below thresholds."
      ]
    }
  ],
  "skills": [
    "Python",
    "FastAPI",
    "AsyncIO",
    "pytest",
    "Multiprocessing",
    "PostgreSQL",
    "Pydantic",
    "Git",
    "REST APIs",
    "Linux VPS Deployment",
    "Streamlit",
    "Threading",
    "AWS",
    "GitHub",
    "Azure",
    "Docker",
    "CI/CD",
    "LangChain",
    "LangGraph",
    "LangSmith",
    "RAG",
    "Multimodal LLMs (Vision)",
    "Groq API",
    "Large Language Models",
    "Guardrails",
    "Agentic Workflows",
    "Structured Outputs",
    "Model Evaluation",
    "GenAI",
    "Prompt Engineering",
    "Azure OpenAI",
    "Microsoft 365 Integration",
    "Weaviate",
    "Pinecone",
    "SQL",
    "Redis",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "Machine Learning Foundations",
    "PyTorch",
    "Web Scraping (Selenium, BeautifulSoup)",
    "Linear Algebra",
    "Data Analysis",
    "Tableau",
    "Model Training",
    "PowerBI",
    "Languages: English (Fluent (C1))",
    "Languages: Spanish (Intermediate (B1))",
    "Languages: Ukrainian (Native)",
    "Languages: Chinese (Beginner)",
    "Certification: CS50: Introduction to Computer Science (Harvard University / edX)",
    "Certification: Introduction to FastAPI and Backend Development Fundamentals",
    "Certification: Advanced Learning Algorithms (DeepLearning.AI)",
    "Certification: Basic Image Classification with TensorFlow"
  ],
  "education": [
    {
      "degree": "Bachelor of Science (BS) in Computer Science",
      "school": "Kharkiv Polytechnic University",
      "dates": "Sep 2016 – Dec 2018",
      "details": "Minors: AI Data Analysis"
    }
  ]
}""",
        },
    },
    {
        "inputs": {
            "job_description": """Grafana Labs, the company behind the open observability cloud, is founded on the principles of open source, open standards, open ecosystems, and open culture. Grafana Cloud, our fully managed observability platform, is flexible and built for scale. With Grafana Cloud's actually useful AI, organizations can see, understand, and act on all their disparate data to move at the speed of their ambitions. Today, more than 35 million users and 7,000+ customers – including Anthropic, Bloomberg, NVIDIA, Microsoft, and Salesforce – trust Grafana Labs to ensure reliability of their applications and systems, resolve incidents quickly, and optimize their telemetry to reduce noise and cost. We are a 100% remote company with 1,600+ team members across 40+ countries, and we’re backed by leading investors including Lightspeed Venture Partners, Sequoia Capital, GIC, Coatue, J.P. Morgan, CapitalG, and Lead Edge Capital. Learn more at grafana.com and follow us on LinkedIn and X.

We’re scaling fast and staying true to what makes us different: an open-source legacy, a global collaborative culture, and a passion for meaningful work. Our team thrives in an innovation-driven environment where transparency, autonomy, and trust fuel everything we do.

You may not meet every requirement, and that’s okay. If this role excites you, we’d love you to raise your hand for what could be a truly career-defining opportunity.

This is a remote position. We are considering candidates in Germany, Ireland, Sweden, Spain and the UK only.

The Opportunity:

At Grafana Labs, we build observability tools that help users understand, respond to, and improve their systems – regardless of scale, complexity, or tech stack. We recently started a skunkworks initiative with a mission to bring observability to the rest of the business via general data analytics. Our goal is to make Grafana the single best place where humans and AI agents understand and act on data from across the enterprise. We build systems that help users make sense of their sea of data through AI-driven features in use cases like product analytics and sales data. These capabilities lower the barrier of domain expertise and surface meaningful signals from messy data. 

The 2H team is a mix of seasoned Grafanistas and new hires. We operate with a high degree of autonomy and ownership, both as individuals and as a team. Engineers are empowered to make decisions, move quickly, and validate ideas early – while being supported by a deeply collaborative culture that values curiosity, feedback, and cross-functional partnership.

We’re looking for an AI Software Engineer with a strong software engineering background, a quick iteration mindset, and a passion for experimentation – balanced by a focus on shipping and scaling impactful features that deliver value to users. As part of our skunkworks initiative, you'll wear multiple hats and won't rely on cross-functional teams that typically support other teams inside Grafana Labs engineering. You will design, develop, test, and ship AI-powered features that can manage dealing with large datasets, while also expanding the capabilities of analytics-focused AI agents to assist users with information retrieval. As the team matures, there’s a broad opportunity to expand or redefine this role based on impact and initiative.

What You’ll Be Doing:

Build and deliver AI solutions: Take ownership of developing delightful, high-performance AI features to help users discover, organize, and optimize access to large datasets.
Rapid experimentation and iteration: Implement a highly iterative process where you quickly prototype, test, and validate with real users, including shipping and evolving LLM- or agent-powered workflows for the data engineering lifecycle.
Collaborate: Work with the rest of the team to shape AI-driven product features, including the integration of agentic components with internal tools like Slack and alerting systems while engaging with internal data teams for dogfooding.
Utilize AI tools effectively: Use AI and automation tools to enhance both product functionality and your own development workflows. 
Effective communication: You’ll be working in a highly dynamic and collaborative environment, so we need someone who can communicate effectively and contribute across teams.
Ownership and impact: Take full ownership of the AI solutions you develop, ensuring they are not only innovative but also scalable, maintainable, and aligned with real user workflows.
What Makes You a Great Fit:

Strong engineering skills: Solid experience building production-grade, user-facing software systems. You’re a self-starter, capable of tackling complex engineering problems and making UI design decisions with minimal supervision.
AI experience with a practical mindset: You’re familiar with AI technologies and frameworks, and you focus on delivering high-quality solutions that work in the real world, not just in theory. 
Quick iteration and experimentation: You’re comfortable releasing prototypes, collecting feedback, and iterating with a pragmatic mindset.
Proven initiative: You take ownership and drive projects forward, pushing boundaries to find the most impactful solutions. You can deal with ambiguity and are able to define scope where things are loosely defined. 
Collaborative attitude: You communicate effectively with your peers. You’re open to feedback, and you bring a solutions-oriented mindset to the table.
Requirements: 

Experience with LLMs, context engineering, and building applications powered by GenAI.
Proven track record of delivering software that made it into production and is actively used by users. 
Exposure to working in cloud-native environments (e.g., AWS, GCP, Azure).
Experience using observability tools to understand and troubleshoot system behavior.
Bonus Points For:

Experience building or working with agent frameworks or multi‑agent workflows.
Experience as a data analyst or work with data platforms (e.g., Looker, Tableau, PowerBI, Snowflake, DataBricks)
Experience building tools for data engineering.""",
            "cv": base_cv,
        },
        
        "outputs": {"tailored_content": """ {
  "header": {
    "name": "Liliia Shrainer",
    "title": "AI Engineer",
    "email": "lilischreiner3@gmail.com",
    "phone": "+34627512910",
    "location": "Valencia, Spain",
    "linkedin": "linkedin.com/in/liliia-shrainer",
    "website": ""
  },
  "summary": "Residence and Work Permit (Autorización de Residencia y Trabajo). AI Engineer with 2 years of experience building production-ready LLM pipelines, agentic workflows, and data engineering tooling. Strong Python background (FastAPI, pytest) with hands-on work in multimodal LLMs, RAG/vector search, context engineering, and automated evaluation. Proven record of improving system stability, shipping iterative prototypes, and translating technical work into business impact (including ~ $1,000,000 USD client savings). Comfortable working with cloud-native services (AWS) and collaborating across product, analytics, and engineering teams.",
  "experience": [
    {
      "title": "AI Software Engineer / LLM Developer",
      "company": "Trinetix",
      "location": "Valencia, Spain",
      "dates": "May 2025 – Present",
      "bullets": [
        "Engineered multimodal LLM pipelines and automated agent workflows (20+ autonomous agents) using LangGraph, Python, and vision models to process, enrich, and summarize unstructured data for information retrieval and downstream analytics.",
        "Refactored core Python codebase to resolve critical AI API integration bugs by implementing robust retry handling, rate-limiting logic, and structured error handling—improving reliability of external model endpoints.",
        "Built comprehensive pytest suites to validate LLM output schemas, API integrations, and backend pipeline execution, improving overall system stability and accelerating safe iteration.",
        "Architected an automated LLM extraction pipeline with structured Pydantic schemas and evaluation benchmarks, achieving 99% extraction accuracy while communicating technical progress directly to Big Four consulting stakeholders.",
        "Engineered a custom analytical scoring algorithm that matched legacy vendor performance, saving the client approximately $1,000,000 USD annually.",
        "Delivered prompt engineering lectures and hands-on workshops to 200+ non-technical employees to improve AI literacy and internal adoption.",
        "Participated in code reviews, testing cycles, and collaborated with senior engineers to integrate LLMs into existing software applications and internal tooling."
      ]
    },
    {
      "title": "Analytics & ML Consultant",
      "company": "Xyara",
      "location": "Prague, Czechia",
      "dates": "Jan 2025 – Feb 2025",
      "bullets": [
        "Advised startup leadership on machine learning pipelines and data analytics strategies to prepare for a Y Combinator pitch, including recommendations for model evaluation and data instrumentation.",
        "Presented findings and recommendations to stakeholders, influencing data-driven decision-making across departments."
      ]
    },
    {
      "title": "Data Analyst",
      "company": "Qatar Energy COEC",
      "location": "Shanghai, China",
      "dates": "Jan 2024 – May 2024",
      "bullets": [
        "Optimized the Engineering Design Register system using Linear Algebra principles, reducing data retrieval time by 30% and improving engineering data management accuracy.",
        "Automated delay-tracking workflows using JavaScript and Excel VBA, reducing manual tracking time by 40%.",
        "Developed and maintained Tableau dashboards to visualize KPIs and operational metrics for stakeholders, improving visibility into program performance."
      ]
    },
    {
      "title": "Data Analyst & Engineer",
      "company": "Oxygen Biotech",
      "location": "Prague, Czechia",
      "dates": "Mar 2023 – Oct 2023",
      "bullets": [
        "Developed and maintained a real-time cryptocurrency trading data tracking system using Python, Pandas, SQL, and WebSockets, implementing monitoring of data throughput and latency.",
        "Automated data collection and enrichment through web scraping pipelines using Selenium and BeautifulSoup, improving data coverage for analytics.",
        "Optimized data processing throughput using multiprocessing and threading techniques and applied data normalization to improve downstream model input quality.",
        "Built and maintained ETL pipelines to ensure data accuracy and accessibility for reporting and analysis."
      ]
    },
    {
      "title": "Project Manager / AI Specialist",
      "company": "Legend Has It",
      "location": "Prague, Czechia",
      "dates": "Sep 2022 – Mar 2023",
      "bullets": [
        "Managed a team of 5 delivering early-stage AI-driven projects using GPT-3 for persona creation and interactive workflows, coordinating development and delivery timelines.",
        "Contributed prompt architecture and persona modeling for the Sophia Humanoid Robot project, shaping conversational behavior and response constraints.",
        "Tracked project progress and communicated status updates to stakeholders, fostering transparency and alignment."
      ]
    },
    {
      "title": "Sales Manager/Coach",
      "company": "Skyeng",
      "location": "Remote",
      "dates": "Aug 2018 – Mar 2021",
      "bullets": [
        "Within 2 years and 8 months, grew from a leading Sales Manager to Training Specialists Team Lead and an architect of training programs.",
        "Conducted lectures, workshops, and examinations to onboard 30 new hires onto the sales process.",
        "Achieved sales results 20% above target.",
        "Managed a team of 10 training specialists, including performance reviews, coaching, scheduling, and planning.",
        "Developed and implemented sales training materials, resulting in a 10% increase in team productivity.",
        "Analyzed sales data to identify trends and opportunities, contributing to a 5% growth in quarterly revenue."
      ]
    },
    {
      "title": "Backend Developer",
      "company": "Big Johnsons Burger Joint: Full-Stack Web Application (Project)",
      "location": "",
      "dates": "Jan 2026 – Present",
      "bullets": [
        "Designed and implemented a full-stack restaurant ordering web application using FastAPI and React, integrated with SQL database storage on a self-managed Linux VPS.",
        "Handled Redsys payment gateway integration, managing secure redirects, payment callbacks, and transaction verification in FastAPI."
      ]
    },
    {
      "title": "Developer / AI Engineer",
      "company": "Spanish Etymology Application (Project)",
      "location": "",
      "dates": "Oct 2025 – Present",
      "bullets": [
        "Developed an interactive language learning application that decomposes Spanish vocabulary into Latin and Greek root components to generate contextual mnemonics.",
        "Orchestrated multi-step agentic reasoning chains using LangGraph, deployed Groq API for ultra-low latency inference, and integrated LangSmith for LLM tracing and evaluation with a Streamlit interface."
      ]
    },
    {
      "title": "AI Engineer",
      "company": "LLM as a Judge: Evaluation & Feedback Pipeline (Project)",
      "location": "",
      "dates": "Dec 2025 – Jan 2026",
      "bullets": [
        "Built a multi-model evaluation pipeline combining an LLM-as-a-Teacher and an LLM-as-a-Judge to grade and correct homework responses deterministically.",
        "Utilized LangChain and Pinecone vector search for RAG-based lookup of grammar rules and ethics guidelines, triggering automatic regenerations when scores fall below thresholds."
      ]
    }
  ],
  "skills": [
    "Slack",
    "Problem Solving",
    "Version Control (Git)",
    "Sales",
    "Analytics",
    "Communication",
    "Teamwork",
    "Collaboration",
    "Cross-Functional Communication",
    "Adaptibility",
    "Continuous Learning",
    "Ethical Judgement",
    "Python",
    "FastAPI",
    "AsyncIO",
    "pytest",
    "Multiprocessing",
    "PostgreSQL",
    "Pydantic",
    "Git",
    "REST APIs",
    "Linux VPS Deployment",
    "Streamlit",
    "Threading",
    "AWS",
    "Data Engineering",
    "LangChain",
    "LangGraph",
    "LangSmith",
    "RAG",
    "Multimodal LLMs (Vision)",
    "Groq API",
    "Prompt Optimization",
    "Guardrails",
    "Agentic Workflows",
    "Structured Outputs",
    "Model Evaluation",
    "GenAI",
    "AI Evaluation",
    "Regulation (EU) 2024/1689",
    "Weaviate",
    "Pinecone",
    "SQL",
    "Redis",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "Machine Learning Foundations",
    "PyTorch",
    "Web Scraping (Selenium, BeautifulSoup)",
    "Linear Algebra",
    "Data Analysis",
    "Tableau",
    "Model Training",
    "PowerBI",
    "English (Fluent (C1))",
    "Spanish (Intermediate (B1))",
    "Ukrainian (Native)",
    "Chinese (Beginner)"
  ],
  "education": [
    {
      "degree": "Bachelor of Science (BS) in Computer Science",
      "school": "Kharkiv Polytechnic University",
      "dates": "Sep 2016 – Dec 2018",
      "details": "Minors: AI Data Analysis"
    },
    {
      "degree": "Certificate: CS50: Introduction to Computer Science",
      "school": "Harvard University / edX",
      "dates": "",
      "details": ""
    },
    {
      "degree": "Certificate: Introduction to FastAPI and Backend Development Fundamentals",
      "school": "",
      "dates": "",
      "details": ""
    },
    {
      "degree": "Certificate: Advanced Learning Algorithms",
      "school": "DeepLearning.AI",
      "dates": "",
      "details": ""
    },
    {
      "degree": "Certificate: Basic Image Classification with TensorFlow",
      "school": "",
      "dates": "",
      "details": ""
    }
  ]
}
        """ 
        }
        },

    {
        "inputs": {
            "job_description": """Our Vision

We believe in a world where everyone, regardless of their country’s wealth or frontiers, enjoys access to medicines and healthcare when they need it.


Our Mission

We work tirelessly to remove access barriers faced by patients and caregivers across Low and Middle-Income Countries (LMICs) when seeking quality medicines and quality healthcare.


Who We Are: Accelerating access to medicines for all

Imagine a world where critical medicines are within reach, affordable, and synonymous with quality, no matter where you are. That is the world we're building with our unique, demand-aggregation model that unites healthcare providers across LMICs. At the heart of our identity is a single, resolute commitment: to build a future where geography and income never stand between any individual and life-saving medicines. Our platform isn't merely a space for transactions, we unlock affordable access to medicines by aggregating demand across healthcare providers. We also help manufacturers build a sustainable and reliable global access strategy.


Axmed Global Health Advisory is the access-focused advisory arm of Axmed, a social impact company dedicated to improving access to medicines across low- and middle-income countries (LMICs). As a specialized advisory firm, Axmed Global Health Advisory partners with private sector, global health organizations, and industry stakeholders to develop and implement market access strategies, innovative financing models, and go-to-market solutions tailored to LMIC healthcare systems.


The role:

We're hiring an AI Engineer to build production-grade autonomous agents that run the key steps of our procurement marketplace, with a human in the loop where it matters. This is not a research role. You'll ship agents into production that handle real transactions, real suppliers, and real buyers, and you'll be accountable for how they perform once they're live.
You'll work closely with our commercial and operations teams to identify which parts of the procurement workflow (sourcing, quoting, order matching, supplier follow-up, compliance checks, and more) are ready for agentic automation. You'll be the one who designs, builds, ships, and monitors those agents end-to-end.


What you'll own:

Design and build end-to-end agents that autonomously perform key steps of the procurement workflow
Build in human review checkpoints where autonomy carries too much risk, deciding where agents should act alone and where they should flag for a person
Own the full lifecycle: design, build, deploy, monitor, iterate. You ship it, you watch it, you fix it
Instrument agents so failures are visible fast: logging, monitoring, and alerting, not just “it works on my machine”
Work directly with commercial and operations teams to map real workflow steps into agent specs. You'll need to understand the procurement process, not just the code
Make judgment calls on reliability, cost, and latency trade-offs for a live marketplace, and continuously improve agents based on real production data and failure modes


What we're looking for:

Strong software engineering fundamentals: you can build reliable systems, not just call an LLM API
Fluency with the modern agentic stack: LLM APIs and orchestration frameworks, tool use and function calling, Python, cloud infrastructure, CI/CD
Ability to design human-in-the-loop systems, knowing where automation should stop and a person should step in


Experience:

You have built and shipped AI agents into a live production environment, not just prototyped them
You have owned systems after launch: monitoring them, debugging failures, and iterating on real production data
You have worked in environments with ambiguity and limited infrastructure, where you decide the approach rather than execute one


Traits:

A builder's mindset: you would rather ship something real and iterate than perfect something in isolation
Comfortable with ambiguity, making judgment calls rather than waiting for a full spec
Collaborative with non-technical teams, translating real workflows into working systems


Right to Work: As an early-stage company, we are not currently able to offer visa sponsorship or relocation support. For this reason, candidates must already have the legal right to work in the country where they are based.""",
            "cv": base_cv,
        },
        "outputs": {
            "tailored_content": """{
  "header": {
    "name": "Liliia Shrainer",
    "title": "AI Engineer",
    "email": "lilischreiner3@gmail.com",
    "phone": "+34627512910",
    "location": "Valencia, Spain",
    "linkedin": "linkedin.com/in/liliia-shrainer",
    "website": ""
  },
  "summary": "Residence and Work Permit (Autorización de Residencia y Trabajo). AI Engineer with 2 years of experience building production-grade LLM pipelines and agentic workflows using Python, FastAPI, LangChain and LangGraph. Proven track record shipping autonomous agents and stabilizing API integrations through robust retry/backoff, rate-limiting and schema validation; built test suites and automated extraction pipelines that improved extraction accuracy to 99%. Delivered client-facing technical work (including Big Four stakeholders) and company-wide AI workshops, and saved clients ~$1,000,000 USD through a custom analytical scoring algorithm.",
  "experience": [
    {
      "title": "AI Software Engineer / LLM Developer",
      "company": "Trinetix",
      "location": "Valencia, Spain",
      "dates": "May 2025 – Present",
      "bullets": [
        "Engineered multimodal LLM pipelines and automated agent workflows (20+ autonomous agents) using LangGraph, Python, and vision models to process, enrich, and summarize unstructured data for downstream systems.",
        "Refactored core Python codebase to resolve critical AI API integration bugs, implementing robust retry/backoff, rate-limiting, and error handling for external model endpoints, reducing integration failures and improving reliability.",
        "Built pytest-based test suites and Pydantic schema validation to verify LLM outputs, API integrations, and pipeline execution, improving system stability and enabling faster debugging cycles.",
        "Architected an automated LLM extraction pipeline with structured Pydantic schemas and evaluation benchmarks, achieving 99% data extraction accuracy while communicating technical progress directly to Big Four consulting stakeholders.",
        "Engineered a custom analytical scoring algorithm that matched legacy vendor performance, saving the client approximately $1,000,000 USD annually.",
        "Delivered prompt engineering lectures and hands-on workshops to over 200 non-technical employees, increasing AI literacy and adoption across commercial and operations teams.",
        "Participated in code reviews and collaborated with senior engineers to integrate LLMs into existing applications and maintenance workflows."
      ]
    },
    {
      "title": "Data Analyst",
      "company": "Self-Employed",
      "location": "",
      "dates": "Mar 2023 – Feb 2025",
      "bullets": [
        "Data Analyst Services for clients in Finance (Prague) and Energy (Qatar). Consulting startup for a Y Combinator pitch.",
        "Cleaned and preprocessed large volumes of data, improving data accuracy by 15%.",
        "Collaborated with cross-functional teams to define data requirements and ensure data integrity for finance and energy clients.",
        "Developed and maintained Tableau dashboards to visualize KPIs for stakeholders and inform financial decision-making.",
        "Analyzed complex datasets to identify trends and provide actionable insights for financial decision-making.",
        "Optimized the Engineering Design Register system using linear algebra principles, reducing data retrieval time by 30% and improving engineering data management accuracy.",
        "Automated delay-tracking workflows using JavaScript and Excel VBA, reducing manual tracking time by 40%.",
        "Developed and maintained a real-time cryptocurrency trading data tracking system using Python, Pandas, SQL, and WebSockets.",
        "Automated data collection and enrichment through web scraping pipelines using Selenium and BeautifulSoup.",
        "Optimized data processing throughput by implementing multiprocessing and threading techniques, and applied data normalization to improve downstream model performance.",
        "Advised startup leadership on machine learning pipelines and data analytics strategies in preparation for a Y Combinator pitch."
      ]
    },
    {
      "title": "Project Manager / AI Specialist",
      "company": "Legend Has It",
      "location": "Prague, Czechia",
      "dates": "Sep 2022 – Mar 2023",
      "bullets": [
        "Managed a team of 5 delivering early-stage AI-driven projects utilizing GPT-3 for persona creation and interactive workflows, coordinating delivery timelines and technical scope.",
        "Contributed prompt architecture and persona modeling for the Sophia Humanoid Robot project, defining persona behaviors and response constraints.",
        "Tracked project progress and communicated status updates to stakeholders, fostering transparency and alignment between technical and non-technical teams."
      ]
    },
    {
      "title": "Sales Manager/Coach",
      "company": "Skyeng",
      "location": "Remote",
      "dates": "Aug 2018 – Mar 2021",
      "bullets": [
        "Conducted lectures, workshops, and examinations to onboard 30 new hires onto the sales process.",
        "Achieved a sales rate 20% above target through coaching and process improvements.",
        "Managed a team of 10 training specialists, including performance reviews, coaching, scheduling, and planning.",
        "Developed and implemented new sales training materials, resulting in a 10% increase in team productivity.",
        "Analyzed sales data to identify trends and opportunities, contributing to a 5% growth in quarterly revenue."
      ]
    },
    {
      "title": "Backend Developer",
      "company": "Big Johnsons Burger Joint: Full-Stack Web Application",
      "location": "",
      "dates": "Jan 2026 – Present",
      "bullets": [
        "Designed and implemented a full-stack restaurant ordering web application using FastAPI and React, integrated with SQL database storage on a self-managed Linux VPS.",
        "Handled Redsys payment gateway integration, managing secure redirects, payment callbacks, and transaction verification in FastAPI."
      ]
    },
    {
      "title": "AI Software Developer",
      "company": "Spanish Etymology Application",
      "location": "",
      "dates": "Oct 2025 – Present",
      "bullets": [
        "Developed an interactive language learning application that decomposes Spanish vocabulary into Latin and Greek root components to generate contextual mnemonics.",
        "Orchestrated multi-step agentic reasoning chains using LangGraph, deployed Groq API for ultra-low latency inference, and integrated LangSmith for LLM tracing and evaluation with a Streamlit interface."
      ]
    },
    {
      "title": "AI Engineer",
      "company": "LLM as a Judge: Evaluation & Feedback Pipeline",
      "location": "",
      "dates": "Dec 2025 – Jan 2026",
      "bullets": [
        "Built a multi-model evaluation pipeline combining an LLM-as-a-Teacher and an LLM-as-a-Judge to grade and correct homework responses deterministically.",
        "Utilized LangChain and Pinecone vector search for RAG-based lookup of grammar rules and ethics guidelines, triggering automatic regenerations when scores fall below thresholds."
      ]
    }
  ],
  "skills": [
    "Slack",
    "Problem Solving",
    "Version Control (Git)",
    "Sales",
    "Analytics",
    "Communication",
    "Teamwork",
    "Collaboration",
    "Cross-Functional Communication",
    "Adaptability",
    "Continuous Learning",
    "Ethical Judgement",
    "Python",
    "FastAPI",
    "AsyncIO",
    "pytest",
    "Multiprocessing",
    "PostgreSQL",
    "Pydantic",
    "Git",
    "REST APIs",
    "Linux VPS Deployment",
    "Streamlit",
    "Threading",
    "AWS",
    "System Building",
    "Software Systems",
    "CI/CD",
    "Monitoring",
    "LangChain",
    "LangGraph",
    "LangSmith",
    "RAG",
    "Multimodal LLMs (Vision)",
    "Groq API",
    "Prompt Optimization",
    "Guardrails",
    "Agentic Workflows",
    "Structured Outputs",
    "Model Evaluation",
    "GenAI",
    "AI Evaluation",
    "Regulation (EU) 2024/1689",
    "Weaviate",
    "Pinecone",
    "SQL",
    "Redis",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "Machine Learning Foundations",
    "PyTorch",
    "Web Scraping (Selenium, BeautifulSoup)",
    "Linear Algebra",
    "Data Analysis",
    "Tableau",
    "Model Training",
    "PowerBI",
    "English Fluent C1",
    "Spanish Intermediate B1",
    "Ukrainian Native",
    "Chinese Beginner"
  ],
  "education": [
    {
      "degree": "Bachelor of Science (BS) in Computer Science",
      "school": "Kharkiv Polytechnic University",
      "dates": "Sep 2016 – Dec 2018",
      "details": "Minors: AI Data Analysis"
    }
  ]
}""",
        },
    },
    {
        "inputs": {
            "job_description": """Rakuten TV is a leading streaming platform available in 42 countries across Europe, offering transactional, advertising-based, and free ad-supported streaming content. We are part of Rakuten Group, one of the world's leading internet services companies.

We are looking for a Junior AI Engineer to join our AI team and work directly with our AI Lead. You will contribute to the design, development, and deployment of AI-powered solutions across content discovery, personalization, and operational workflows.

This role is AI-first: you're expected to use AI tools in your daily work to speed up delivery while maintaining engineering rigor, traceability, and quality.

 

Responsibilities

Partner with the AI Lead to identify high-impact technical problems, translate them into concrete AI solutions and deliver them. 
AI Engineering: Build end-to-end AI workflows: data  →  model/agent logic  →  evaluation  →  deployable prototype.
Apply engineering best practices with rigor: reason about model behavior/limitations, design evaluation pipelines (golden datasets, regression tests, human-in-the-loop review).
Integrate prototypes into real systems via APIs and services, ensuring observability (latency, cost, quality).
Communication: Produce clear demos and documentation; communicate results, tradeoffs, and risks to both technical and non-technical stakeholders .

Requirements

1–3 years of experience building products end-to-end, from architecting solutions to deploying production-grade software; internships directly related to the role are also considered valuable.
Hands-on experience with LLMs or AI agents.
Proficiency in at least one programming language (Python is a plus), knowledge of Git and collaborative development practices, and familiarity with Docker and/or container technologies.
Experience with cloud-based AI platforms (AWS, GCP, Azure) and AI services from providers (OpenAI, Anthropic, and similar). 
Familiarity with MLOps practices: model versioning, experiment tracking, monitoring, and API development with FastAPI or equivalent frameworks. 
Strong understanding of AI fundamentals: why models fail, hallucinations, grounding strategies, and evaluation-driven development.

Please include your GitHub or portfolio in your application to show us the projects you have worked on :)

Nice-to-Have Requirements

Participation in hackathons or programming competitions; experience building your own products, AI agents, or automations.
Experience in a streaming, media technology context.""",
            "cv": base_cv,
        },
        "outputs": {
            "tailored_content": """{
  "header": {
    "name": "Liliia Shrainer",
    "title": "AI Engineer",
    "email": "lilischreiner3@gmail.com",
    "phone": "+34627512910",
    "location": "Valencia, Spain",
    "linkedin": "linkedin.com/in/liliia-shrainer",
    "website": ""
  },
  "summary": "AI Engineer with 2 years of experience programming in Python, AI, and LLM Engineering, specializing in building end-to-end AI solutions from prototype to production. Proven track record in multimodal LLM pipelines, AI API integration, and MLOps practices, including evaluation-driven development. Skilled in Python, FastAPI, and LangGraph with expertise in building comprehensive test suites and automated LLM extraction pipelines to ensure engineering rigor and traceability.",
  "experience": [
    {
      "title": "AI Software Engineer / LLM Developer",
      "company": "Trinetix",
      "location": "Valencia, Spain",
      "dates": "May 2025 – Present",
      "bullets": [
        "Engineered multimodal LLM pipelines and automated agent workflows (20+ autonomous agents) using LangGraph, Python, and vision models to process, enrich, and summarize unstructured data.",
        "Refactored core Python codebase to resolve critical AI API integration bugs, implementing robust retry handling, rate-limiting logic, and error handling for external model endpoints.",
        "Built comprehensive test suites using pytest to validate LLM output schemas, API integrations, and backend pipeline execution, improving overall system stability and traceability.",
        "Architected an automated LLM extraction pipeline with structured Pydantic schemas and evaluation benchmarks, achieving 99% data extraction accuracy while communicating technical progress directly to Big Four consulting stakeholders.",
        "Engineered a custom analytical scoring algorithm that matched legacy vendor performance, saving the client approximately $1,000,000 USD annually.",
        "Delivered prompt engineering lectures and workshops to over 200 non-technical employees, enhancing company-wide AI literacy and adoption.",
        "Participated in code reviews and testing cycles, ensuring the quality and reliability of AI components through collaborative development practices.",
        "Collaborated with senior engineers to integrate Large Language Models (LLMs) into existing software applications via REST APIs."
      ]
    },
    {
      "title": "Analytics & ML Consultant",
      "company": "Xyara",
      "location": "Prague, Czechia",
      "dates": "Jan 2025 – Feb 2025",
      "bullets": [
        "Advised startup leadership on machine learning pipelines and data analytics strategies in preparation for a Y Combinator pitch.",
        "Presented findings and recommendations to stakeholders, influencing data-driven decision-making across departments."
      ]
    },
    {
      "title": "Data Analyst",
      "company": "Qatar Energy COEC",
      "location": "Shanghai, China",
      "dates": "Jan 2024 – May 2024",
      "bullets": [
        "Optimized the Engineering Design Register system using Linear Algebra principles, reducing data retrieval time by 30% and improving engineering data management accuracy.",
        "Automated delay tracking workflows using JavaScript and Excel VBA, reducing manual tracking time by 40%.",
        "Developed and maintained dashboards using Tableau to visualize key performance indicators for stakeholders."
      ]
    },
    {
      "title": "Data Analyst & Engineer",
      "company": "Oxygen Biotech",
      "location": "Prague, Czechia",
      "dates": "Mar 2023 – Oct 2023",
      "bullets": [
        "Developed and maintained a real-time cryptocurrency trading data tracking system using Python, Pandas, SQL, and WebSockets.",
        "Automated data collection and enrichment through advanced web scraping pipelines using Selenium and BeautifulSoup.",
        "Optimized data processing throughput by implementing multiprocessing, threading techniques, and data normalization.",
        "Developed and maintained ETL pipelines, ensuring data accuracy and accessibility for reporting needs.",
        "Assisted in data cleaning and preprocessing, improving data quality for analytical models."
      ]
    },
    {
      "title": "Project Manager / AI Specialist",
      "company": "Legend Has It",
      "location": "Prague, Czechia",
      "dates": "Sep 2022 – Mar 2023",
      "bullets": [
        "Managed a team of 5 delivering early-stage AI-driven projects utilizing GPT-3 for persona creation and interactive workflows.",
        "Contributed prompt architecture and persona modeling for the Sophia Humanoid Robot project.",
        "Tracked project progress and communicated status updates to stakeholders, fostering transparency."
      ]
    },
    {
      "title": "Sales Manager/Coach",
      "company": "Skyeng",
      "location": "Remote",
      "dates": "Aug 2018 – Mar 2021",
      "bullets": [
        "Conducted lectures, workshops, and examinations to onboard new hires onto the sales process for 30 people.",
        "Achieved a rate 20% above the target for sales.",
        "Managed a team of 10 training specialists, including performance reviews, coaching, scheduling, and planning.",
        "Developed and implemented new sales training materials, resulting in a 10% increase in team productivity.",
        "Analyzed sales data to identify trends and opportunities, contributing to a 5% growth in quarterly revenue."
      ]
    },
    {
      "title": "Backend Developer",
      "company": "Big Johnsons Burger Joint: Full-Stack Web Application",
      "location": "",
      "dates": "Jan 2026 – Present",
      "bullets": [
        "Designed and implemented a full-stack restaurant ordering web application using FastAPI and React, integrated with SQL database storage on a self-managed Linux VPS.",
        "Handled Redsys payment gateway integration, managing secure redirects, payment callbacks, and transaction verification in FastAPI."
      ]
    },
    {
      "title": "Project Lead / Developer",
      "company": "Spanish Etymology Application",
      "location": "",
      "dates": "Oct 2025 – Present",
      "bullets": [
        "Developed an interactive language learning application that decomposes Spanish vocabulary into Latin and Greek root components to generate contextual mnemonics.",
        "Orchestrated multi-step agentic reasoning chains using LangGraph, deployed Groq API for ultra-low latency inference, and integrated LangSmith for LLM tracing and evaluation with a Streamlit interface."
      ]
    },
    {
      "title": "AI Engineer",
      "company": "LLM as a Judge: Evaluation & Feedback Pipeline",
      "location": "",
      "dates": "Dec 2025 – Jan 2026",
      "bullets": [
        "Built a multi-model evaluation pipeline combining an LLM-as-a-Teacher and an LLM-as-a-Judge to grade and correct homework responses deterministically.",
        "Utilized LangChain and Pinecone vector search for RAG-based lookup of grammar rules and ethics guidelines, triggering automatic regenerations when scores fall below thresholds."
      ]
    }
  ],
  "skills": [
    "Slack",
    "Problem Solving",
    "Version Control (Git)",
    "Ethical Judgment",
    "Analytics",
    "Communication",
    "Teamwork",
    "Collaboration",
    "Cross-Functional Communication",
    "Adaptibility",
    "Continuous Learning",
    "Python",
    "FastAPI",
    "AsyncIO",
    "pytest",
    "Multiprocessing",
    "PostgreSQL",
    "Pydantic",
    "Git",
    "REST APIs",
    "Linux VPS Deployment",
    "Streamlit",
    "Threading",
    "AWS",
    "Docker",
    "GitHub",
    "LangChain",
    "LangGraph",
    "LangSmith",
    "RAG",
    "Multimodal LLMs",
    "MLOps",
    "Prompt Optimization",
    "Guardrails",
    "Agentic Workflows",
    "Structured Outputs",
    "Model Evaluation",
    "GenAI",
    "AI Evaluation",
    "OpenAI",
    "Anthropic",
    "Weaviate",
    "Pinecone",
    "SQL",
    "Redis",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "Machine Learning Foundations",
    "PyTorch",
    "Web Scraping",
    "Linear Algebra",
    "Data Analysis",
    "Tableau",
    "Model Training",
    "PowerBI",
    "English (Fluent (C1))",
    "Spanish (Intermediate (B1))",
    "Ukrainian (Native)",
    "Chinese (Beginner)"
  ],
  "education": [
    {
      "degree": "Bachelor of Science (BS) in Computer Science",
      "school": "Kharkiv Polytechnic University",
      "dates": "Sep 2016 – Dec 2018",
      "details": "Minors: AI Data Analysis"
    },
    {
      "degree": "Certificate: CS50: Introduction to Computer Science",
      "school": "Harvard University / edX",
      "dates": "",
      "details": ""
    },
    {
      "degree": "Certificate: Introduction to FastAPI and Backend Development Fundamentals",
      "school": "",
      "dates": "",
      "details": ""
    },
    {
      "degree": "Certificate: Advanced Learning Algorithms",
      "school": "DeepLearning.AI",
      "dates": "",
      "details": ""
    },
    {
      "degree": "Certificate: Basic Image Classification with TensorFlow",
      "school": "",
      "dates": "",
      "details": ""
    }
  ]
}
            """
        },
    },
]

response = client.create_examples(dataset_id=dataset.id, examples=golden_standard)

created = response["count"] if isinstance(response, dict) else response.get("count")
print(f"Sent {len(golden_standard)} examples, LangSmith created {created}.")