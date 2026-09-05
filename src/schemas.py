from pydantic import BaseModel, Field

class HeaderInfo(BaseModel):
    name: str
    title: str
    email: str
    phone: str
    location: str
    linkedin: str
    website: str


class ExperienceItem(BaseModel):
    title: str
    company: str
    location: str
    dates: str
    bullets: list[str]


class EducationItem(BaseModel):
    degree: str
    school: str
    dates: str
    details: str


class TailoredContent(BaseModel):
    header: HeaderInfo = Field(default_factory=HeaderInfo, description="The header information of the CV.")
    summary: str = Field(description="The summary of the CV.")
    experience: list[ExperienceItem] = Field(default_factory=list, description="The experience items of the CV.")
    skills: list[str] = Field(default_factory=list, description="The skills of the CV.")
    education: list[EducationItem] = Field(default_factory=list, description="The education items of the CV.")



class TailoredCVDynamic(BaseModel):
    tailored_content: TailoredContent = Field(description="The tailored CV, split into the sections the HTML template renders.")
    keywords_matched: list[str] = Field(default_factory=list, description="The keywords that were matched in the CV and the job description.")
    keywords_not_matched: list[str] = Field(default_factory=list, description="The keywords that were not matched in the CV and the job description.")
