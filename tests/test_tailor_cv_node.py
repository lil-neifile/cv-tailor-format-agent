import json

from src.agent.tools import tailor_cv

BASE_CV = """
Carissa Perez
AI Engineer
carissa.perez@example.com
+1-234-567-8901
San Francisco, CA
https://www.linkedin.com/in/carissa-perez/
https://www.carissaperez.com

Summary:
I am an AI engineer with a passion for building scalable and efficient systems. I have experience with a variety of programming languages and frameworks, and I am always looking for new challenges and opportunities to grow.

Experience:
- AI Engineer at Google (2020 - Present)
- AI Engineer at Facebook (2018 - 2020)
- AI Engineer at Amazon (2016 - 2018)

Education:
- Bachelor of Science (BS) in Computer Science from Kharkiv Polytechnic University (2016 - 2020)
- Master of Science (MS) in Artificial Intelligence from Kharkiv Polytechnic University (2020 - 2022)
"""

JOB_DESCRIPTION = """
Your Responsibilities on this role
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

Models: OpenAI, Anthropic, AWS Bedrock, and other foundation model providers
"""


def test_tailor_cv_node_outputs_results():
    result = tailor_cv(
        {
            "base_cv_text": BASE_CV,
            "job_description": JOB_DESCRIPTION,
        }
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
