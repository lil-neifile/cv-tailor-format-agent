from langsmith import traceable
from src.workflow_agent import compiled_agent
from src.workflow import compiled_graph_divided
from langsmith.schemas import Example, Run
from langsmith.evaluation import evaluate
from litellm import completion
import json

model = "gemini/gemini-3.6-flash"
DATASET_NAME = "tailored_cv_dataset"

@traceable(run_type="chain")
def run_agent_deterministic(inputs: dict) -> dict:
    content = compiled_graph_divided.invoke(
        {
            "base_cv_text": inputs["cv"],
            "job_description": inputs["job_description"],
        }
    )
    return {"tailored_content": content.get("tailored_content")}

@traceable(run_type="chain")
def run_agent_dynamic(inputs: dict) -> dict:
    content = compiled_agent.invoke(
        {
            "cv": inputs["cv"],
            "job_description": inputs["job_description"],
        }
    )
    return {"tailored_content": content.get("tailored_content")}


def evaluate_tailored_content(run: Run, example: Example) -> dict:
    """Evaluate the tailored content of the run."""

    actual_outputs = run.outputs
    actual_tailored_cv = actual_outputs.get("tailored_content")


    golden_outputs = example.outputs
    golden_target_cv = golden_outputs.get("tailored_content")
    job_description = example.inputs.get("job_description")

    if not actual_tailored_cv:
        return {"key": "cv_alignment_score", "score": 0.0, "comment": "Error: tailored_cv was missing from output."}

    judge_prompt = f"""
    You are an expert HR and CV evaluator scoring an AI resume optimizer.
    Compare the Generated CV field against the Golden Target CV field.
    
    Assess them based on keyword match. The golden target cv would be ideally matched with a job description, and will help to pass the screening process.

    Provide your response strictly in the following JSON format:
    {{
        "reasoning": "A concise sentence explaining the grade.",
        "score": 1.0 (if it matches perfectly in keyword match) or 0.0 (if it misses key fields)
    }}

    ---
    GOLDEN TARGET CV:
    {golden_target_cv}
    
    ---
    GENERATED CV:
    {actual_tailored_cv}

    Original Job Description:
    {job_description}
    
    JSON RESPONSE:"""

    try: 
        response = completion(
            model=model,
            messages=[{"role": "user", "content": judge_prompt}],
            temperature=0.0,
            response_format={"type": "json_object"},
        )
        response_json = json.loads(response.choices[0].message.content)
        return {
            "key": "cv_alignment_score",
            "score": response_json["score"],
            "comment": response_json.get("reasoning"),
        }
    
    except Exception as e:
        return {"key": "cv_alignment_score", "score": 0.0, "comment": f"Error: {str(e)}"}


if __name__ == "__main__":
    print("⏳ Running evaluation on 'tailored_cv' field...")
    
    evaluate(
        run_agent_deterministic,
        data=DATASET_NAME,
        evaluators=[evaluate_tailored_content],
        experiment_prefix="CV-GRAPH-DIVIDED-Comparison"
    )
    
    print("🎉 Done! Open your LangSmith dashboard to compare the CV metrics side-by-side.")

