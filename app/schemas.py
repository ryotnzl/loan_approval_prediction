from pydantic import BaseModel, constr
from typing import Literal

class LoanApplicant(BaseModel):
    Income: float
    Age: float
    Experience: float
    Married_Single: Literal["married", "single"]  # Strict enforcement
    House_Ownership: Literal["owned", "rented", "norent_noown"]  # Only these values allowed
    Car_Ownership: Literal["yes", "no"]  # Binary choice
    Profession: constr(strip_whitespace=True, min_length=2, max_length=50)  # Valid profession name
    CITY: constr(strip_whitespace=True, min_length=2, max_length=50, regex=r"^[A-Za-z\s\-]+$")  # Only letters, spaces, hyphens
    STATE: constr(strip_whitespace=True, min_length=2, max_length=50, regex=r"^[A-Za-z\s\-]+$")  # Only letters, spaces, hyphens
    CURRENT_JOB_YRS: float
    CURRENT_HOUSE_YRS: float