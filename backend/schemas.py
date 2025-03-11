from pydantic import BaseModel, Field
from typing import Literal

class LoanApplicant(BaseModel):
    Income: float = Field(..., example=50000)
    Age: float = Field(..., example=30)
    Experience: float = Field(..., example=5)
    Married_Single: Literal["married", "single"] = Field(..., example="married")
    House_Ownership: Literal["owned", "rented", "norent_noown"] = Field(..., example="owned")
    Car_Ownership: Literal["yes", "no"] = Field(..., example="yes")
    Profession: str = Field(..., min_length=2, max_length=50, example="Software Engineer")
    CITY: str = Field(..., min_length=2, max_length=50, example="Mumbai")
    STATE: str = Field(..., min_length=2, max_length=50, example="Maharashtra")
    CURRENT_JOB_YRS: float = Field(..., example=3)
    CURRENT_HOUSE_YRS: float = Field(..., example=4)
