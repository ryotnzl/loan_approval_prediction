from pydantic import BaseModel, StringConstraints
from typing import Annotated, Literal

class LoanApplicant(BaseModel):
    Income: float
    Age: float
    Experience: float
    Married_Single: Literal["married", "single"]  # Strict enforcement
    House_Ownership: Literal["owned", "rented", "norent_noown"]  # Only these values allowed
    Car_Ownership: Literal["yes", "no"]  # Binary choice
    Profession: Annotated[str, StringConstraints(strip_whitespace=True, min_length=2, max_length=50)]  # Valid profession name
    CITY: Annotated[str, StringConstraints(strip_whitespace=True, min_length=2, max_length=50, pattern=r"^[A-Za-z\s\-]+$")]  # Only letters, spaces, hyphens
    STATE: Annotated[str, StringConstraints(strip_whitespace=True, min_length=2, max_length=50, pattern=r"^[A-Za-z\s\-]+$")]  # Only letters, spaces, hyphens
    CURRENT_JOB_YRS: float
    CURRENT_HOUSE_YRS: float