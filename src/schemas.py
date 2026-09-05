from pydantic import BaseModel, Field

class HeaderInfo(BaseModel):
    name: str = ""
    title: str = ""
    email: str = ""
    phone: str = ""
    location: str = ""
    linkedin: str = ""
    website: str = ""


class ExperienceItem(BaseModel):
    title: str = ""
    company: str = ""
    location: str = ""
    dates: str = ""
    bullets: list[str] = Field(default_factory=list)


class EducationItem(BaseModel):
    degree: str = ""
    school: str = ""
    dates: str = ""
    details: str = ""


class TailoredContent(BaseModel):
    header: HeaderInfo = Field(default_factory=HeaderInfo, description="The header information of the CV.")
    summary: str = Field(description="The summary of the CV.")
    experience: list[ExperienceItem] = Field(default_factory=list, description="The experience items of the CV.")
    skills: list[str] = Field(default_factory=list, description="The skills of the CV.")
    education: list[EducationItem] = Field(default_factory=list, description="The education items of the CV.")

    class Config:
        json_schema_extra = {
            "example": {
                "header": {
                    "name": "John Doe",
                    "title": "Software Engineer",
                    "email": "john.doe@example.com",
                    "phone": "123-456-7890", 
                    "location": "San Francisco, CA",
                    "linkedin": "https://www.linkedin.com/in/john-doe",
                    "website": "https://www.john-doe.com"
                },
                "summary": "A summary of the CV.",
                "experience": [
                    {
                        "title": "Software Engineer",
                        "company": "Google",
                        "location": "San Francisco, CA",
                        "dates": "2020-2024",
                        "bullets": [
                            "Developed and maintained web applications using React and Node.js",
                            "Implemented RESTful APIs for data retrieval and manipulation"
                        ]
                    }
                ],
                "skills": [
                    "React",
                    "Node.js",
                    "JavaScript",
                    "HTML",
                    "CSS",  
                ],
                "education": [
                    {
                        "degree": "Bachelor of Science in Computer Science",
                        "school": "University of California, Berkeley",
                        "dates": "2016-2020",
                        "details": "Graduated with honors"
                    }
                ]
            }
        }


class JobDescriptionAnalyzer(BaseModel):
    job_role_name: str = Field(default="", description="The name of the job role.")
    high_importance_keywords: list[str] = Field(default_factory=list, description="The high importance keywords of the job description.")
    medium_importance_keywords: list[str] = Field(default_factory=list, description="The medium importance keywords of the job description.")
    low_importance_keywords: list[str] = Field(default_factory=list, description="The low importance keywords of the job description.")

    class Config:
        json_schema_extra = {
            "example": {
                "job_role_name": "AI Engineer",
                "high_importance_keywords": ["Python", "SQL", "AWS"],
                "medium_importance_keywords": ["React", "Node.js", "JavaScript"],
                "low_importance_keywords": ["HTML", "CSS"]
            }
        }

class CompareCVWithJobDescription(BaseModel):
    skills_match: list[str] = Field(default_factory=list, description="The skills that are present in the CV and represent the provided importance.")
    skills_present_importance_lower_than_expected: list[str] = Field(default_factory=list, description="The skills that are present in the CV, but not according to the importance, lower than expected.")
    skills_present_different_wording: list[str] = Field(default_factory=list, description="The skills that are present in the CV, but with a different wording than the one used in the list of skills.")
    skills_missing: list[str] = Field(default_factory=list, description="The skills that are missing in the CV.")

    class Config:
        json_schema_extra = {
            "example": {
                "skills_present": ["Python", "SQL", "AWS"],
                "skills_present_importance_lower_than_expected": ["React", "Node.js", "JavaScript"],
                "skills_present_different_wording": ["React", "Node.js", "JavaScript"]

            }
        }

class TailoredCVDynamic(BaseModel):
    tailored_content: TailoredContent = Field(description="The tailored CV, split into the sections the HTML template renders.")
    keywords_matched: list[str] = Field(default_factory=list, description="The keywords that were matched in the CV and the job description.")
    keywords_not_matched: list[str] = Field(default_factory=list, description="The keywords that were not matched in the CV and the job description.")

    class Config:
        json_schema_extra = {
            "example": {
                "tailored_content": TailoredContent.Config.json_schema_extra["example"],
                "keywords_matched": ["Python", "SQL", "AWS"],
                "keywords_not_matched": ["React", "Node.js", "JavaScript"]
            }
        }