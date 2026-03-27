#출력을 JSON 포맷으로 보내야하는데 그 것을 여기서 정의 할 것
#데이터의 형태를 지정할 것
# 그냥 리포트를 만들라고 하는 것 보다 이렇게 형태를 지정하는 것이 훨씬 성능좋음

from typing import List
from pydantic import BaseModel

class Job(BaseModel):
    
    job_title: str
    company_name: str
    job_location: str
    is_remote_friendly: bool | None = None
    employment_type: str | None = None
    compensation: str | None = None
    job_posting_url: str
    job_summary: str

    key_qualifications: List[str] | None = None
    job_responsibilities: List[str] | None = None
    date_listed: date | None = None
    required_technologies: List[str] | None = None
    core_keywords: List[str] | None = None

    role_seniority_level: str | None = None
    years_of_experience_required: str | None = None
    minimum_education: str | None = None
    job_benefits: List[str] | None = None
    includes_equity: bool | None = None
    offers_visa_sponsorship: bool | None = None
    hiring_company_size: str | None = None
    hiring_industry: str | None = None
    source_listing_url: str | None = None
    full_raw_job_description: str | None = None

class JobList(BaseModel):
    jobs: List[Job]

# {
# 'jobs':[{position: 'xxx, location: 'xxx', is_remote: TRUE}]
# }