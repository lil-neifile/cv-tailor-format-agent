import json

from src.graph.nodes import tailor_cv

BASE_CV = """
Liliia Shrainer
lilischreiner3@gmail.com
+34627512910
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
AI Data Analysis
"""

JOB_DESCRIPTION = """
AI Engineer

We are looking for an AI Engineer to design and deploy LLM-powered applications.

Requirements:
- Strong Python programming skills
- Experience with LangChain and LangGraph
- LLM fine-tuning and prompt engineering
- Gemini and OpenAI API integration
- Docker and Kubernetes for model deployment
- Excellent communication and collaboration skills
"""


def test_tailor_cv_node_outputs_results():
    result = tailor_cv(
        {
            "base_cv_text": BASE_CV,
            "job_description": JOB_DESCRIPTION,
        }
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
